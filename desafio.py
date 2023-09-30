# Importando o sqlite
import sqlite3

#Criando o banco
banco = sqlite3.connect('cadastro.db')

cursor = banco.cursor()

#cursor.execute("CREATE TABLE pessoas (nome text, rg integer, idade integer)")


#Criando código do trabalho final do curso
#Sistema de cadastro de pessoas (nome completo, rg, cpf, idade)
#Funcionalidades (adcionar, excluir e listar pessoas)

#Variável que armazena
banco_cadastro = []

#Função que recebe os dadoos do usuário e insere no "banco de dados"
def cadastrar_pessoa():
  nome = input("Digite o nome completo da pessoa: ")
  rg = input("Digite o RG da pessoa: ")
  cpf = input("Digite o CPF da pessoa: ")
  idade = input("Digite a idade da pessoa: ")

#Passo os 4 dados para uma só variável (crio um vetor)
  cadastro_individual = [nome, rg, idade, cpf]
#Isiro este vetor no "banco de dados"
  banco_cadastro.append(cadastro_individual)

  print("Pessoa cadastrada com sucesso! ")

def remover_pessoa():
  nome = input("Digite o nome completo da pessoa que deseja remover: ")

#Pesquiso no "banco de dados" para ver se a pessoa está cadastrada
  for pessoa in banco_cadastro:
#Se a pessoa estiver no "banco de dados", eu removo
    if pessoa[0] == nome:
      banco_cadastro.remove(pessoa)
      print(f"{nome} foi removido(a) com sucesso! ")

#Senao, eu falo que não foi encontrada
    else:
      print(f"{nome} não encontrado(a)! ")

#Função listar pessoas
def listar_pessoas():
  print("\nLista de pessoas cadastradas\n")

# Percorro todo o "banco de dados" e imprimo as informações sobre cada pessoa
#0 -> nome
#1 -> rg
#2 -> cpf
#3 -> idade

  for pessoa in banco_cadastro:
    print(f"Nome: {pessoa[0]}")
    print(f"RG: {pessoa[1]}")
    print(f"CPF: {pessoa[2]}")
    print(f"Idade: {pessoa[3]}")
    print("-" * 20)

#A funcão recebe como parâmetro o nome que o usuário deseja editar
def editar_pessoa(nome):
 #Pesquiso no "banco de dados" para ver se a pessoa está cadastrada 
  for pessoa in banco_cadastro:
    if pessoa[0] == nome:

      #Pergunto para o usuário os novos dados
      nome_novo = input("Digite o nome completo da pessoa")
      rg_novo = input("Digite o rg da pessoa")
      cpf_novo = input("Digite o cpf da pessoa")
      idade_nova = input("Digite a idade da pessoa")
      
#Passo os 3 dados para uma só variável (crio um vetor)
      cadastro_editar = [nome_novo, rg_novo, idade_nova,cpf_novo]

#Acesso o vetor cadastro_editar para inserir as novas informações
      for i in range(len(cadastro_editar)):
        pessoa[i] = cadastro_editar[i]

      print("Usuário editado com sucesso! ")

    else:
      print("Pessoa não encontrda")      

while True:

  print("\nEscolha uma opção:\n")
  print("1. Cadastrar pessoa")
  print("2. Remover pessoa")
  print("3. Listar pessoas")
  print("4. Editar pessoa")
  print("5. Sair\n")

  escolha = int(input("Digite o número da opção desejada: "))

  if (escolha == 1):
    cadastrar_pessoa()

  elif (escolha == 2):
    remover_pessoa()

  elif (escolha == 3):
    listar_pessoas()

  elif (escolha == 4):
    nome_alterar = input("Digite o nome da pessoa que você deseja editar")
    editar_pessoa(nome_alterar)

  elif (escolha == 5):
    print("Saindo do programa...")
    break

  else:
    print("Opção inválida, tente outra opção!")
    
    banco.commit()
    
