from time import sleep

print("---------------------------------")
print("|Calculo da Média Anual Escolar |")
print("---------------------------------")

aluno = str(input("Nome do aluno(a): "))
nota1 = float(input("Nota do Primeiro Trimestre: "))
nota2 = float(input("Nota do Primeiro Trimestre: "))
nota3 = float(input("Nota do Primeiro Trimestre: "))

media = float((nota1 + nota2 + nota3)/3)

if media <= 7:
    print("A média do aluno(a)", aluno, "é", media,)
    print("O aluno(a)", aluno, "reprovou")
else:
    print("A média do aluno(a)", aluno, "é", media)
    print("O aluno", aluno, "passou!!")

sleep(60)
