automoveis = []

def cadastrar_automoveis():
    modelo = input("Digite o modelo desejado: ")
    cor = input("Digite a cor desejada: ")
    ano = input("Digite o ano desejado: ")

    automovel = [modelo, cor, ano]
    automoveis.append(automovel)

    print("Automovel cadastrado com sucesso")


def listar_automoveis():
    if len(automoveis) == 0:
        print("Não cadastrado!")
    else:
        print("\n===== Automoveis Cadastrados =====")
        for i, auto in enumerate(automoveis, start=1):
            modelo = auto[0]
            cor = auto[1]
            ano = auto[2]

            print(f"{i} - Modelo: {modelo} | Cor: {cor} | Ano: {ano}")
        print()


def buscar_automovel():
    automovel_busca = input("Digite a informação sobre o automovel: ")
    encontrado = False

    for auto in automoveis:
        modelo = auto[0]
        cor = auto[1]
        ano = auto[2]

        if modelo.lower() == automovel_busca.lower() or cor.lower() == automovel_busca.lower():
            print("\nAutomovel encontrado:")
            print(f"Modelo: {modelo} | Cor: {cor} | Ano: {ano}\n")
            encontrado = True

    if not encontrado:
        print("\nAutomovel não encontrado\n")


def excluir_automovel():
    if len(automoveis) == 0:
        print("\nNenhum automóvel cadastrado.\n")
        return

    modelo_excluir = input("Digite o modelo que deseja excluir: ")

    for auto in automoveis:
        if auto[0].lower() == modelo_excluir.lower():
            automoveis.remove(auto)
            print("\nAutomóvel removido com sucesso!\n")
            return

    print("\nAutomóvel não encontrado.\n")


def menu():
    opcao = ""

    while opcao != "5":
        print("===== SISTEMA DE CADASTRO DO AUTOMOVEL =====")
        print("1 - Cadastrar Automovel")
        print("2 - Listar Automovel")
        print("3 - Buscar Automovel")
        print("4 - Excluir")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_automoveis()
        elif opcao == "2":
            listar_automoveis()
        elif opcao == "3":
            buscar_automovel()
        elif opcao == "4":
            excluir_automovel()
        elif opcao == "5":
            print("\nEncerrando o sistema...")
        else:
            print("\nOpção inválida. Tente novamente.\n")


menu()