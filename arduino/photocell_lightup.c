//Purpose: Light up a set of lights based on readings from a photocell
//
//Edit these initial values to change the behavior of the program
int baudRate = 9600;
int photocellPin = 0;     // the cell and 10K pulldown are connected to a0
int readingInterval= 200;
int maximumPhotoReading = 950;

int lights[] = {2,3,5,7,8,10,12,13}; //The pin identifiers to power the lights
int totalLights = 8;  // The total number of lights

void setup(void) {
  Serial.begin(baudRate);
   for(int i = 0; i <= totalLights; i = i + 1)
   {
      pinMode(lights[i], OUTPUT);
   }
}

double localReadingMax;
void lightPhotoReading(int reading) {
  localReadingMax = (int)(( (reading * 1.0) / maximumPhotoReading) * totalLights);
  Serial.print(reading);
  Serial.print(" with max of ");
  Serial.print(maximumPhotoReading);
  Serial.print(" turns into ");
  Serial.println(localReadingMax);
  for(int i = 0; i < localReadingMax && i < totalLights; i = i + 1)
  {
     digitalWrite(lights[i], HIGH);
  }

  for(int i = localReadingMax; i < totalLights; i = i + 1)
  {
    digitalWrite(lights[i], LOW);
  }

}

int photocellReading;     // the analog reading from the analog resistor divider
void loop(void) {
  photocellReading = analogRead(photocellPin);
  //printPhotoReading(photocellReading);
  lightPhotoReading(photocellReading);
  delay(readingInterval);
}
