import sqlite3
con = sqlite3.connect('imc.db')
cur = con.cursor()
# criando a tabela
cur.execute ("""
CREATE TABLE  indice(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome varchar(100),
        peso varchar(4),
        altura varchar (5),
        total float 

);
""")

# solicitando os dados ao usuário
nome = input('Nome: ')
peso = input('Peso: ')
altura = input('altura: ')

total = 0
imc = (float(peso)) / float((altura)) * 2

if imc <= 17:
    total == float(imc)
elif (imc >= 17) and (imc <=18.49):
        total == float(imc)
elif (imc >= 18.50) and (imc <= 24.99):
        total == float (imc)
elif (imc >= 25) and (imc <= 29.99):
        total == float(imc)
elif (imc >= 30) and (imc <= 34.99):
        total == float(imc)
elif (imc >= 35) and (imc <= 39.99):
        total == float(imc)
else:
        total == float(imc)

# inserindo dados na tabela
cur.execute("""
INSERT INTO indice (nome, peso, altura, total)
VALUES (?,?,?,?)
""", (nome, peso, altura, total))

print('Conexao banco fechada.')
con.close()
