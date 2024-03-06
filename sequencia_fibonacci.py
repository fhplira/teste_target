# Questão 2 - Sequencia Fibonacci

def sequencia_fibonacci():
    try:
        print("A sequencia de Fibonacci contém números positivos que iniciam no 0")
        valor = int(input("Insira um número para descobrir se ele pertence à sequência: "))
        if valor == 0:
            print(f"O número {valor} pertence à sequencia fibonacci")

        fibonacci = [0, 1]
        num = fibonacci[-1]
        while num < valor:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
            num = fibonacci[-1]

        if fibonacci[-1] == valor:
            print(f"O número {valor} pertence à sequencia fibonacci")
        else:
            print(f"O número {valor} não pertence à sequencia fibonacci")

    except ValueError:
        print("Erro de tipo, insira um número")
        sequencia_fibonacci()


sequencia_fibonacci()
