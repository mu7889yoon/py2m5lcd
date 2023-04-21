#include <M5StickC.h>

void setup() {
  M5.begin();
  M5.Lcd.setRotation(3);
  M5.Lcd.setTextFont(2);
}

void loop() {
  if (Serial.available() > 0) {
    M5.Lcd.fillScreen(BLACK);
    M5.Lcd.setCursor(0, 0);
    String name = Serial.readStringUntil('\n');
    M5.Lcd.print(name+"\n");
  }
}
kimosugite naiteru