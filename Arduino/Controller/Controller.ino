// Datum : 03-06-2018
// Naam  : Steven Wijnja
// Versie: 1.1
// Omschr: Controller

#include <Adafruit_GFX.h>    // Core graphics library
#include <SPI.h>       // this is needed for display
#include <Adafruit_ILI9341.h>
#include <Wire.h>      // this is needed for FT6206
#include <Adafruit_FT6206.h>
#include <SoftwareSerial.h>

// The FT6206 uses hardware I2C (SCL/SDA)
Adafruit_FT6206 ctp = Adafruit_FT6206();

// The display also uses hardware SPI, plus #9 & #10
#define TFT_CS 10
#define TFT_DC 9
Adafruit_ILI9341 tft = Adafruit_ILI9341(TFT_CS, TFT_DC);

// Aantal menus
#define aantal_menus  4
int boxsize = 320/aantal_menus;

// Huidige status van controller, oftewel in welk menu we zitten
int state = 0,
    old_state = 0;

// Mode van de robot
int mode = 0;
#define VW_MAX_MESSAGE_LEN  40
char tx_buf[VW_MAX_MESSAGE_LEN];
// Define colors
#define GRAY  RGB(38, 37, 36)
#define BLACK ILI9341_BLACK
#define RED  RGB(255, 0, 0)
#define ORANGE RGB(0, 51, 0)

uint16_t picked_color = 0;

// Waardes van de joysticks
// y_rechts omkeren wegens orientatie van de joystick
#define x_rechts  map(analogRead(A12), 0, 1023, 11, 19)
#define y_rechts  map(analogRead(A13), 0, 1023, 29, 21)

#define x_links  map(analogRead(A8), 0, 1023, 31, 39)
#define y_links  map(analogRead(A9), 0, 1023, 41, 49)

#define LButton_pin 25
#define RButton_pin 49
#define LButton     digitalRead(LButton_pin) == HIGH
#define RButton     digitalRead(RButton_pin) == HIGH

// Flank variabelen
int xr_old = x_rechts;
int yr_old = y_rechts;
int xl_old = x_links;
int yl_old = y_links;
boolean old_lb = LButton;
boolean old_rb = RButton;
int old_mode = mode;
uint16_t old_color = picked_color;

#define BT  Serial1
#define PC  Serial

// Verbonden via Serieel of BT
#define WIRED   true

long int timer = millis();
String wired_string;
float volt = 11.1;

/* TODO
 *  1. WIRED of BT keuze in menu zetten
 *  2. enableRecieve, zoek uit of reciever op pin 18 of 19 zit
 *  3. enableTransmit, zelfde voor transmitting
 *  4. Virtuelwire weghalen zodra RCSwitch getest is
 */

void setup(void) {
    pinMode(LButton_pin, INPUT);
    pinMode(RButton_pin, INPUT);

    pinMode(A8, INPUT);
    pinMode(A9, INPUT );
    pinMode(A12, INPUT);
    pinMode(A13, INPUT);
    
    pinMode(18, OUTPUT); // BT TX
    pinMode(19, INPUT);  // BT RX


    /* Virtuelwire - kan weg na testen van RCSwitch
    vw_set_ptt_inverted(true); //
    vw_set_tx_pin(18);
    vw_set_rx_pin(19);
    vw_setup(2000); // speed of data transfer Kbps
    */
    
    while (!Serial); // used for leonardo debugging

    // Initialiseer Seriele verbindingen en scherm
    PC.begin(115200);
    PC.println(F("Cap Touch Paint!"));
    BT.begin(9600);
    tft.begin();

    if (!ctp.begin(40)) { // pass in 'sensitivity' coefficient
        PC.println("Couldn't start FT6206 touchscreen controller");
        while (1);
    }

    PC.println("Capacitive touchscreen started");
    
    picked_color = GRAY;
    tft.setRotation(1);

    drawMenus(0);
    handleMenus();
}

void loop() {
    // Zodra joystick waardes veranderen stuur via serieel of BT
    if (xl_old != x_links || yl_old != y_links || xr_old != x_rechts || yr_old != y_links) {
        // Flank variabelen
        xl_old = x_links;
        yl_old = y_links;
        xr_old = x_rechts;
        yr_old = y_rechts;
        sprintf(tx_buf, "XL=%d&YL=%d&XR=%d&YR=%d&LB=%d&RB=%d&mode=%d&c=%d", xl_old, yl_old, xr_old, yr_old, LButton, RButton, mode, picked_color);
        if (WIRED) {
            //send information to touchscreen
            sendToScreen(1000000, xl_old);
            sendToScreen(2000000, yl_old);
            sendToScreen(3000000, xr_old);
            sendToScreen(4000000, yr_old);
            sendToScreen(5000000, LButton);
            sendToScreen(6000000, RButton);
            sendToScreen(7000000, mode);
            //int scaled_color = map(picked_color, 0, 65536, 0, 999);
            sendToScreen(8000000, picked_color);  
        }
        // Refresh BT menu
        if (state == 3) handleMenus();
    }
    //send to bluetooth (used for arm and tank)
    String datatosend = String(x_links) + String(y_links) + String(x_rechts) + String(y_rechts) + String(LButton) + String(RButton) + String(mode);
    sendbluetooth(datatosend);
    // Ontvang data van serieel of BT en zet dit in rx_buf of wired_string
    // Waarom twee aparte variabelen voor opslaan?
    if (WIRED) {
        if(Serial.available() > 0) {
            wired_string = Serial.readStringUntil('\n');
        }
    } 
    //checking for availability
    PC.println("available");
    
    // Wait for a touch
    if (!ctp.touched()) {
        return;
    }
    // Retrieve a point  
    TS_Point px = ctp.getPoint(),
              p = ctp.getPoint();

    // flip it around to match the screen.
    p.x = map(px.y, 0, 320, 320, 0);
    p.y = map(px.x, 0, 240, 0, 240);

    // alles onder y < 40 is menu
    if (p.y < 40) {
        // Menukeuze op basis van x coordinaat
        for (int i = 0; i < aantal_menus; i++) {
            if (p.x < (i + 1) * boxsize) {
                if (i != old_state) { // Voorkomen van flikkeren
                    drawMenus(i);
                    state = i;
                }
                break;
            }
        }
    // Geen touch op menu, handle menu opties
    // Handlemenus() vervangen wegens knipperen van scherm
    } else if (state == 0) {  // Hoofdmenu
        if (p.x > 18 && p.x < 138) {
            if (p.y > 45 && p.y < 100) {
                mode = 0;
                checkModeVsOldMode(mode, old_mode);
            }
            if (p.y > 110 && p.y < 165) {
                mode = 1;
                checkModeVsOldMode(mode, old_mode);
            }
            if (p.y > 175 && p.y < 230) {
                mode = 2;
                checkModeVsOldMode(mode, old_mode);
            }
        } else if (p.x > 148 && p.x < 268) {
            if (p.y > 45 && p.y < 100) {
                mode = 3;
                checkModeVsOldMode(mode, old_mode);
            }
            if (p.y > 110 && p.y < 165) {
                mode = 4;
                checkModeVsOldMode(mode, old_mode);
            }
            if (p.y > 175 && p.y < 230) {
                mode = 5;
                checkModeVsOldMode(mode, old_mode);
            }
        }
    } else if (state == 2) {  // Colorpicker
        float hue = (float) p.x / 320.0;
        float saturation = 1;
        float lightness = ((float) p.y - 40.0) / (240.0 - 10.0);
        if (picked_color != hslToRgb(hue, saturation, lightness)) {

            tft.fillRect(2 * boxsize, 0, boxsize, 40, hslToRgb(hue, saturation, lightness));
            tft.setCursor(0, 2);
            tft.setTextColor(ILI9341_WHITE);
            tft.setTextSize(2);
            tft.println("              Color");
            tft.println("              picker");
            picked_color = hslToRgb(hue, saturation, lightness);
        }
    }

    // Zodra menukeuze veranderd, scherm refreshen
    if (state != old_state) {
        handleMenus();
        old_state = state;
    }

}

void sendbluetooth(String string){
       BT.println(string);
       BT.flush();  
  }

void sendToScreen(int number, int data) {
      PC.println(number + data);
  }

void checkModeVsOldMode(int newMode, int oldMode){
                if (newMode != oldMode) {
                    drawButton(mode);
                    drawButton(old_mode);
                    //handleMenus();
                    old_mode = mode;
                }  
}

