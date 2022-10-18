from pyfirmata import Arduino, util
import time

                                                #void setup(){
Uno = Arduino('COM4')                          #   Serial.begin(BAUD_RATE);
it = util.Iterator(Uno)                         #
it.start()                                      #
                                                #
valD11 = Uno.get_pin('d:11:i')                  #   pinMode(11,INPUT);
                                                #
                                                #}
                                                #
estadoBt1Ant = True                             # bool estadoBt1Ant = HIGH;
                                                #
contador = 0                                    # int contador = 0;
                                                #								
                                                #
print("Inicio do programa")
while True:                                     # void loop(){
    time.sleep(0.15)                            #   delay(150);
                                                #
    estadoBotao1 = valD11.read()                #   estadoBotao1 = digitalRead(11);
                                                #
    if estadoBotao1 == 0 and estadoBt1Ant :     #   if (!estadoBotao1 && estadoBt1Ant){
        contador += 1                           #       contador++;
        print(contador)                         #       Serial.println(contador);
                                                #   }
                                                #
    if contador >= 3 :                          #   if (contador >= 5){
        Uno.digital[6].write(1)                 #       digitalWrite(5, HIGH);
    else:                                       #   } else {
        Uno.digital[6].write(0)                 #       digitalWrite(5, LOW);
                                                #   }
    if contador >= 5 :                          #   if (contador >= 5){
        for x in range(10):
            Uno.digital[6].write(1)
            time.sleep(0.5)
            Uno.digital[6].write(0)                 #       digitalWrite(5, HIGH);
            time.sleep(0.5)
                                                #   }
                                                #
    estadoBt1Ant = estadoBotao1                 #   estadoBt1Ant = estadoBotao1;
                                                #}