#include <IRremote.h>

int IC_LED_IND = 2;
int RELE_PIN = 3;
int IR_RECV_PIN = 11;

IRrecv irrecv(IR_RECV_PIN);
decode_results results;

void setup()
{
  pinMode(IC_LED_IND, OUTPUT);
  pinMode(RELE_PIN, OUTPUT);
  pinMode(IR_RECV_PIN, INPUT);
  
  irrecv.enableIRIn();
  
  Serial.begin(9600);
  Serial.println("Running");
  Serial.flush();
}

void loop()
{

  if (irrecv.decode(&results)) {
    Serial.println(results.value, HEX); //dumps value to Serial ... comment for production
    Serial.flush();
    

    irrecv.resume(); // Receive the next value
  }
  delay(1000);
}
