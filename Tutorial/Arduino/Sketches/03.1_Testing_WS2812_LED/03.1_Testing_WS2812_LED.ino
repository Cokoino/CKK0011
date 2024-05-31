/**********************************************************************
  Product     : Cokoino 4WD Car chassis kit
  Auther      : www.cokoino.com
  Modification: 2022/07/03
**********************************************************************/
#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
#include <avr/power.h> // Required for 16 MHz Adafruit Trinket
#endif    

#define LED_PIN 2
#define LED_COUNT 3
#define Led_delay 100
Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);

void setup() 
{
  #if defined(__AVR_ATtiny85__) && (F_CPU == 16000000)
    clock_prescale_set(clock_div_1);
  #endif
  // END of Trinket-specific code.
  strip.begin();           // INITIALIZE NeoPixel strip object (REQUIRED)
  strip.show();            // Turn OFF all pixels ASAP
  strip.setBrightness(50); // Set BRIGHTNESS to about 1/5 (max = 255)
  Serial.begin(9600);
}

void loop() 
{
  SW2812_Test();
}

void SW2812_Test()
{
  colorWipe(strip.Color(255,   0,    0), Led_delay); // Red
  colorWipe(strip.Color(  0, 255,    0), Led_delay); // Green
  colorWipe(strip.Color(  0,   0,  255), Led_delay); // Blue
  colorWipe(strip.Color(  255,255, 255), Led_delay); // While
  //rainbow(10);             // Flowing rainbow cycle along the whole strip
  //theaterChaseRainbow(50); // Rainbow-enhanced theaterChase variant
}

void colorWipe(uint32_t color, int wait) {
  for(int i=0; i<strip.numPixels(); i++) { // For each pixel in strip...
    strip.setPixelColor(i, color);         //  Set pixel's color (in RAM)
    strip.show();                          //  Update strip to match
    delay(wait);                           //  Pause for a moment
  }
}

void theaterChase(uint32_t color, int wait) 
{
  for(int a=0; a<10; a++) {  // Repeat 10 times...
    for(int b=0; b<3; b++) { //  'b' counts from 0 to 2...
      strip.clear();         //   Set all pixels in RAM to 0 (off)
      // 'c' counts up from 'b' to end of strip in steps of 3...
      for(int c=b; c<strip.numPixels(); c += 3) {
        strip.setPixelColor(c, color); // Set pixel 'c' to value 'color'
      }
      strip.show(); // Update strip with new contents
      delay(wait);  // Pause for a moment
    }
  }
}

void rainbow(int wait) 
{
  for(long firstPixelHue = 0; firstPixelHue < 5*65536; firstPixelHue += 256)
  {
    strip.rainbow(firstPixelHue);
    strip.show(); // Update strip with new contents
    delay(wait);  // Pause for a moment
  }
}

void theaterChaseRainbow(int wait) 
{
  int firstPixelHue = 0;     // First pixel starts at red (hue 0)
  for(int a=0; a<30; a++) {  // Repeat 30 times...
    for(int b=0; b<3; b++) { //  'b' counts from 0 to 2...
      strip.clear();         //   Set all pixels in RAM to 0 (off)
      for(int c=b; c<strip.numPixels(); c += 3)
      {
        int      hue   = firstPixelHue + c * 65536L / strip.numPixels();
        uint32_t color = strip.gamma32(strip.ColorHSV(hue)); // hue -> RGB
        strip.setPixelColor(c, color); // Set pixel 'c' to value 'color'
      }
      strip.show();                // Update strip with new contents
      delay(wait);                 // Pause for a moment
      firstPixelHue += 65536 / 90; // One cycle of color wheel over 90 frames
    }
  }
}
