# Resumos da aulas de Python 
print("=" * 60)
print("1. Lógica de Programação")
print("=" * 60)

# Traduzindo o pseudocódigo para Python
nota1 = 7.5
nota2 = 8.0
media = (nota1 + nota2) / 2

print(f"A média do aluno é: {media:.2f}")
if media >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")

print("\n" + "=" * 60)
print("2. Variáveis e tipos")
print("=" * 60)

# Declaração e atribuição de variáveis
nome_completo = "Alice da Silva" #string
idade = 30 #integer
altura = 1.76 #float
eh_estudante = True #boolean
print(f"Nome: {nome_completo}")
print(f"Idade: {idade} anos")
print(f"Altura: {altura} m")
print(f"É estudante? {eh_estudante}")
# Exemplo de nomes de variáveis inválidos
# 1nome = "inválido"
# nome-completo = "inválido"

x = 10 # tipo int
y1 = 10 # tipo int
y2 = "10" # tipo str
# Podemos somar tipos numéricos
print(x + y1)
# Mas não podemos somar numeros com string
# print (x + y2) # Isso geraria um erro

# Variável Gloal
saudacao = "Olá, mundo!"
nome = "Aluno"

# Função
def minha_funcao():

    # Variável local
    nome = "Ana"
    print(f"\nDentro da função: {nome}")
    print(f"\nAcessando a variavel global dentro da função: {saudacao}")

minha_funcao()

print(f"\nFora da função: {saudacao}")
print(f"Fora da função: {nome}")

# Função
def minha_funcao():

    # Variável local
    nome = "Ana"
    print(f"\nDentro da função: {nome}")
    print(f"\nAcessando a variavel global dentro da função: {saudacao}")

minha_funcao()

#Integer(inteiro)
numero_inteiro = 100
print(f"\nNúmero inteiro: {numero_inteiro} - Tipo: {type(numero_inteiro)}")
#Float(ponto flutuante)
numero_decimal = 19.99
print(f"Número decimal: {numero_decimal} - Tipo: {type(numero_decimal)}")
#String(Texto)
texto = "Olá, mundo!"
print(f"Texto: {texto} - Tipo: {type(texto)}")
#Boolean
verdadeiro = True
falso = False
print(f"Verdadeiro: {verdadeiro} - Tipo: {type(verdadeiro)}")
print(f"Falso: {falso} - Tipo: {type(falso)}")

# Operações atiméticas
# Definição de variáveis
a = 10
b = 3
# Usando operadores aritméticos
soma = a + b #adição
subtracao = a - b #subtração
multiplicacao = a * b #multiplicação
divisao = a / b #divisão(Resultado em float)
divisao_inteira = a // b #divisão inteira (descarta a parte decimal)
modulo = a % b #resto da divisão
potencia = a ** b #potência
print(f"\n{a} + {b} = {soma}")
print(f"{a} - {b} = {subtracao}")
print(f"{a} * {b} = {multiplicacao}")
print(f"{a} / {b} = {divisao}")
print(f"{a} // {b} = {divisao_inteira}")
print(f"{a} % {b} = {modulo}")
print(f"{a} ** {b} = {potencia}")
# As regras da matemática se aplicam normalmente
# Variáveis
a = 10
b = 0

# Tentativa de divisão por zero
try:
    resultado = a / b
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
# Cuidado isso não pode!
# 8 + 's'
# Mas isso pode!
'8' + 's'
'8s'

# Operadores de comparação
# Definição de variáveis
x = 5
y = 10
# Operador "maior que"
x > y 
# Operador "menor que"
x < y
# Operador "igual a"
x == y
# Operador "diferente de"
x != y
# Operador "maior ou igual a"
x >= 5
# Operador "menor ou igual a"
x <= y
print(f"\n{x} > {y}: {x > y}") # Maior que
print(f"{x} < {y}: {x < y}") # Menor que
print(f"{x} == {y}: {x == y}") # Igual a
print(f"{x} != {y}: {x != y}") # Diferente de
print(f"{x} >= 5: {x >= 5}")  # Maior ou igual a
print(f"{x} <= {y}: {x <= y}") # Menor ou igual a

# Operadores lógicos
# Definição de variáveis
tem_dinheiro = True
tem_tempo = False
# Operador "and" Ambos precisam ser verdadeiros
print(f"tem_dinheiro and tem_tempo: {tem_dinheiro and tem_tempo}")
# Operador "or" Pelo menos um precisa ser verdadeiro
print(f"tem_dinheiro or tem_tempo: {tem_dinheiro or tem_tempo}")
# Operador "not" Inverte o valor
print(f"not tem_dinheiro: {not tem_dinheiro}")

# Manipulação de strings
# Definição de uma string
frase = "Python é uma linguagem de programação poderosa."
# Concatenação
nome = "Maria"
saudacao = "Olá, " + nome + "!"
print(f"\nTamanho da frase: {len(saudacao)}")
# Maiúsculas ou minúsculas
print(f"Frase em maiúsculas: {frase.upper()}")
print(f"Frase em minúsculas: {frase.lower()}")
# Remover espaços em branco do inicio e do fim
frases_sem_espacos = frase.strip()
print(f"Frase sem espaços: '{frases_sem_espacos}'")
# Substituir o texto
print(f"Supstituindo 'divertido' por 'legal': {frase.replace('poderosa', 'legal')} .")
print(f"Frase sem espaços: '{frases_sem_espacos}'")
# Fatiamento (slicing) - Acessando partes da string
# O índice em python começa em 0
print(f"Primeiro caractere: {frases_sem_espacos[0]}")
print(f"A palavra 'Python': {frases_sem_espacos[9:15]}") # do índice 9 até o 14

# Estruturas de dados - listas
# Criando uma lista
frutas = ["maçã", "banana", "laranja", "uva"]
print(f"\nLista de frutas: {frutas}")
# Acessando um ítem pelo índice
print(f"Primeira fruta: {frutas[0]}")
print(f"Última fruta: {frutas[-1]}")
# Adicionando um item no final da lista
frutas.append("abacaxi")
print(f"Lista após adicionar abacaxi: {frutas}")
# Removendo um item da lista
frutas.remove("banana")
print(f"Lista após remover banana: {frutas}")
# Modificando um item da lista
frutas[1] = "kiwi"
print(f"Lista após modificar a segunda fruta: {frutas}")
# Podemos imprimir diretamente
print(frutas)
# Verificando o tamanho da lista
print(f"Tamanho da lista: {len(frutas)}")
# Deletando a lista 
del frutas
# Lista não pode mais ser acessada
# print(frutas)

# Estruturas de dados - Tuplas
# Criando uma tupla
coordenadas = (10.0, 20.5)
print(f"Tupla de coordenadas: {coordenadas}")
type(coordenadas)
# Acessando um item pelo índice
print(f"Coordenada X: {coordenadas[0]}")
print(f"Coordenada Y: {coordenadas[1]}")
# Tentativa de modificar um item da tupla (isso gerará um erro)
# coordenadas[0] = 15.0
# Tuplas são úteis para dados que não devem ser alterados, como meses do ano, coordenadas, etc.
dias_da_semana = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")
print(f"O primeiro dia da semana é: {dias_da_semana[0]}")

# Estruturas de dados - Dicionários
# Criando um dicionário de informações de um aluno
aluno = {
    "nome": "João",
    "idade": 20,
    "curso": "Engenharia de Software",
    "aluno_ativo": True
}
print(f"\nDicionário do aluno: {aluno}")
type(aluno)
# Acessando valores pelo nome da chave
print(f"Nome do aluno: {aluno['nome']}")
print(f"Curso: {aluno.get('curso')}") #.get() é uma alternativa para acessar valores
# Adicionando um novo par chave-valor
aluno["cidade"] = "São Paulo"
print(f"Dicionário após adicionar cidade:\n {aluno}")
# Modificando um valor existente
aluno["idade"] = 23
print(f"Idade atualizada: {aluno['idade']}")
# Removendo um par chave-valor
del aluno["aluno_ativo"]
print(f"Dicionário após remover aluno_ativo:\n {aluno}")

# Estruturad de dados - Conjuntos (Sets)
# Criando um conjunto de números
numeros = {1, 2, 3, 4, 5}
print(f"Conjunto de números (sem duplicados) : {numeros}")
type(numeros)
# Adicionando um número ao conjunto
numeros.add(6)
print(f"Conjunto após adicionar 6: {numeros}")
# Removendo um número do conjunto
numeros.remove(2)
print(f"Conjunto após remover 2: {numeros}")
# Operações com conjuntos
conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}
# União
uniao = conjunto_a.union(conjunto_b)
print(f"\nUnião de A e B: {uniao}")
# Interseção
intersecao = conjunto_a.intersection(conjunto_b)
print(f"Interseção de A e B: {intersecao}")

# Conversão entre tipos de dados
# Convertendo de string para integer
numero_em_texto = "123"
numero_inteiro = int(numero_em_texto)
print(f"String '{numero_em_texto}' convertida para inteiro: {numero_inteiro} - Tipo: {type(numero_inteiro)}")
# isso não pode ser feito
# teste = "Esta é uma string teste"
# teste_int =int(teste)
# print(teste_int)
# Convertendo de string para float
numero_em_texto_float = "45.67"
numero_float = float(numero_em_texto_float)
print(f"String '{numero_em_texto_float}' convertida para float: {numero_float} - Tipo: {type(numero_float)}")
# Convertendo de integer para string
idade = 25
idade_texto = str(idade)
print(f"Integer {idade} convertido para string: '{idade_texto}' - Tipo: {type(idade_texto)}")
# Convertendo entre estruturas de dados
lista_com_duplicatas = [1, 2, 2, 3, 4, 4, 5]
conjunto_unico = set(lista_com_duplicatas)
lista_sem_duplicatas = list(conjunto_unico)
print(f"\nLista original: {lista_com_duplicatas}")
print(f"Conjunto (sem duplicatas): {conjunto_unico}")
print(f"\nConvertida de volta para Lista: {lista_sem_duplicatas}\n")

# Saída de dados com print()
# Variáveis
nome = "Juliana"
idade = 25
cidade = "Rio de Janeiro"

#Usando f-strings para formatar a saída
print(f"Olá, meu nome é {nome}, tenho {idade} anos e moro em {cidade}.")
# Formatando números
preco = 49.95678
print(f"O preço do produto é: R$ {preco:.2f}") # Formata para 2 casas decimais

# Entrada de Dados com input()
# Pedindo o Nome do usuário (string)
nome_usuario = input("Digite seu nome: ")

# Pedindo a Idade do usuário (integer)
idade_usuario_str = input("Qual sua idade? ")
idade_usuario_str = int(idade_usuario_str)

from datetime import date

# Pega o ano correte na data definida no sistema operacional da sua máquina
ano_atual = date.today().year

# Processando os dados
ano_nascimento = ano_atual - idade_usuario_str
print(f"Olá, {nome_usuario}! Você nasceu em {ano_nascimento}.")
print(f"Você tem {idade_usuario_str} anos e nasceu aprocimadamente em {ano_nascimento}.")