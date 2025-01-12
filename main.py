from peewee import IntegrityError
from database import db, Usuario, Anuncio

# Função para criar um usuário
def criar_usuario(nome, email, senha):
    # Verificar se o email já existe
    if Usuario.select().where(Usuario.email == email).exists():
        print(f"Erro: O email '{email}' já está em uso. Usuário não criado.")
        return None

    try:
        usuario = Usuario.create(nome=nome, email=email, senha=senha)
        print(f"Usuário {nome} criado com sucesso!")
        return usuario
    except Exception as e:
        print(f"Erro ao criar usuário: {e}")
        return None

# Função para criar um anúncio
def criar_anuncio(usuario, titulo, descricao, valor):
    if usuario is None:
        print(f"Erro: Anúncio '{titulo}' não pode ser criado sem um usuário válido.")
        return None

    try:
        anuncio = Anuncio.create(usuario=usuario, titulo=titulo, descricao=descricao, valor=valor)
        print(f"Anúncio '{titulo}' criado com sucesso!")
        return anuncio
    except Exception as e:
        print(f"Erro ao criar anúncio '{titulo}': {e}")
        return None

# Função para listar todos os anúncios
def listar_anuncios():
    anuncios = Anuncio.select()
    print("\n--- Lista de Anúncios ---")
    for anuncio in anuncios:
        print(f"Titulo: {anuncio.titulo}, Descrição: {anuncio.descricao}, Valor: {anuncio.valor:.2f}, Usuário: {anuncio.usuario.nome}")

# Função principal
def main():
    # Conectar ao banco de dados
    db.connect()

    # Criar tabelas, se necessário
    db.create_tables([Usuario, Anuncio], safe=True)

    # Criar usuários
    usuario1 = criar_usuario("João Silva", "joao@example.com", "senha123")
    usuario2 = criar_usuario("Maria Oliveira", "maria@example.com", "senha456")
    usuario3 = criar_usuario("Carlos Santos", "carlos@example.com", "senha789") 
    usuario4 = criar_usuario("Victor Lanes", "lanesvictor99@gmail.com", "s@W44n3sz99@")  # Novo usuário

    # Criar anúncios
    if usuario1:
        criar_anuncio(usuario1, "Venda de Carro", "Carro usado, modelo 2015", 30000.00)
    if usuario2:
        criar_anuncio(usuario2, "Notebook Usado", "Notebook em boas condições", 2500.00)
    if usuario3:
        criar_anuncio(usuario3, "Apartamento para Alugar", "Apartamento de 3 quartos no centro", 1500.00)
    if usuario4:
        criar_anuncio(usuario4, "Apartamento para Alugar", "Apartamento de 5 quartos no centro", 6000.00)

    # Listar anúncios
    listar_anuncios()

    # Fechar conexão com o banco
    db.close()

if __name__ == "__main__":
    main()
