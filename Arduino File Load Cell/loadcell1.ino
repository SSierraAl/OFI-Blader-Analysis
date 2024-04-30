#include <HX711.h>

#include "HX711.h"
# define dat 3
# define clk 2

HX711 scale;

void setup() {
Serial.begin(115200);
scale.begin(dat,clk);
}

long val = 0;
float count = 0;
float RDG = 0;
float LOAD = 0;

void loop() {
  count = count+1;
  //val = ((count-1) /count) *val + (1/count) * scale.read();
  val = 0.8 * val + 0.2* scale.read();
  Serial.println((val-(-183444)) / 446.60f);
 
}