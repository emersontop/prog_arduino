from pyfirmata import Arduino, util  #biblioteca que se comunica com o arduino
import time

                                #void setup(){
Uno = Arduino('COM4')  #Crio o objeto uno
                                     # Serial.begin(9600);
print('Olá Mundo!')                  # Serial.println("Olá Mundo!");   
                                #}

tempo = 0

while True:                     # void loop(){

    tempo = tempo + 0.1

    Uno.digital[13].write(1)         # digitalWrite(13, HIGH);
    print('LED ligado',tempo)              # Serial.println("LED ligado");
    time.sleep(tempo)                    # delay(1000);

    Uno.digital[13].write(0)         # digitalWrite(13, LOW);
    print('LED desligado',tempo)           # Serial.println("LED desligado");
    time.sleep(tempo)                    # delay(1000);

                                #}