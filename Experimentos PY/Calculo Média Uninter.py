apol1 = int(input("Nota primeira apol: "))
apol2 = int(input("Nota segunda apol: "))
apol3 = int(input("Nota terceira apol: "))
apol4 = int(input("Nota quarta apol: "))
apol5 = int(input("Nota quinta apol: "))
ap = int(input("Nota Atividade Pratica: "))
po = int(input("Nota prova objetiva: "))
pd = int(input("Nota prova prática: "))

n3 = ((apol1+apol2+apol3+apol4+apol5)/5)
n1 = po
n4 = ((ap * 0.40)+(pd * 0.60))

media = ((n1 * 0.30) + (n3 * 0.20) + (n4 * 0.50))

if(media < 70):
    print("Infelizmente você pegou exame. Sua nota é:",media)

else:
    print("Passou Direto!!! Sua nota é:", media)
