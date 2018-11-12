void setup() {
  Serial.begin(9600,SERIAL_8O2);   
}

void loop() {
 test_write();
}

void test_write() {
    Serial.write("Cam-Fisica\n");
    delay(10);
}

void test_receive() {
}
