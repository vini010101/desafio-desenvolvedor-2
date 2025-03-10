# Entrada do usuário
texto = input("Digite uma string para inverter: ")

# Variável para armazenar a string invertida
string_invertida = ""

# Loop percorrendo a string de trás para frente
for i in range(len(texto) - 1, -1, -1):
    string_invertida += texto[i]

# Exibir o resultado
print("String invertida:", string_invertida)
