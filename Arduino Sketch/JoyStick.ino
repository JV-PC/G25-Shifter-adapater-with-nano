const int X_pin = A3, Y_pin = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int x = analogRead(X_pin);
  int y = analogRead(Y_pin);
  
  int buttonStates = 0;

  Serial.println(String(x) + "," + String(y) + "," + String(buttonStates));

  delay(40);
}
