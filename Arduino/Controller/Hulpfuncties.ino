void drawMenus(uint8_t keuze) { 
  // Menublokken
  int color;
  for (int i = 0; i < aantal_menus; i++) {
    color = (i == 2 && keuze == i) ? picked_color : (keuze == i ? GRAY : BLACK);
    tft.fillRect(i*boxsize, 0, boxsize, 40, color);
  }

  // Menu teksten
  tft.setCursor(0, 2);
  tft.setTextColor(ILI9341_WHITE);
  tft.setTextSize(2);
  tft.println(" Hoofd");
  tft.println(" menu");

  // 7 spaties per vak
  tft.setCursor(0, 2);
  tft.println("       Accu");
  tft.println("       status");

  tft.setCursor(0, 2);
  tft.println("              Color");
  tft.println("              picker");


  tft.setCursor(0, 2);
  tft.println("                     RF");
  tft.println("                     Con");
}


void drawButton(uint8_t keuze) {
    uint8_t x, y;
    String text1, text2;
    // Positie bepalen voor de knop aan de hand van de keuze oftewel mode
    x = keuze <= 2 ? 18 : 148;
    if (keuze == 0 || keuze == 3) {
        y = 45;
    }
    if (keuze == 1 || keuze == 4) {
        y = 110;
    }
    if (keuze == 2 || keuze == 5) {
        y = 175;
    }

    // Highlight de gekozen mode
    int color = keuze == mode ? ORANGE : BLACK;
    
    if (keuze == 0) {
        text1 = "  Drive";
        text2 = "  mode";
    }
    if (keuze == 1) {
        text1 = "  Linedance";
        text2 = "  mode";
    }
    if (keuze == 2) {
        text1 = "  Knaben";
        text2 = "  Wunder";
    }
    if (keuze == 3) {
        text1 = "             Dancing";
        text2 = "             mode";
    }
    if (keuze == 4) {
        text1 = "             Obstacle";
        text2 = "             course";
    }
    if (keuze == 5) {
        text1 = "             Transport";
        text2 = "             & rebuild";
    }
    
    tft.fillRoundRect(x, y, 120, 55, 15, color);
    tft.drawRoundRect(x, y, 120, 55, 15, ILI9341_WHITE);
    tft.setCursor(0, y + 13);
    tft.setTextColor(ILI9341_WHITE);
    tft.setTextSize(2);
    tft.println(text1);
    tft.println(text2);

}

void handleMenus() {
    //PC.println(state);
    switch (state) {
         // Hoofdmenu ------------------------------------------------------------------
         case 0:
            tft.fillRect(0, 40, 320, 200, GRAY);
            /*
            tft.setCursor(0, 220);
            tft.setTextColor(ILI9341_BLUE);
            tft.setTextSize(2);
            tft.print(" Programmmatijd: ");
            tft.print((millis() - timer) / 1000);
            tft.println("s");
            */
            
            //drawRoundRect(uint16_t x0, uint16_t y0, uint16_t w, uint16_t h, uint16_t radius, uint16_t color);
            /*
            drawButton(18, 45, mode == 0 ? ORANGE : BLACK, "  Drive", "  mode");
            drawButton(18, 110, mode == 1 ? ORANGE : BLACK, "  Linedance", "  mode");
            drawButton(18, 175, mode == 2 ? ORANGE : BLACK, "  Knaben", "  Wunder");
            drawButton(148, 45, mode == 3 ? ORANGE : BLACK, "             Dancing", "             mode");
            drawButton(148, 110, mode == 4 ? ORANGE : BLACK, "             Obstacle", "             course");
            drawButton(148, 175, mode == 5 ? ORANGE : BLACK, "             Transport", "             & rebuild");
            */
            for (int i = 0; i < 6; i++) drawButton(i);  // Doet hetzelfde als hierboven staat
            break;
        // Batterij status ------------------------------------------------------------
        case 1:
            tft.fillRect(0, 40, 320, 200, GRAY);
            tft.setCursor(0, 60);
            tft.setTextColor(ILI9341_RED);
            tft.setTextSize(2);
            tft.setTextWrap(false);
            tft.print(" Batterijspanning: ");
            tft.print(" ");
            tft.print(volt);
            tft.println("V");
            tft.println(" ");
            tft.print(" Belasting: ");
            tft.print(volt);
            tft.print("A");
            break;
        // Colorpicker   ------------------------------------------------------------
        case 2:
            //tft.fillRect(0, 40, 320, 200, GRAY);
            drawHSL();
            break;  
        // RF menu      ------------------------------------------------------------ 
        case 3:
            tft.fillRect(0, 40, 320, 200, GRAY);
            tft.setCursor(0, 60);
            tft.setTextColor(ILI9341_WHITE);
            tft.setTextSize(2);
            
            tft.print("RF received: ");
            WIRED ? tft.println(wired_string) : tft.println((char * ) rx_buf);
            
            tft.println("RF send: ");
            char * split;
            split = strtok(tx_buf, "&");    // Split string into tokens
            int i = 0;
            while (split != NULL) {
                i % 2 ? tft.println(split) : tft.print(split);    // Print op elke regel 2 waardes
                if (i % 2 == 0) tft.print("  ");                  // Ruimte tussen de waardes
                split = strtok(NULL, "&");                        // Ga naar volgende token
                i++;                                             
            }
            break;
    }
}


// -------------- Functies voor de colorpicker --------------
// Get 16-bit equivalent of 24-bit color
uint16_t RGB(uint8_t r, uint8_t g, uint8_t b) {
  return ((r / 8) << 11) | ((g / 4) << 5) | (b / 8);
}

float hue2rgb (float p, float q, float t) {
  if (t < 0) t += 1;
  if (t > 1) t -= 1;
  if (t < 1.0 / 6) return p + (q - p) * 6 * t;
  if (t < 1.0 / 2) return q;
  if (t < 2.0 / 3) return p + (q - p) * (2.0 / 3 - t) * 6;
  return p;
}

uint16_t hslToRgb(float h, float s, float l) {
  float r, g, b;

  if (s == 0) {
    r = g = b = l; // achromatic
  } else {
    float q = l < 0.5 ? l * (1 + s) : l + s - l * s;
    float p = 2 * l - q;
    r = hue2rgb(p, q, h + 1.0 / 3);
    g = hue2rgb(p, q, h);
    b = hue2rgb(p, q, h - 1.0 / 3);
  }
  return RGB(min(r * 255, 255), min(g * 255, 255), min(b * 255, 255));
}

void drawHSL() {
  tft.fillRect(0, 40, 320, 200, RGB(0, 0, 0));
  float hue;
  float saturation = 1;
  float lightness;
  unsigned int height = 240;
  unsigned int width = 320;
  for (unsigned int x = 0; x < width; x += 1) {
    hue = ((float)x) / width;
    for (unsigned int y = 40; y < height; y += 1) {
      lightness = ((float)y-40) / (height - 10); // top NUM_WHITE_PIXELS pixels represent white, full power
      
      tft.drawPixel(x, y, hslToRgb(hue, saturation, lightness));
    }
  }
}


