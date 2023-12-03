//Ultrasonic sensor
#include <NewPing.h>  

#define TRIGGER_PIN  A1  // Arduino pin tied to trigger pin on the ultrasonic sensor.
#define ECHO_PIN     A0  // Arduino pin tied to echo pin on the ultrasonic sensor.
#define MAX_DISTANCE 11

NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE);

//LEDs
const int red = 3;
const int green = 2;

//Seven Segment Display
int a = 10;
int b = 11;
int c = 13;
int d = 9;
int e = 12;
int f = 7;
int g = 8 ;

void setup() {
//Ultrasonic
Serial.begin(9600);

//LEDs
pinMode(red, OUTPUT);
pinMode(green, OUTPUT);
digitalWrite(red, LOW);
digitalWrite(green, HIGH);

//Seven Segment Display
pinMode(a, OUTPUT);
pinMode(b, OUTPUT);
pinMode(c, OUTPUT);
pinMode(d, OUTPUT);
pinMode(e, OUTPUT);
pinMode(f, OUTPUT);
pinMode(g, OUTPUT);
}
int pins[7] = {a, b, c, d, e, f, g};

void displayNumber(int *number) {
  for (int i = 0; i < 7; i++) {
    digitalWrite(pins[i], number[i]);
  }
}

void distance(){
delay(50);                     // Wait 50ms between pings (about 20 pings/sec). 29ms should be the shortest delay between pings.
Serial.print("Ping: ");
Serial.print(sonar.ping_cm()); // Send ping, get distance in cm and print result (0 = outside set distance range)
Serial.println("cm"); 
}

void led_change(){
int numberCount = 2;

int numbers[numberCount][7] = {
  {1, 1, 1, 1, 1, 1, 0}, // 0
  {0, 1, 1, 0, 0, 0, 0}, // 1
};
  
if(sonar.ping_cm() < 10){
digitalWrite(red, HIGH);
digitalWrite(green, LOW);
displayNumber(numbers[0]);
}else{
 digitalWrite(red, LOW);
 digitalWrite(green, HIGH);
 displayNumber(numbers[1]);
}  
}

void loop() {
delay(50);                     // Wait 50ms between pings (about 20 pings/sec). 29ms should be the shortest delay between pings.
Serial.print("Ping: ");
Serial.print(sonar.ping_cm()); // Send ping, get distance in cm and print result (0 = outside set distance range)
Serial.println("cm"); 
delay(1000);
led_change();
}
