// Datum : 03-06-2018
// Naam  : Steven Wijnja
// Versie: 1.1
// Omschr: Controller

#include <Adafruit_GFX.h>    // Core graphics library
#include <SPI.h>       // this is needed for display
#include <Adafruit_ILI9341.h>
#include <Wire.h>      // this is needed for FT6206
#include <Adafruit_FT6206.h>

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

// Define colors
#define GRAY  RGB(38, 37, 36)
#define BLACK ILI9341_BLACK
#define RED  RGB(255, 0, 0)
#define ORANGE RGB(0, 51, 0)

uint16_t picked_color = 0;

// Waardes van de joysticks
// y_rechts omkeren wegens orientatie van de joystick
#define x_rechts  map(analogRead(A12), 0, 1023, 1, 9)
#define y_rechts  map(analogRead(A13), 0, 1023, 19, 11)

#define x_links  map(analogRead(A8), 0, 1023, 21, 29)
#define y_links  map(analogRead(A9), 0, 1023, 31, 39)

#define LButton_pin 25
#define RButton_pin 49
#define LButton     digitalRead(LButton_pin) == HIGH
#define RButton     digitalRead(RButton_pin) == HIGH

// Virtuelwire - vervangen zodra RCSwitch getest is
#define VW_MAX_MESSAGE_LEN  40

// RF variables
char tx_buf[VW_MAX_MESSAGE_LEN];
uint8_t rx_buf[VW_MAX_MESSAGE_LEN];
uint8_t buflen = VW_MAX_MESSAGE_LEN;

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

// Verbonden via Serieel of RF
#define WIRED   true

long int timer = millis();
String wired_string;
float volt = 11.1;

/* TODO
 *  1. WIRED of RF keuze in menu zetten
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
    
    pinMode(18, OUTPUT); // RF TX
    pinMode(19, INPUT);  // RF RX


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
    // Zodra joystick waardes veranderen stuur via serieel of RF
    if (xl_old != x_links || yl_old != y_links || xr_old != x_rechts || yr_old != y_links) {
        // Flank variabelen
        xl_old = x_links;
        yl_old = y_links;
        xr_old = x_rechts;
        yr_old = y_rechts;

        // Make a char array with joystick values, button pressed and current mode
        sprintf(tx_buf, "XL=%d&YL=%d&XR=%d&YR=%d&LB=%d&RB=%d&mode=%d&c=%d", xl_old, yl_old, xr_old, yr_old, LButton, RButton, mode, picked_color);

        if (WIRED) {
            //send information to touchscreen
            PC.println(1000000 + xl_old);
            PC.println(2000000 + yl_old);
            PC.println(3000000 + xr_old);
            PC.println(4000000 + yr_old);
            PC.println(5000000 + LButton);
            PC.println(6000000 + RButton);
            PC.println(7000000 + mode);
            //int scaled_color = map(picked_color, 0, 65536, 0, 999);
            PC.println(8000000 + picked_color);  
        }
        // Refresh RF menu
        if (state == 3) handleMenus();
    }
    //send to bluetooth (used for arm and tank)
    if(BT.available())  {
        BT.println(x_links);
        BT.println(y_links);
        BT.println(x_rechts);
        BT.println(y_rechts);
    } 
    
    // Ontvang data van serieel of RF en zet dit in rx_buf of wired_string
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
        if (p.x > 18 && p.x < (18 + 120)) {
            if (p.y > 45 && p.y < (45 + 55)) {
                mode = 0;
                if (mode != old_mode) {
                    drawButton(mode);
                    drawButton(old_mode);
                    //handleMenus();
                    old_mode = mode;
                }
            }
            if (p.y > 110 && p.y < (110 + 55)) {
                mode = 1;
                if (mode != old_mode) {
                    drawButton(mode);
                    drawButton(old_mode);
                    //handleMenus();
                    old_mode = mode;
                }

            }
            if (p.y > 175 && p.y < (175 + 55)) {
                mode = 2;
                if (mode != old_mode) {
                    drawButton(mode);
                    drawButton(old_mode);
                    //handleMenus();
                    old_mode = mode;
                }
            }
        } else if (p.x > 148 && p.x < (148 + 120)) {
            if (p.y > 45 && p.y < (45 + 55)) {
                mode = 3;
                if (mode != old_mode) {
                    drawButton(mode);
                    drawButton(old_mode);
                    //handleMenus();
                    old_mode = mode;
                }
            }
            if (p.y > 110 && p.y < (110 + 55)) {
                mode = 4;
                if (mode != old_mode) {
                    drawButton(mode);
                    drawButton(old_mode);
                    //handleMenus();
                    old_mode = mode;
                }
            }
            if (p.y > 175 && p.y < (175 + 55)) {
                mode = 5;
                if (mode != old_mode) {
                    drawButton(mode);
                    drawButton(old_mode);
                    //handleMenus();
                    old_mode = mode;
                }
            }
        }
    } else if (state == 1) {  // Batterij status
      
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
    } else if (state == 4) {
      
    }

    // Zodra menukeuze veranderd, scherm refreshen
    if (state != old_state) {
        handleMenus();
        old_state = state;
    }

}

