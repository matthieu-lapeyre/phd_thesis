void setup() {
  // open serial communaction at 57600 baud
  Serial.begin(57600);
}

// the loop routine runs over and over again forever:
void loop() {

  // Read input voltage for the 5 FSR sensors
  int sen1 = analogRead(A3);
  int sen2 = analogRead(A4);
  int sen3 = analogRead(A5);
  int sen4 = analogRead(A6);
  int sen5 = analogRead(A7);

  // send data with the serial communication and use ',' as formater
  Serial.println(sen1 + ',' + sen2 + ',' + sen3 + ',' + sen4 + ',' + sen5);

  delay(20);        // delay in between reads for stability
}
