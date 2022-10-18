import serial

porta = "COM"
velocidade = 9600

conexao = serial.serial(porta, velocidade)

while True:
    opcao = input("a/A - LED VERDE ou b/B - LED AMARELO ou c/C - LED VERMELHO \n")

    if opcao == "a":
        conexao.write(b'a')
    if opcao == "b":
        conexao.write(b'b')
    if opcao == "c":
        conexao.write(b'c')
    if opcao == "A":
        conexao.write(b'A')
    if opcao == "B":
        conexao.write(b'B')
    if opcao == "C":
        conexao.write(b'C')

conexao.close()