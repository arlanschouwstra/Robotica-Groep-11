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
int boxsize = 320 / aantal_menus;

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

#define BT  Serial1
#define PC  Serial

// Verbonden via Serieel of BT
#define WIRED   true

// Waardes van de joysticks
// y_rechts omkeren wegens orientatie van de joystick
#define x_rechts  map(analogRead(A12), 0, 1023, 11, 19)
#define y_rechts  map(analogRead(A13), 0, 1023, 19, 11)

#define x_links  map(analogRead(A8), 0, 1023, 11, 19)
#define y_links  map(analogRead(A9), 0, 1023, 11, 19)

#define LButton_pin 25
#define RButton_pin 49
#define LButton     digitalRead(LButton_pin) == HIGH
#define RButton     digitalRead(RButton_pin) == HIGH
int LButton_old = 0;
int RButton_old = 0;

// Flank variabelen
int xr_old = 0;
int yr_old = 0;
int xl_old = 0;
int yl_old = 0;
boolean old_lb = 0;
boolean old_rb = 0;
int old_mode = 0;
uint16_t picked_color = 0;
uint16_t old_color = picked_color;
//int old[7];
int old[7] = {xl_old, yl_old, xr_old, yr_old, old_lb, old_rb, mode};
int current[7] = {x_links, y_links, x_rechts, y_rechts, LButton, RButton, mode};
String names[7] = {"lx: ", "ly: ", "rx: ", "ry: ", "LB: ", "RB: ", "md: "};
//int current[7];
int y;
int x;

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
    pinMode(A9, INPUT);
    pinMode(A12, INPUT);
    pinMode(A13, INPUT);

    pinMode(18, OUTPUT); // BT TX
    pinMode(19, INPUT);  // BT RX

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
    //old[0] = x_links;
    //old[1] = y_links;
    //old[2] = x_rechts;
    //old[3] = y_rechts;
// old[4]= LButton;
    //old[5] = RButton;
    //old[6] = mode;
    //current[0] = x_links;
   // current[1] = y_links;
    //current[2] = x_rechts;
   // current[3] = y_rechts;
// current[4]= LButton;
// current[5] = RButton;
// current[6] = mode;

    drawMenus(0);
    handleMenus();
}

void loop() {
    // Zodra joystick waardes veranderen stuur via serieel of BT
    // Flank variabelen
    checkChange();
    // Wait for a touch
    if (!ctp.touched()) {
        return;
    }

    handleTouchEvent();
}

