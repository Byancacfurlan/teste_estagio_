#2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.
#IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

palavra = input("Digite algo: ")
palavra = palavra.lower()

contagem = palavra.count("a")

if contagem>0:
    print(f"A letra 'a' apareceu {contagem} vezes no que foi escrito")
else:
    print("A letra 'a' não apareceu no que foi escrito")