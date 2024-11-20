void setup() {
  pinMode(LED_BUILTIN, OUTPUT);  // Initialize the built-in LED
  Serial.begin(9600);           // Start serial communication at 9600 baud
}

void loop() {
  if (Serial.available() > 0) {
    char blinkSignal = Serial.read();  // Read the incoming signal (as a char)

    // Check if the received signal is '1' or '0'
    if (blinkSignal == '1') {
      digitalWrite(LED_BUILTIN, HIGH);  // Turn the LED on
      Serial.println("LED ON");
    } else if (blinkSignal == '0') {
      digitalWrite(LED_BUILTIN, LOW);   // Turn the LED off
      Serial.println("LED OFF");
    }
  }
}
