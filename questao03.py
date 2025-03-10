import json

# Carregar os dados do do arquivo JSON
with open("dados.json", "r") as arquivo:
    dados = json.load(arquivo)

# Filtrar apenas os valores de faturamento maior que zero
valores_validos = [dia["valor"] for dia in dados if dia["valor"] > 0]

# Exibir opções
print("\nEscolha uma opção:")
print("1 - Maior valor de faturamento ocorrido em um dia do mês")
print("2 - Menor valor de faturamento ocorrido em um dia do mês")

# Entrada do usuário
entrada = int(input("\nDigite sua opção: "))

# Verificar a escolha e exibir o resultado correspondente, caso o usuario digite um valor invalido é exibido um erro.
if entrada == 1:
    print(f"\nMaior faturamento: {max(valores_validos)}")
elif entrada == 2:
    print(f"\nMenor faturamento: {min(valores_validos)}")
else:
    print("\nOpção inválida. Tente novamente.")
