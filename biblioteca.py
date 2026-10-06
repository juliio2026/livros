# ============================================================
# SISTEMA DE GERENCIAMENTO DE LIVROS
# Linguagem de Programação - Unidade 2 - Aula 4
# ============================================================

# Importação da biblioteca Matplotlib
import matplotlib.pyplot as plt


# ------------------------------------------------------------
# 1. CLASSE LIVRO
# ------------------------------------------------------------

class Livro:

    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

    def __str__(self):
        return (
            f"Título: {self.titulo} | "
            f"Autor: {self.autor} | "
            f"Gênero: {self.genero} | "
            f"Quantidade disponível: {self.quantidade}"
        )


# ------------------------------------------------------------
# 2. LISTA DE LIVROS
# ------------------------------------------------------------

livros = []


# ------------------------------------------------------------
# 3. CADASTRAR LIVRO
# ------------------------------------------------------------

def cadastrar_livro():

    print("\n===== CADASTRO DE LIVRO =====")

    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    genero = input("Digite o gênero do livro: ")

    while True:
        try:
            quantidade = int(input("Digite a quantidade disponível: "))

            if quantidade < 0:
                print("A quantidade não pode ser negativa.")
            else:
                break

        except ValueError:
            print("Digite uma quantidade válida.")

    novo_livro = Livro(titulo, autor, genero, quantidade)

    livros.append(novo_livro)

    print("\nLivro cadastrado com sucesso!")


# ------------------------------------------------------------
# 4. LISTAR LIVROS
# ------------------------------------------------------------

def listar_livros():

    print("\n===== LIVROS CADASTRADOS =====")

    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
        return

    for numero, livro in enumerate(livros, start=1):
        print(f"{numero}. {livro}")


# ------------------------------------------------------------
# 5. BUSCAR LIVRO PELO TÍTULO
# ------------------------------------------------------------

def buscar_livro():

    print("\n===== BUSCA DE LIVRO =====")

    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
        return

    titulo_busca = input("Digite o título do livro que deseja buscar: ")

    encontrado = False

    for livro in livros:

        if livro.titulo.lower() == titulo_busca.lower():

            print("\nLivro encontrado!")
            print(livro)

            encontrado = True
            break

    if not encontrado:
        print("\nLivro não encontrado.")


# ------------------------------------------------------------
# 6. GERAR GRÁFICO
# ------------------------------------------------------------

def gerar_grafico():

    print("\n===== GRÁFICO DE LIVROS POR GÊNERO =====")

    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
        return

    quantidade_por_genero = {}

    for livro in livros:

        genero = livro.genero

        if genero in quantidade_por_genero:
            quantidade_por_genero[genero] += livro.quantidade
        else:
            quantidade_por_genero[genero] = livro.quantidade

    generos = list(quantidade_por_genero.keys())
    quantidades = list(quantidade_por_genero.values())

    plt.figure(figsize=(10, 5))

    plt.bar(generos, quantidades)

    plt.title("Quantidade de Livros por Gênero")
    plt.xlabel("Gênero")
    plt.ylabel("Quantidade de Livros")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()


# ------------------------------------------------------------
# 7. MENU PRINCIPAL
# ------------------------------------------------------------

while True:

    print("\n")
    print("==========================================")
    print("     SISTEMA DE GERENCIAMENTO DE LIVROS")
    print("==========================================")
    print("1 - Cadastrar novo livro")
    print("2 - Listar todos os livros")
    print("3 - Buscar livro pelo título")
    print("4 - Gerar gráfico por gênero")
    print("5 - Sair")
    print("==========================================")

    opcao = input("Digite uma opção: ")

    if opcao == "1":

        cadastrar_livro()

    elif opcao == "2":

        listar_livros()

    elif opcao == "3":

        buscar_livro()

    elif opcao == "4":

        gerar_grafico()

    elif opcao == "5":

        print("\nSistema encerrado.")
        break

    else:

        print("\nOpção inválida. Escolha uma opção de 1 a 5.")
