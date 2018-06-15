#include <Servo.h>
#include <Wire.h>
#include <Serial>
#include <FastLED.h>

/*  for LED-MATRIX*/
#define LED_PIN     12
#define NUM_LEDS    80
#define led_per_bar 8
#define brightness  255     // Scale 0-255
#define MIRROR      false    // Mirror vertically
/*  for SOUNDFILTERS*/
#define lowpass_pin   A0
#define bandpass_pin  A2
#define highpass_pin  A1
/*  for wheels*/
#define left_forward_pin
#define left_backward_pin
#define left_speed_pin
#define right_forward_pin
#define right_backward_pin
#define right_speed_pin

CRGB leds[NUM_LEDS];

/*GROEP 11*/
const uint64_t IMAGES[] PROGMEM = {
  0x0080808080800000,
  0x8040404040408000,
  0xc02020a02020c000,
  0xe01010d01010e000,
  0x708888680808f000,
  0x3844443404047800,
  0x1c22221a02023c00,
  0x0e11110d01011e00,
  0x0708080600000f00,
  0x1314141310101700,
  0x090a0a1908081b00,
  0x0405051c04041d00,
  0x1212120e12120e00,
  0x0909090709090700,
  0x0404141314040300,
  0x02120a090a120100,
  0x1905050405051800,
  0x1c02020202021c00,
  0x0e11111111110e00,
  0x0708080808080700,
  0x1314141414141300,
  0x190a0a1a0a0a1900,
  0x1c05051d05051c00,
  0x0e02020e02020e00,
  0x1711111711111700,
  0x0b08081b08081b00,
  0x0504041d04041d00,
  0x0202020e12120e00,
  0x0101010709090700,
  0x1000000304140300,
  0x18000001020a1100,
  0x1c10101011151800,
  0x1e080808080a0c00,
  0x1f04040404050600,
  0x0f02020202020300,
  0x1701010101110100,
  0x1b00000000081000,
  0x1d10101010141800,
  0x1e080808080a0c00,
  0x1f04040404050600,
  0x0f02020202020300,
  0x0701010101010100,
  0x0300000000000000,
  0x0100000000000000,
  0x0000000000000000
};

/*DAFT PUNK*/
const uint64_t IMAGES2[] = {
  0x0000000000000000,
  0x1010101010101000,
  0x1818181818181800,
  0x1c0c0c0c0c0c1c00,
  0x1e06060606061e00,
  0x1f13131313131f00,
  0x0f19191919190f00,
  0x070c0c0c0c0c0700,
  0x0306060606060300,
  0x1113131313130100,
  0x1819191919191000,
  0x0c0c0c1c0c0c1800,
  0x0606061e06061c00,
  0x1313131f13131e00,
  0x1919191f19190f00,
  0x0c0c0c0f0c0c0700,
  0x0606060706060300,
  0x1313131313131100,
  0x1919191919191800,
  0x0c0c0c1c0c0c1c00,
  0x0606061e06061e00,
  0x0303031f03031f00,
  0x0101010f01011f00,
  0x0000000700000f00,
  0x0000000300000700,
  0x0000000100101300,
  0x0000000000081900,
  0x1010101010141c00,
  0x18181818181a1e00,
  0x0c0c0c0c0c0d1f00,
  0x0606060606161f00,
  0x03030303030b0f00,
  0x0101010101050700,
  0x0000000000020300,
  0x0000000000010100,
  0x1010101010101000,
  0x1818181818181800,
  0x0c0c1c0c0c0c1c00,
  0x06061e0606061e00,
  0x03031f1313131f00,
  0x01010f1919190f00,
  0x0000070c0c0c0700,
  0x0000030606060300,
  0x0010111313131100,
  0x1018181919191800,
  0x180c0c0c0c0c0c00,
  0x1c06060606060600,
  0x1e13131313131300,
  0x1f19191919191900,
  0x0f0c0c0c0c0c0c00,
  0x0706060606060600,
  0x1313131313131300,
  0x1919191919191900,
  0x0c0c0c0c1c1c0c00,
  0x060606161e0e0600,
  0x0303131b0f070300,
  0x1111191d17131100,
  0x18181c1e1b191800,
  0x0c0c0e0f0d0c0c00,
  0x0606070706060600,
  0x1313131313131300,
  0x1919191919191900,
  0x0c0c1c1c1c0c0c00,
  0x06161e0e1e160600,
  0x131b0f070f1b1300,
  0x190d0703070d1900,
  0x0c06030103060c00,
  0x0603010001030600,
  0x0301000000010300,
  0x0100000000000100
};
/*  apple,bottom jeans, boots*/
const uint64_t IMAGES3[] = {
  
};

/*  get low*/
const uint64_t IMAGES4[] = {
  
};
/*  don't break my heart*/
const uint64_t IMAGES5[] = {
  
};
/*  candy_man*/
const uint64_t IMAGES6[] = {
  
};
/*  metallica*/
const uint64_t IMAGES7[] = {
  0x0000000000000000,
  0x1010101010101000,
  0x1818181818181800,
  0x0c0c0c0c1c1c0c00,
  0x060606161e0e0600,
  0x0303030b1f170300,
  0x111111151f1b1100,
  0x1818181a1f1d1800,
  0x0c0c0c0d0f0e0c00,
  0x0606060607070600,
  0x1313131313131300,
  0x1919191919191900,
  0x1c0c0c1c0c0c1c00,
  0x1e06061e06061e00,
  0x1f03031f03031f00,
  0x1f01011f01011f00,
  0x0f00000f00000f00,
  0x0700000700000700,
  0x0300000300101300,
  0x0100000100081900,
  0x1010101010141c00,
  0x18181818181a1e00,
  0x0c0c0c0c0c0d1f00,
  0x0606060606161f00,
  0x03030303030b0f00,
  0x0101010101050700,
  0x1010101010120300,
  0x1818181818191100,
  0x0c0c0c1c0c0c1800,
  0x0606061e06061c00,
  0x1313131f13131e00,
  0x1919191f19190f00,
  0x0c0c0c0f0c0c0700,
  0x0606060706060300,
  0x1313131313131100,
  0x1919191919191800,
  0x1c0c0c0c0c0c0c00,
  0x1e06060606060600,
  0x1f03030303030300,
  0x1f01010101010100,
  0x0f00000000000000,
  0x0700000000000000,
  0x1310101010101000,
  0x1918181818181800,
  0x1c0c0c0c0c0c0c00,
  0x1e06060606060600,
  0x1f03030303030300,
  0x1f01010101010100,
  0x0f00000000000000,
  0x0700000000000000,
  0x1300000000001000,
  0x1910101010101800,
  0x1c18181818181c00,
  0x1e0c0c0c0c0c1e00,
  0x0f06060606060f00,
  0x0703030303030700,
  0x0311111111110300,
  0x1118181818181100,
  0x180c0c0c0c0c1800,
  0x1c06060606061c00,
  0x1e13030303131e00,
  0x0f19010101190f00,
  0x070c0000000c0700,
  0x0306000000060300,
  0x1113101010130100,
  0x1819181818191000,
  0x0c0c0c1c0c0c1800,
  0x0606061e06061c00,
  0x1313131f13131e00,
  0x1919191f19190f00,
  0x0c0c0c0f0c0c0700,
  0x0606060706060300,
  0x0303030303030100,
  0x0101010101010000
};
/*  moonlight*/
const uint64_t IMAGES8[] = {
  0x0000000000000000,
  0x1010101010101000,
  0x1818181818181800,
  0x0c0c0c0c1c1c0c00,
  0x060606161e0e0600,
  0x0303030b1f170300,
  0x111111151f1b1100,
  0x1818181a1f1d1800,
  0x0c0c0c0d0f0e0c00,
  0x0606060607070600,
  0x0313131313130300,
  0x1119191919191100,
  0x180c0c0c0c0c1800,
  0x1c06060606061c00,
  0x1e13131313131e00,
  0x0f19191919190f00,
  0x070c0c0c0c0c0700,
  0x0306060606060300,
  0x0113131313130100,
  0x1019191919191000,
  0x180c0c0c0c0c1800,
  0x1c06060606061c00,
  0x1e13131313131e00,
  0x0f19191919190f00,
  0x070c0c0c0c0c0700,
  0x0306060606060300,
  0x1113131313131100,
  0x1819191919191800,
  0x0c0c0c0c1c1c0c00,
  0x060606161e0e0600,
  0x0303131b0f070300,
  0x1111191d17131100,
  0x18181c1e1b191800,
  0x0c0c0e0f0d0c0c00,
  0x0606070706060600,
  0x1313131313131300,
  0x1919191919191900,
  0x1c0c0c0c0c0c0c00,
  0x1e06060606060600,
  0x1f03030303030300,
  0x1f01010101010100,
  0x0f00000000000000,
  0x0700000000000000,
  0x1300000000001000,
  0x1910101010101800,
  0x1c18181818181c00,
  0x1e0c0c0c0c0c1e00,
  0x0f06060606060f00,
  0x0703030303030700,
  0x0311111111110300,
  0x1118181818181100,
  0x180c0c0c0c0c1800,
  0x1c06160606061c00,
  0x1e131b0303131e00,
  0x0f191d0101190f00,
  0x070c0e00000c0700,
  0x0306070000060300,
  0x1113131010131100,
  0x1819191818191800,
  0x0c0c0c1c0c0c0c00,
  0x0606061e06060600,
  0x1313131f13131300,
  0x1919191f19191900,
  0x0c0c0c0f0c0c0c00,
  0x0606060706060600,
  0x0303030303131300,
  0x0101010101091900,
  0x1010101010141c00,
  0x18181818181a1e00,
  0x0c0c0c0c0c0d1f00,
  0x0606060606161f00,
  0x03030303030b0f00,
  0x0101010101050700,
  0x0000000000020300,
  0x0000000000010100,
  0x0000000000000000
};

const int IMAGES_LEN = sizeof(IMAGES)/8;
const int IMAGES_LEN2 = sizeof(IMAGES2)/8;
const int IMAGES_LEN3 = sizeof(IMAGES3)/8;
const int IMAGES_LEN4 = sizeof(IMAGES4)/8;
const int IMAGES_LEN5 = sizeof(IMAGES5)/8;
const int IMAGES_LEN6 = sizeof(IMAGES6)/8;
const int IMAGES_LEN7 = sizeof(IMAGES7)/8;
const int IMAGES_LEN8 = sizeof(IMAGES8)/8;
/*==============================================================================
 * CHECKSTRING()
 *============================================================================*/
void checkString(buttonString){
    if(buttonString == "checkSong"){
      soundFilterDance()
    }
    else if(buttonString == "dance_start"){
      LEDDance()
    }
    else if(buttonString == "line_dance_start"){
      soundFilterLineDance()
    }
    else if(buttonString == "display_group_name"){
      displayGroupName()
    }
    if(buttonString != "display_group_name"){
      FastLED.clear();
      FastLED.show();
    }
}
/*==============================================================================
 * LEDMATRIX()
 *============================================================================*/
void displayImage(uint64_t image, uint8_t offset, CRGB color) {
    for (int rows = 0; rows < 8; rows++) {
        byte row = (image >> (7 - rows) * 8) & 0xFF;/*  shifts the bits in image to the right by (7-rows)*8. “& 0xff” effectively masks the variable so it leaves only the value in the last 8 bits, and ignores all the rest of the bits.*/
        for (int col = 0; col < 5; col++) {
            if (bitRead(row, col)) {
                int index = (MIRROR ? 4 - col : col) * 8 + rows;
                leds[index + offset] = color;
            }
        }
    }   
}

int j = 0;
byte hue = 0;
/*  start when signal displayGroupName is received.*/
void displayGroupName(){
    // Display the image
    uint64_t image;
    memcpy_P(&image, &IMAGES[j],8); /*  (destination,source,num) Copies the values of num bytes from the location pointed to by source directly to the memory block pointed to by destination.*/
    
    hue = map(j, 0, IMAGES_LEN, 0, 255); /* map(value, fromLow, fromHigh, toLow, toHigh) Re-maps a number from one range to another. That is, a value of fromLow would get mapped to toLow, a value of fromHigh to toHigh, values in-between to values in-between, etc.*/
    /*image,offset,color(hue,saturation,value)*/
    displayImage(image, 0, CHSV(hue, 255, 150));
    
    /*display on the 2nd led matrix. both led matrices are 5 leds wide.*/
    if (j + 5  < IMAGES_LEN ) {
        memcpy_P(&image, &IMAGES[j+5],8);
        displayImage(image, 40, CHSV(hue, 255, 255));/* 40 is the LED NUMBER where 2nd matrix starts*/
    }
    /*  if the next iteration goes past the image size, reset j & hue*/
    if (++j >= IMAGES_LEN) j = 0;/* updates the j value, till it reaches IMAGES_LEN, causes the color to change due to hue.*/
    if (++hue >= 255) hue = 0;

    FastLED.show();
    FastLED.delay(100);
}
/*  start when signal danceStart is received AND SOUNDFILTER() returns a value to notify music has started.*/
LEDDance(){
    /*  time the switch of the IMAGES[] to the music.*/
}
/*==============================================================================
 * SOUNDFILTER()
 *============================================================================*/
int lowpass_max = 800;
int midpass_max = 650;
int highpass_max = 1023;
/*NEEDS TO CHECK FOR A SPECIFIED SOUND PITCH FOR DANCE AND LINEDANCE*/
void soundFilterDance(){
    int lowpass_signal = analogRead(lowpass_pin);
    int lowpass = map(lowpass_signal, 0,  lowpass_max , 1, 9); /*converts actual values to a number from 0 to 100.*/
    
    int bandpass_signal = analogRead(bandpass_pin);
    int bandpass = map(bandpass_signal, 0,midpass_max, 1, 9);
    
    int highpass_signal = analogRead(highpass_pin);
    int highpass = map(highpass_signal, 0, highpass_max, 1, 9);
    Serial.println(String(lowpass)+String(bandpass)+String(highpass))
}

void lineDance(){   
    int lowpass_signal = analogRead(lowpass_pin);
    int lowpass = map(lowpass_signal, 0,  lowpass_max , 0, led_per_bar);/*  converts 0 to lowpass_max into 0 to 8 and puts the value into lowpass.*/
    Serial.print("lowpass_signal: ");
    Serial.println(lowpass_signal);

    int bandpass_signal = analogRead(bandpass_pin);
    int bandpass = map(bandpass_signal, 0,midpass_max, 0, led_per_bar);
    Serial.print("bandpass_signal: ");
    Serial.println(bandpass_signal);

    int highpass_signal = analogRead(highpass_pin);
    int highpass = map(highpass_signal, 0, highpass_max, 0, led_per_bar);
    Serial.print("highpass_signal: ");
    Serial.println(highpass_signal);
    
    int R, G, B;
    // turn all leds off
    for (int i = 0; i < 80; i++) leds[i] = CRGB(0, 0, 0);
    
    while (lowpass--) {
        R = lowpass > led_per_bar * 0.33 ? 255 : 0;
        G = lowpass < led_per_bar * 0.66 ? 255 : 0;
        B = 0;
        leds[lowpass] = CRGB(R, G, B); /* while lowpass is on, all the leds in the range it has are turned on.*/
    }
    
    while (bandpass--) {
        R = bandpass > led_per_bar * 0.33 ? 255 : 0;/*if bandpass > led_per_bar*0.33, then 255, else 0*/
        G = bandpass < led_per_bar * 0.66 ? 255 : 0;
        B = 0;
        leds[bandpass + led_per_bar] = CRGB(R, G, B);
    }
    while (highpass--) {
        R = highpass > led_per_bar * 0.33 ? 255 : 0;
        G = highpass < led_per_bar * 0.66 ? 255 : 0;
        B = 0;
        leds[highpass + 2*led_per_bar] = CRGB(R, G, B);
    }
       
    FastLED.show();
    delay(10);
}
/*==============================================================================
 * SETUP()
 *============================================================================*/
void setup() {
  // put your setup code here, to run once:
  //  pin used for LED MATRIX
  FastLED.addLeds < WS2812, LED_PIN, GRB > (leds, NUM_LEDS);
  FastLED.setBrightness(brightness);
  Serial.begin(9600);
  //  pins used for sound filters.
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
}
/*==============================================================================
 * LOOP()
 *============================================================================*/
void loop() {
  // put your main code here, to run repeatedly:
  // Turn all leds off
  FastLED.clear();
  
  if (Serial.available()) {
    checkString(Serial.read())/*read command from PI*/
    /*sendback = Serial.read()*/
    /*Serial.println(sendback);*/
    
    
  }
}
