//This script uses a distance sensor to generate different tones on a pieza

//Edit these initial values to change the behavior of the script
int baudRate = 9600;


int readingInterval= 200;
int sendPin = 4;    //i.e. the trig pin
int receivePin = 2; //i.e. the echo pin
int tonePin = 7; // the pin with the speaker


void setup(void) {
  Serial.begin(baudRate);
  pinMode(sendPin, OUTPUT);
  pinMode(receivePin, INPUT);
}

//###################### Section full of tools for handling the arrays

void pushLongArray(long arr[], int arrSize, long distance){
  int i = 0;
  while(i < arrSize - 1) {
    arr[i] = arr[i+1];
    i++;
  }
  arr[arrSize-1] = distance;
}

void sortLongArray(long array[], int arrSize){
  int i = 0;
  long swap;
  while( i < arrSize - 1) {
    if( array[i] > array[i+1] ){
      swap = array[i];
      array[i] = array[i+1];
      array[i+1] = swap;
      i = 0;
    } else {
      i++;
    }
  }
  i = 0;
  while (i < arrSize) {
     i++;
  }
}
long medianLongArray(long array[], int arrSize){
  int median = arrSize / 2;
  long sorted[arrSize];

  int index = 0;

  while (index < arrSize) {
    sorted[index] = array[index];
    index++;
  }
  sortLongArray(sorted, arrSize);

  return sorted[median];
}
//##############

long safeDistance(long distance) {
  pushLongArray(history,historyLength, distance);
  return medianLongArray(history,historyLength);
}

long getReading() {
  digitalWrite(sendPin, LOW);
  delayMicroseconds(2);

  digitalWrite(sendPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(sendPin, LOW);
  return pulseIn(receivePin, HIGH);
}

long distance, duration, last_distance;

void loop(void) {
  duration = getReading();
  distance = safeDistance((duration/2) / 29.1);
  if(distance != last_distance &&(distance >= 0 || distance <= 200)){
    //noTone(tonePin);
    tone(tonePin, distance*10+500, 50);
    // to distinguish the notes, set a minimum time between them.
    // the note's duration + 30% seems to work well:
    //delay(45);
    // stop the tone playing:
    last_distance = distance;
  }
}
