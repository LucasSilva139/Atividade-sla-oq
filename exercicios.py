# Exercício 1
def classificar_triangulo(lado1, lado2, lado3):
    if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
        return"Lados inválidos"
    if (lado1 + lado2 <= lado3 or
       lado1 + lado3 <= lado2 or
       lado2 + lado3 <= lado1):
       return"Esses lados não formam um triângulo"
    if lado1 == lado2 == lado3:
        return"Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return"Isósceles"
    else:
        return"Escaleno"
print(classificar_triangulo(5, 5, 5))

# Exercício 2
def exibir_tabuada(numero):
    for multiplicador in range(1, 11):
        print(f"{numero} x {multiplicador} = {numero * multiplicador}")
    exibir_tabuada(7)

# Exercício 3
def alunos_acima_da_media(notas):
    if not notas:
        return[]
    media = sum(notas.values()) / len(notas)
    return [nome for nome, nota in notas.items() if nota>media]
notas = {
    "Ana": 8,        
    "Bruno": 6,
    "Carla": 9
    }
print(alunos_acima_da_media(notas))
# Exercício 4
def quadrado_dos_pares(numeros):
    return [numero ** 2 for numero in numeros if numero % 2 == 0]
numeros = [1, 2, 3, 4, 5, 6]
print(quadrado_dos_pares(numeros))

# Exercício 5 
def dsa_calcula_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = 78,8
altura = 1,75

resultado = dsa_calcula_imc(peso, altura)
print(f"IMC: {resultado:.2f}")

# Exercício 6
def ordenar_pessoas(pessoas):
    return sorted(pessoas, key=lambda pessoa: pessoa[idade])
pessoas = [
    {"nome": "Lucas", "idade": 16},
    {"nome": "Anna", "idade": 12},
    {"nome": "Carlos", "idade": 18}
]
print(ordenar_pessoas(pessoas))

# Exercício 7
def contar_pares_impares(numeros):
    pares = sum(1 for numero in numeros if numero % 2 == 0)
    impares = sum(1 for numero in numeros if numero % 2 != 0)
    return {
        "pares": pares,
        "impares": impares
    }
print(contar_pares_impares([1, 2, 3, 4, 5, 6]))

# Exercício 8
def filtrar_emails(emails, dominio_desejado="gmail.com"):
    return [
        email for email in emails
        if email.endswith(dominio_desejado)
    ]

emails = [
    "lucas@gmail.com",
    "ana@gmail.com",
    "carlos@gmail.com"
]
print(filtrar_emails(emails))
print(filtrar_emails(emails, "hotmail.com"))

# Exercício 9
def transformar_frases(frases):
    return list(
        map(lambda frase: frase.upper() + " PYTHON", frases)
    )
frases = [
    "estou aprendendo programação",
    "python é interesante"
]
print(transformar_frases(frases))

# Exercício 10
import random
numero_secreto = random.randit(1, 20)

print("\nJogo de adivinhação!")
print("Tente adivinhar um número entre 1 e 20.")

for tentariva in range(1, 6):
    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    elif palpite > numero_secreto:
        print("O palpite foi muito alto.")
    else:
        print("O palpite foi muito baixo")
else: 
    print(f"Você perdeu! O número secreto era {numero_secreto}")