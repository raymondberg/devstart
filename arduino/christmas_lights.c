//Purpose: This script uses a variety of pins in sequence to light
// a set of LEDs like Christmas lights. It can be set to alternate mode,
// where every other light is active at a time, or standard "unison" mode.


//Edit these initial values to change the behavior of the program
int lights[] = {1,2,3,4,5,6,8,13}; //The pin identifiers to power the lights
int total = 8;  // The total number of lights
bool alternate_mode = false; //Should the lights alternate? if not, blink together
bool on_blink = 100; //Time to wait between light on and light off (first half)
bool off_blink = 100; //Time to wait between light off and light on (second half)

void setup() {
  for(int i = 0; i <= total; i = i + 1)
  {
     pinMode(lights[i], OUTPUT);
  }
}

void loop() {
  int index = 100;

  for(int i = 0; i < total; i = i + 1)
  {
    if(alternate_mode){
      if( i % 2 == 0) {
        digitalWrite(lights[i], HIGH);
      } else {
        digitalWrite(lights[i], LOW);
      }
    } else {
      digitalWrite(lights[i], HIGH);
    }
   }

  delay(on_blink);

  for(int i = 0; i < total; i = i + 1)
  {
    if(alternate_mode){
      if( i % 2 == 0) {
        digitalWrite(lights[i], LOW);
      } else {
        digitalWrite(lights[i], HIGH);
      }
    } else {
      digitalWrite(lights[i], LOW);
    }
  }
  delay(off_blink);
}
