import random


letra = ['1','2','3','4','5','6','7','8','9','0','¥','$','&','!','?','@','€','a','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
         's','t','u','v','w','x','y','z',]
a = random.choice(letra)
b = random.choice(letra)
c = random.choice(letra)
d = random.choice(letra)
e = random.choice(letra)
crip = []
pin = [a,b,c,d,e]
encrip = []
text = str(input("▶ Digite o texto: "))
crt = len(text)
cont = 0

for x in text:
    crip.append(text[cont])
    cont +=1
for y in range(0,crt):
    encrip.append(random.choice(letra))
print('A criptografia de {} é: '.format(text))
for z in range(0,crt):
    print(encrip[z], end='')
cripto = (''.join(encrip))
pim = (''.join(pin))
print("\n\n✊ PIN: {}".format(pim))
pintest = input("Digite o PIN para liberar o decodificador: ")
if pintest == pim:
    desc = input("\n✋ Decodificador liberado. \nDescriptografe o código com o texto gerado: ")
else:
    while pim != pintest:
        print("PIN incorreto. O PIN será redefinido.")
        a = random.choice(letra)
        b = random.choice(letra)
        c = random.choice(letra)
        d = random.choice(letra)
        e = random.choice(letra)
        pin = [a,b,c,d,e]
        pim = (''.join(pin))
        print('\n✊ PIN:', pim)
        pintest = input("Digite o PIN para liberar o decodificador: ")
        if pintest == pim:
            desc = input("\n✋ Decodificador liberado. \nDescriptografe o código com o texto gerado: ")
if desc == cripto:
    print('\n✅ Código descriptografado. O texto é {}.'.format(text))
else:
    while desc != cripto:
        print("Errou ❗ Escreva a codificação certa!")
        desc = input("Descript: ")
        if desc == cripto:
            print('\n✅ Código descriptografado. O texto é {}.'.format(text))
