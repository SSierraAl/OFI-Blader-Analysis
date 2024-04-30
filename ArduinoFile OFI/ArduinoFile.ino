/*!
 * @file getData.ino
 * @brief acquisition of spectral data
 * @details Read the values of 10 optical channels of the AS7341 spectral sensor, the more light of a certain wavelength of the light source,
 * the greater the corresponding channel value.
 *
 * @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
 * @license     The MIT license (MIT)
 * @author [fengli](li.feng@dfrobot.com)
 * @version  V1.0
 * @date  2020-07-16
 * @url https://github.com/DFRobot/DFRobot_AS7341
 */
#include "DFRobot_AS7341.h"
/*!
 * @brief Construct the function
 * @param pWire IC bus pointer object and construction device, can both pass or not pass parameters, Wire in default.
 */
DFRobot_AS7341 as7341;

bool ledon = true;
bool ledoff = false;

const int numReadings  = 10;
float readings [numReadings];
int readIndex  = 0;
float total  = 0;
int lim=0;
String comand;

void setup(void) {
  // put your setup code here, to run once:
  //Serial.begin(115200);
  Serial.begin(115200);
  //Detect if IIC can communicate properly 
  while (as7341.begin() != 0) {
    Serial.println("IIC init failed, please check if the wire connection is correct");
    delay(100);
  }
  Wire.setClock(100000);//CLOCK del bus de I2C al maximo
  as7341.setAtime(8);//tamaño del arreglo
  as7341.setAstep(255);//step para calcular el tiempo de integracion
}

void loop(void) {
  //Lectura por serial de la intensidad

  if(Serial.available()>0){ //verificacion de posibilidad de lectura
    int intensity=Serial.parseInt(); //transformacion a entero
    if(Serial.read()=='\n'){ //Revisa si es una entrada valida diferente a vacio
      intensity=21; //Fija entrada valida fuera de rango
    }
    if(intensity>0 && intensity<=20){ // Verifica que los valores sean validos y restringidos
      as7341.enableLed(ledon);//Prender el led
      as7341.controlLed (intensity);//Nivel de corriente o intensidad
    }
    else if(intensity == 0) //verifica si es 0 para apagar el led
      as7341.enableLed(ledoff);//Apagar el led
  }
/*
  while(Serial.available()==0){} //verificacion de posibilidad de lectura
    int intensity=Serial.parseInt(); //transformacion a entero
    if(Serial.read()=='\n'){ //Revisa si es una entrada valida diferente a vacio
      intensity=21; //Fija entrada valida fuera de rango
    }
    if(intensity>0 && intensity<=20){ // Verifica que los valores sean validos y restringidos
      as7341.enableLed(ledon);//Prender el led
      as7341.controlLed (intensity);//Nivel de corriente o intensidad
    }
    else if(intensity == 0) //verifica si es 0 para apagar el led
      as7341.enableLed(ledoff);//Apagar el led
*/

  // put your main code here, to run repeatedly:
  DFRobot_AS7341::sModeOneData_t data1;
  DFRobot_AS7341::sModeTwoData_t data2;
  //Serial.println("--------------------");
  //tiempoInicio = millis(); // Guardar el tiempo de inicio
  as7341.startMeasure(as7341.eF1F4ClearNIR);
  //Read the value of sensor data channel 0~5, under eF1F4ClearNIR
  data1 = as7341.readSpectralDataOne();
  as7341.startMeasure(as7341.eF5F8ClearNIR);
  //Read the value of sensor data channel 0~5, under eF5F8ClearNIR
  data2 = as7341.readSpectralDataTwo();

  //Serial.print("F1(405-425nm)Purple:");
  Serial.println(data1.ADF1);

  //Serial.print("F2(435-455nm):Blue fonce:");
  Serial.println(data1.ADF2);

  //Serial.print("F3(470-490nm):Blue:");
  Serial.println(data1.ADF3);

  //Serial.print("F4(505-525nm):Cyan:");
  Serial.println(data1.ADF4);

  //Serial.print("F5(545-565nm):Green:");
  Serial.println(data2.ADF5);
  
  //Serial.print("F6(580-600nm)yellow:");
  Serial.println(data2.ADF6);
  
  //Serial.print("F7(620-640nm)orange:");
  Serial.println(data2.ADF7);

  //Serial.print("F8(670-690nm)RED:");
  Serial.println(data2.ADF8);
  //unsigned long tiempoActual = millis(); // Guardar el tiempo de fin
  //Serial.print("Time: ");
  //Serial.println(tiempoActual-tiempoInicio);

  //float purple_ratio=(float)data1.ADF1/(float)data2.ADF8;
  //Serial.println("Purple ratio:");
  //Serial.println(purple_ratio);
  //float hgbratio=7.90445*pow(0.37612, purple_ratio);
  //Serial.println("hgb ratio:");
  //Serial.println(hgbratio);
}
