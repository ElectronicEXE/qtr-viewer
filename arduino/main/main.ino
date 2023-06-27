#include <QTRSensors.h>

QTRSensors qtr;

const uint8_t SensorCount = 8;
uint16_t sensorValues[SensorCount];

void setup()
{
  qtr.setTypeAnalog();
  qtr.setSensorPins((const uint8_t[]){A0, A1, A2, A3, A4, A5, A6, A7}, SensorCount);
  qtr.setEmitterPin(2);

  delay(500);
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH); 

  for (uint16_t i = 0; i < 150; i++)
  {
    qtr.calibrate();
  }
  digitalWrite(LED_BUILTIN, LOW); 

  Serial.begin(9600);
  
}

void loop()
{
  uint16_t position = qtr.readLineBlack(sensorValues);

  Serial.print(sensorValues[0]);
  Serial.print(",");
  Serial.print(sensorValues[1]);
  Serial.print(",");
  Serial.print(sensorValues[2]);
  Serial.print(",");
  Serial.print(sensorValues[3]);
  Serial.print(",");
  Serial.print(sensorValues[4]);
  Serial.print(",");
  Serial.print(sensorValues[5]);
  Serial.print(",");
  Serial.print(sensorValues[6]);
  Serial.print(",");
  Serial.print(sensorValues[7]);
  Serial.print(",");
  Serial.println(position);
}
