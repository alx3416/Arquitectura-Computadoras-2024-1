void setup() {
  pinMode(LED_BUILTIN, OUTPUT);  // Initialize the built-in LED
  Serial.begin(9600);           // Start serial communication at 9600 baud
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);  // Turn the LED on
  Serial.println("LED ON");         // Send a signal that the LED is on
  delay(1000);                      // Wait for 1 second
  digitalWrite(LED_BUILTIN, LOW);   // Turn the LED off
  Serial.println("LED OFF");        // Send a signal that the LED is off
  delay(1000);                      // Wait for 1 second
}