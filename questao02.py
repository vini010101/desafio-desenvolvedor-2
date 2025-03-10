entrada = int(input("Digite um número para verificar se ele pertence à sequência de Fibonacci: "))

# Inicializa os dois primeiros números da sequência
a, b = 0, 1

while b < entrada:
    a, b = b, a + b  # Avança na sequência de Fibonacci

# Verifica se o número informado pertence à sequência
if entrada == b or entrada == 0:
    print(f"{entrada} pertence à sequência de Fibonacci.")
else:
    print(f"{entrada} NÃO pertence à sequência de Fibonacci.")
