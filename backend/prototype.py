import sqlite3
import re

def conectar_bd():
    # Função para conectar ao banco de dados
    conn = sqlite3.connect('livraria.db')
    return conn

def criar_tabelas(): 
    # Função para criar as tabelas 
    conn = conectar_bd() 
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS Cliente (
            Nome TEXT NOT NULL,
            CPF TEXT NOT NULL,
            Username TEXT PRIMARY KEY NOT NULL,
            Senha TEXT CHECK (LENGTH(Senha) >= 6)
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS Admin ( 
            Username TEXT PRIMARY KEY NOT NULL,
            Senha TEXT NOT NULL CHECK (LENGTH(Senha) >= 6)
        )
    ''')

    cur.execute(''' 
        CREATE TABLE IF NOT EXISTS Livro (
            Id_Seq INTEGER PRIMARY KEY,
            Titulo varchar NOT NULL, 
            Autor varchar NOT NULL, 
            Ano int NOT NULL, 
            Editora varchar NOT NULL, 
            Categoria varchar NOT NULL, 
            Estoque int NOT NULL, 
            Valor decimal (5,2) NOT NULL, 
            Promocao decimal (5,2) DEFAULT 0.00, 
            Valor_Final decimal (5,2) DEFAULT 0.00
        )
     ''')
    1
    cur.execute(''' 
        CREATE TABLE IF NOT EXISTS Transacao (
                Id_Seq INTEGER PRIMARY KEY, 
                Produto INTEGER REFERENCES Livro(Id_Seq), 
                Valor REAL CHECK (Valor <> 0), 
                Concluido BOOLEAN, 
                Cliente TEXT REFERENCES Cliente(Username)
        )
    ''')


    cur.execute('''
        SELECT * FROM Admin
        WHERE Username = 'admin'
    ''')

    admin_existente = cur.fetchone()

    if not admin_existente:
        # Inserir um admin predefinido para fins de exemplo
        cur.execute('''
            INSERT INTO Admin (Username, Senha)
            VALUES (?, ?)
        ''', ('admin', 'Admin123'))

        print("Admin adicionado com sucesso!")

    
    conn.commit()
    conn.close()

def cadastrar_clientes(): 
    # Função para cadastrar os clientes 
    conn = conectar_bd()
    cur = conn.cursor() 

    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")
    username = input("Digite um nome de usuário: ")
    
    while True:
        senha = input("Digite sua senha (mínimo 6 caracteres, 1 letra maiúscula, 1 número): ")
        
        # Verificar se a senha atende aos requisitos
        if len(senha) >= 6 and re.search("[A-Z]", senha) and re.search("[0-9]", senha):
            break
        else:
            print("A senha não atende aos requisitos. Tente novamente.")

    cur.execute(''' 
        INSERT INTO Cliente (Nome, CPF, Username, Senha)
        VALUES (?, ?, ?, ?)''', (nome, cpf, username, senha))
    
    conn.commit()

    print("Cadastro realizado com sucesso!")
    area_inicio()

    
    conn.close()

def login_cliente(): 
    # Função para FAZER LOGIN NÉ MANO AFF 
    conn = conectar_bd()
    cur = conn.cursor() 

    username = input("Digite seu nome de usuário: ")
    senha = input ("Digite sua senha: ")

    cur.execute(''' 
        SELECT * FROM Cliente 
        WHERE Username = ? AND Senha = ?''', (username, senha))
    
    cliente = cur.fetchone()

    if cliente: 
        print("Login bem-sucedido! Bem-vindo, {}.".format(cliente[0]))
        area_cliente(username)
    else: 
        print("Nome de usuário ou senha incorretos.")
        area_inicio()
    
    conn.close()

def login_admin(): 
    # Função para realizar login do Admin (Já predefinido no código)
    conn = conectar_bd()
    cur = conn.cursor()

    username = input("Digite o nome do usuário do Admin: ")
    senha = input ("Digite a senha do Admin: ")

    cur.execute(''' 
        SELECT * FROM Admin
        WHERE Username = ? AND Senha = ?''', (username, senha))

    admin = cur.fetchone()

    if admin: 
        print("Login de Admin bem-sucedido! Bem-vindo, {}.".format(admin[0]))
        area_admin()
    else: 
        print("Nome de usuário ou senha de Admin incorretas.")
        area_inicio()

def area_admin(): 
    while True: 
        print("\nOpções de Administrador: ")
        print("1 - Adicionar Livro")
        print("2 - Remover Livro")
        print("3 - Adicionar Promoção")
        print("4 - Listar Livros")
        print("5 - Listar Clientes")
        print("0 - Sair")

        escolha_admin = input("Escolha uma ação: ")
        
        if escolha_admin == '1': 
            adicionar_livros()
        elif escolha_admin == '2':
            excluir_livro()
        elif escolha_admin == '3': 
            adicionar_promocao()
        elif escolha_admin == '4': 
            listar_livros('admin')
        elif escolha_admin == '5': 
            listar_clientes()
        elif escolha_admin == '0': 
            print('Saindo da área de admin.')
            area_inicio()
        else: 
            print('Opção Inválida.')

def area_inicio(): 
    print('Bem-vindo à Livraria "Leia Mais"! ')
    print('1.Admin')
    print('2.Cliente')

    escolha = input("Escolha uma opção (1 ou 2): ")

    if escolha == '1': 
        login_admin()
    elif escolha == '2': 
        print('1.Login')
        print('2.Cadastrar')

        opcao_cliente = input("Escolha uma opção (1 ou 2): ")

        if opcao_cliente == '1': 
            login_cliente()
        elif opcao_cliente == '2': 
            cadastrar_clientes() 
        else: 
            print('Opção Inválida.')
            area_inicio() 
    else: 
        print('Opção Inválida.')  
        area_inicio()         

def area_cliente(username):
    carrinho = []
    while True: 
        print("\nOpções de Cliente: ")
        print("1 - Listar Livros")
        print("2 - Comprar Livros")
        print("0 - Sair")

        ec = input("Selecione uma opção: ")

        if ec == '1': 
            listar_livros(username)
        elif ec == '2': 
            comprar_livro(username, carrinho)

        elif ec == '0': 
            print('Saindo da área de cliente.')
            area_inicio()
        else: 
            print("Opção inválida.")
    
def listar_livros(username):
    conn = conectar_bd()
    cur = conn.cursor()

    cur.execute('''
        SELECT * FROM Livro
     ''')

    livros = cur.fetchall()

    if not livros:
        print("Nenhum livro foi encontrado.")
    else:
        print("\nLista de Livros:")
        for livro in livros:
            # Ajuste para imprimir os detalhes do livro de forma mais legível
            print(f"Título: {livro[1]}, Autor: {livro[2]}, Ano: {livro[3]}, Editora: {livro[4]}, Gênero: {livro[5]}, Valor: {livro[9]:.2f}")

    if username == 'admin':
        area_admin()
    else:
        area_cliente(username)

    conn.close()

def adicionar_livros(): 
    conn = conectar_bd()
    cur = conn.cursor() 

    id = input("Defina o ID: ")
    titulo = input("Título do livro: ")
    autor = input("Autor do livro: ")
    ano = input("Ano de lançamento do livro: ")
    editora = input("Editora do livro: ")
    genero = input("Gênero do livro: ")
    estoque = input("Unidades em estoque do livro: ")
    valor = float(input("Valor do livro: "))
    promocao = float(input("Promoção atual: "))
    valor_final = valor - (valor * promocao/100.0)


    cur.execute(''' 
        INSERT INTO Livro (Id_Seq, Titulo, Autor, Ano, Editora, Categoria, Estoque, Valor, Promocao, Valor_Final) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (id, titulo, autor, ano, editora, genero, estoque, valor, promocao, valor_final))

    print(f'Livro {titulo} adicionado com sucesso!')

    conn.commit()
    conn.close()

def comprar_livro(username, carrinho):
    conn = conectar_bd()
    cur = conn.cursor()

    cur.execute('''
        SELECT Id_Seq, Titulo, Autor, Valor_Final FROM Livro
    ''')

    livros_disponiveis = cur.fetchall()

    if not livros_disponiveis:
        print("Desculpe, nenhum livro disponível para compra no momento.")
        return

    print("\nLista de Livros Disponíveis:")
    for livro in livros_disponiveis:
        print("ID: {}, Título: {}, Autor: {}, Valor: R${}".format(livro[0], livro[1], livro[2], livro[3]))

    id_livro = int(input("Digite o ID do livro que deseja comprar (0 para sair): "))

    if id_livro == 0:
        area_cliente(username)
        return

    livro_existente = False
    for livro in livros_disponiveis:
        if livro[0] == id_livro:
            livro_existente = True
            break

    if not livro_existente:
        print("ID do livro inválido. Tente novamente.")
        return

    carrinho.append(id_livro)
    print("Livro adicionado ao carrinho.")

    total_valor = 0
    for livro_id in carrinho:
        cur.execute('SELECT Valor FROM Livro WHERE Id_Seq = ?', (livro_id,))
        livro_valor = cur.fetchone()
        if livro_valor:
            total_valor += livro_valor[0]

    

    ecc = input("Deseja concluir a sua compra agora? \n1 - Ir para pagamento. \n2 - Continuar comprando.")
    if ecc == '1':
        concluir_compra(carrinho, total_valor)  # Adicione o carrinho como argumento
    elif ecc == '2':
        area_cliente(username)
    else:
        print("Opção inválida")

def excluir_livro():
    conn = conectar_bd()
    cur = conn.cursor()

    # Listar todos os livros disponíveis
    cur.execute('SELECT Id_Seq, Titulo FROM Livro')
    livros_disponiveis = cur.fetchall()

    if not livros_disponiveis:
        print("Desculpe, não há livros disponíveis para exclusão.")
        return

    print("\nLista de Livros Disponíveis para Exclusão:")
    for livro in livros_disponiveis:
        print("ID: {}, Título: {}".format(livro[0], livro[1]))

    id_livro_exclusao = int(input("Digite o ID do livro que deseja excluir (0 para sair): "))

    if id_livro_exclusao == 0:
        return  # Sair da função se o ID for 0

    # Verificar se o livro existe
    cur.execute('SELECT * FROM Livro WHERE Id_Seq = ?', (id_livro_exclusao,))
    livro_para_excluir = cur.fetchone()

    if livro_para_excluir:
        # Excluir o livro
        cur.execute('DELETE FROM Livro WHERE Id_Seq = ?', (id_livro_exclusao,))
        print("Livro excluído com sucesso.")
    else:
        print("ID do livro inválido. Nenhum livro excluído.")

    conn.commit()
    conn.close()

def concluir_compra(carrinho, total_valor): 

    conn = conectar_bd() 
    cur = conn.cursor() 

    cur.execute(''' 
        INSERT INTO Transacao (Produto, Valor, Concluido, Cliente)
        VALUES (?, ?, ?, ?)''', (', '.join(map(str,carrinho)), total_valor, True, "Cliente"))
    
    for livro_id in carrinho:
        cur.execute('UPDATE Livro SET Estoque = Estoque - 1 WHERE Id_Seq = ?', (livro_id,))
    
    conn.commit()
    conn.close()

    print("\nCompra Concluída!")
    print("Total a Pagar: R${}".format(total_valor))

    # Opções para a forma de pagamento
    print("\nFormas de Pagamento:")
    print("1. Cartão de Crédito")
    print("2. Cartão de Débito")
    print("3. Pix")
    print("4. Boleto")
    print("5. Paypal")

    forma_pagamento = input("Escolha uma forma de pagamento: ")

    if forma_pagamento in ['1', '2', '3', '4', '5']:
        print("Transação concluída! Obrigado por comprar na Leia-Mais.")
    else:
        print("Forma de pagamento inválida. Transação cancelada.")  


def listar_clientes(): 
  conn = conectar_bd() 
  cur = conn.cursor() 

  cur.execute(''' SELECT Username, Senha FROM Cliente''')

  clients = cur.fetchall() 

  if not clients: 
    print("Nenhum cliente foi registrado ainda.")
    area_admin() 
  else: 
    print("Lista de Clientes (Username, Senha)")
    for client in clients: 
      print(f'{client}')
    
  area_admin()
  

def adicionar_promocao():
    conn = conectar_bd()
    cur = conn.cursor()

    print("\nEscolha o critério para adicionar promoção:")
    print("1. Por ID")
    print("2. Por Autor")
    print("3. Por Ano")
    print("4. Por Categoria")

    escolha_criterio = input("Digite o número correspondente ao critério desejado (0 para sair): ")

    if escolha_criterio == '0':
        return  # Sair da função se escolher 0

    if escolha_criterio not in ['1', '2', '3', '4']:
        print("Opção inválida. Tente novamente.")
        return

    if escolha_criterio == '1':
        id_livro = int(input("Digite o ID do livro para adicionar promoção: "))
        percentual_promocao = float(input("Digite o percentual de promoção (ex: 10 para 10%): "))
        cur.execute('SELECT Valor FROM Livro WHERE Id_Seq = ?', (id_livro,))
        valor_atual = cur.fetchone()[0]
        novo_valor = valor_atual - (valor_atual * percentual_promocao / 100.0)
        cur.execute('UPDATE Livro SET Valor_Final = ? WHERE Id_Seq = ?', (novo_valor, id_livro))
    else:
        # Selecionar critério (Autor, Ano ou Categoria)
        criterio = input(f"Digite o {['Autor', 'Ano', 'Categoria'][int(escolha_criterio) - 2]} para adicionar promoção: ")
        percentual_promocao = float(input("Digite o percentual de promoção (ex: 10 para 10%): "))

        # Atualizar valor para livros com base no critério
        cur.execute(f'SELECT Id_Seq, Valor FROM Livro WHERE {["Autor", "Ano", "Categoria"][int(escolha_criterio) - 2]} = ?', (criterio,))
        livros = cur.fetchall()
        
        for livro in livros:
            valor_atual = livro[1]
            novo_valor = valor_atual - (valor_atual * percentual_promocao / 100.0)
            cur.execute('UPDATE Livro SET Valor_Final = ? WHERE Id_Seq = ?', (novo_valor, livro[0]))

    print("Promoção adicionada com sucesso.")
    conn.commit()
    conn.close()



def main(): 
    criar_tabelas()
    area_inicio()


if __name__ == "__main__":
    main()
