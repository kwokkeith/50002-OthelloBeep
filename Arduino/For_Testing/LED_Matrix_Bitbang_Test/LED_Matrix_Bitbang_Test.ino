#include <FastLED.h>

FASTLED_USING_NAMESPACE

#define DATA_PIN    13
//#define CLK_PIN   4
#define LED_TYPE    WS2812B // Testing for this type of LED 
#define COLOR_ORDER GRB
#define NUM_LEDS    64 
CRGB leds[NUM_LEDS];
#define NOP __asm__ __volatile__ ("nop\n\t");


void setup() {

//  pinMode(leds, OUTPUT);
//  DDRB = B01111111;

  
  
  
}

void loop(){   

//  
//   digitalWrite(leds[0], HIGH); // sets the LED on
//   delayMicroseconds(1000); // waits for a second
//   digitalWrite(leds[0], LOW); // sets the LED off
//   delayMicroseconds(1000); // waits for a second

//    PORTB = B11111000;

    // HIGH Output Signal
    for (int k=0;k<8;k++) {
      for (int i=0; i<13; i++) {
        digitalWrite(DATA_PIN, HIGH);
        NOP;
        // High output: 0.8 + 0.45 us 
        }
  
      for (int j=0; j<7; j++) {
        digitalWrite(DATA_PIN, LOW);
        NOP;
      }
    }

    // LOW Output Signal
    for (int k=0;k<16;k++) {
      for (int i=0; i<6; i++) {
        digitalWrite(DATA_PIN, HIGH);
        NOP;
        }
  
      for (int j=0; j<13; j++) {
        digitalWrite(DATA_PIN, LOW);
        NOP;
      }
    }

    // Reset Output
    for (int k=0;k<800;k++) {
      digitalWrite(DATA_PIN, LOW);
      NOP;
    }
  
  }
