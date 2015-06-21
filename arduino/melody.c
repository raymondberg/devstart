//This plays a song at the click of a button
#include "melody.h"

//*************** BEGIN BERGBUTTON
int BERGBUTTON_STATUS = LOW;

bool _detect_button_click(int listen_pin){
  if (listen_pin != -1){
    pinMode(listen_pin, INPUT);
    while( true ) {
      int button_state = digitalRead(listen_pin);
      if (button_state != BERGBUTTON_STATUS){
        if( button_state == HIGH ){
          BERGBUTTON_STATUS = HIGH;
        } else {
          BERGBUTTON_STATUS = LOW;
          return true;
        }
      }
    }
  }
  return false;
}

bool bergbutton_listen_and_power(int listen_pin, int power_pin){
  pinMode(power_pin, OUTPUT);
  if (power_pin != -1){
    digitalWrite(power_pin, HIGH);
    bool result = _detect_button_click(listen_pin);
    digitalWrite(power_pin, LOW);
    return result;
  } else {
    return false;
  }
}

bool bergbutton_listen(int listen_pin){
  return _detect_button_click(listen_pin);
}
//*************** END BERGBUTTON

int beats_per_minute = 40;
int song_tone_pin = 8;
double melody[9][2] = {
  {NOTE_C4,DQUARTER},
  {NOTE_C4,DQUARTER},
  {NOTE_C4,DQUARTER},
  {NOTE_GS3,DQUARTER},
  {NOTE_DS4,DSIXTEENTH},
  {NOTE_C4,DQUARTER},
  {NOTE_GS3,DQUARTER},
  {NOTE_DS4,DSIXTEENTH},
  {NOTE_C4,DQUARTER},
};

void setup() {

}

double getSecondsPerBeat(int bpm)
{
  return 60000.0 / bpm;
}

int getDuration(double note){
   return (int)getSecondsPerBeat(beats_per_minute)/note;
}

void playNote(int tone_pin, double noteData[])
{
    int noteDuration = getDuration(noteData[1]);
    tone(tone_pin, noteData[0], noteDuration);
    int pauseBetweenNotes = noteDuration * 1.15;
    delay(pauseBetweenNotes);
    noTone(tone_pin);
}

void play_song(int tone_pin){
  for (int note_number = 0; note_number < 9; note_number++) {
    playNote(tone_pin, melody[note_number]);
  }
}
void loop() {
  pinMode(13, OUTPUT);
  if( bergbutton_listen_and_power(4,13)){
    play_song(song_tone_pin);
  } else {
    return;
  }
}
