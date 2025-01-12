from peewee import *

# Banco de dados SQLite
db = SqliteDatabase('FreeLancers.db')

# Modelo base para reutilizar o banco
class BaseModel(Model):
    class Meta:
        database = db

# Modelo Usuario
class Usuario(BaseModel):
    nome = CharField()
    email = CharField(unique=True)
    senha = CharField()

# Modelo Anuncio
class Anuncio(BaseModel):
    usuario = ForeignKeyField(Usuario, backref='anuncios')  # Relaciona com Usuario
    titulo = CharField()
    descricao = TextField()
    valor = DecimalField()

# Criação das tabelas (se não existirem)
def inicializar_banco():
    with db:
        db.create_tables([Usuario, Anuncio], safe=True)

# Inicialização automática ao importar o módulo
if __name__ == "__main__":
    inicializar_banco()
