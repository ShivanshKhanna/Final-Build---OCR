//Micro servo
#include <Servo.h>
Servo myservo;
const int down = 80;
const int up = 170;

//LCD screen
#include <LiquidCrystal_I2C.h>
#include <Wire.h>;
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
//Micro-servo

Serial.begin(9600);
myservo.attach(3);
myservo.write(down);

//LCD screen
lcd.begin();
lcd.backlight();
}

void show_payment(){
//RFID does not permit exit
lcd.clear();
lcd.setCursor(0,0);
lcd.print("Amount Required");
lcd.setCursor(0,1);
lcd.print("$");
lcd.println(amount);
delay(1000);
myservo.write(down);
}

void payment(){
//RFID permits exit
lcd1.clear();
lcd1.setCursor(0,0);
lcd1.print("Amount Paid");
lcd1.setCursor(0,1);
lcd1.print("Drive Safe");
delay(1000);
myservo.write(up);
}   

  
void loop(){
  // If there is a serial message available
  if (Serial.available() > 0) {
    
    // Read it into our string
    String data = Serial.readStringUntil('\n');
    Serial.print("sent data");
    Serial.println(data);
     if(data == "payment"){
      payment();
    }else if (data == "No payment"){
     show_payment();
      }
  }
}
    

