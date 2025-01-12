# 6. Contagem de Palavras em Textos
# Objetivo: Dado um texto, contar quantas vezes cada palavra única aparece nele.

# texto = "a raposa marrom salta sobre o cachorro preguiçoso marrom"
# palavras = texto.split() # Armazena todas as palavras em uma lista
# qtde_palavra = {}

# for a in palavras:
#     if a in qtde_palavra:
#         qtde_palavra[a] +=1
#     else:
#         qtde_palavra[a] = 1

# print (qtde_palavra)

# 7. Normalização de Dados
# Objetivo: Normalizar uma lista de números para que fiquem na escala de 0 a 1.
# numeros = [10, 20, 30, 40, 50]
# minimo = min(numeros)
# maximo = max(numeros)
# normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

# 20 - 10 / 50 - 10

# print(normalizados)

# 8. Filtragem de Dados Faltantes
# Objetivo: Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando.

# usuarios = [
#     {"nome": "Alice", "email": "alice@example.com"},
#     {"nome": "Bob", "email": ""},
#     {"nome": "Carol", "email": "carol@example.com"}
# ]

# usuarios_validos = [usuario for usuario in usuarios if not usuario["email"]] #Retorna a lista de chave valor(dicionario) somente dos usuarios que nao existe

# print(usuarios_validos)

# 9. Extração de Subconjuntos de Dados
# Objetivo: Dada uma lista de números, extrair apenas aqueles que são pares.

# numeros = range(1,11)

# pares = [a for a in numeros if a % 2 == 0]
# print(pares)

# 10. Agregação de Dados por Categoria
# Objetivo: Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

# vendas = [
#     {"categoria": "eletrônicos", "valor": 1200},
#     {"categoria": "livros", "valor": 200},
#     {"categoria": "eletrônicos", "valor": 800}
# ]
# total_categoria = {}

# for tot in vendas:
#     categoria = tot["categoria"]
#     valor = tot["valor"]

#     if categoria in total_categoria:
#         total_categoria[categoria] += valor
#     else:
#         total_categoria[categoria] = valor

# print (total_categoria)

# 11. Leitura de Dados até Flag
# Objetivo: Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

# entrada = ""

# while entrada.lower() != "sair":
#     entrada = input("Digite um valor: ")

# 12. Validação de Entrada
# Objetivo: Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

# numero = int(input("Digite um número no intervalo de 1 a 10: "))
# while numero < 1 or numero > 10:
#     print("Numero invalido, favor digitar o numero correto.") 
#     numero = int(input("Digite novamente: "))

# 13. Consumo de API Simulado
# Objetivo: Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

# pagina_atual = 1
# paginas_totais = 5  # Simulação, na prática, isso viria da API

# while pagina_atual <= paginas_totais:
#     print(f"Processando página {pagina_atual} de {paginas_totais}")
#     # Aqui iria o código para processar os dados da página
#     pagina_atual += 1

# print("Todas as páginas foram processadas.")

# 14. Tentativas de Conexão
# Objetivo: Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

# tentativas_maximas = 5
# tentativa = 1

# while tentativa <= tentativas_maximas:
#     print(f"tentando reconectar tentativa {tentativa} de {tentativas_maximas}")
#     if tentativa == tentativas_maximas:
#         print("Limite de tentativas atingindo, tente novamente.")
#     tentativa+=1

# while tentativa <= tentativas_maximas:
#     print(f"Tentativa {tentativa} de {tentativas_maximas}")
#     # Simulação de uma tentativa de conexão
#     # Aqui iria o código para tentar conectar
#     if True:  # Suponha que a conexão foi bem-sucedida
#         print("Conexão bem-sucedida!")
#         break
#     tentativa += 1
# else:
#     print("Falha ao conectar após várias tentativas.")

# 15. Processamento de Dados com Condição de Parada
# Objetivo: Processar itens de uma lista até encontrar um valor específico que indica a parada.

itens = [1, 2, 3, "parar", 4, 5]

# for a in itens:
#     print(a)
#     if a == "parar" :
#         print("palavra encontrada")
#         break
i=0

while i < len(itens):
    if itens[i]== "parar":
        print("palavra encontrada")
        break
    print(f"processando item {itens[i]}")
    i +=1