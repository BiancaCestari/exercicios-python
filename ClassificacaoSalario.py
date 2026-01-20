salario = float(input("Informe seu salário: "))

if salario <= 3000:
    print("Programador Júnior")
elif salario <= 6000:
    print("Programador Pleno")
elif salario <= 15000:
    print("Programador Sênior")
else:
    print("Gerente de Projetos")
