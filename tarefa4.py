#4) Descubra a lógica e complete o próximo elemento:
#a) 1, 3, 5, 7, ___
#b) 2, 4, 8, 16, 32, 64, ____
#c) 0, 1, 4, 9, 16, 25, 36, ____
#d) 4, 16, 36, 64, ____
#e) 1, 1, 2, 3, 5, 8, ____
#f) 2,10, 12, 16, 17, 18, 19, ____

sequenciaA = [1,3,5,7]
sequenciaA.append(sequenciaA[-1]+2)
print(f"O próximo elemento da sequência é {sequenciaA}")

sequenciaB = [2,4,8,16,32,64]
sequenciaB.append(sequenciaB[-1]*2)
print(f"O próximo elemento da sequência é {sequenciaB}")

sequenciaC = [0,1,4,9,16,25,36]
proximo = (len(sequenciaC))**2
sequenciaC.append(proximo)
print(f"O próximo elemento da sequência é {sequenciaC}")

sequenciaD = [0,4,16,36,64]
proximo = (len(sequenciaD)*2)**2
sequenciaD.append(proximo)
print(f"O próximo elemento da sequência é {sequenciaD}")

sequenciaE = [1,1,2,3,5,8]
sequenciaE.append(sequenciaE[-1]+sequenciaE[-2])
print(f"O próximo elemento da sequência é {sequenciaE}")

sequenciaF = [2,10,12,16,17,18,19]
sequenciaF.append(200)
print(f"O próximo elemento da sequência é {sequenciaF}")
