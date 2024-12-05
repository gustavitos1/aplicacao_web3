from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, scoped_session, declarative_base

engine = create_engine('sqlite:///base_vet_analise_9.sqlite3')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Cliente(Base):
    __tablename__ = 'clientes'

    id_cliente = Column(Integer, primary_key=True)
    CPF = Column(String(11), nullable=False, unique=True)
    Nome = Column(String(50), nullable=False, index=True)
    Telefone = Column(String(15), nullable=False, unique=True)


    def __repr__(self):
        return f'<Cliente: {self.Nome}, CPF: {self.CPF}, Telefone: {self.Telefone}>'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_Cliente(self):
        dados_Cliente = {
            "id_cliente": self.id_cliente,
            "Telefone": self.Telefone,
            "Nome": self.Nome,
            "CPF": self.CPF
        }
        return dados_Cliente


class Animal(Base):
    __tablename__ = 'animais'

    id_animal = Column(Integer, primary_key=True)
    nome_animal = Column(String(30), nullable=False, index=True)
    raca = Column(String(30))
    anoNasci = Column(Integer, nullable=False)
    idCliente = Column(Integer, ForeignKey("clientes.id_cliente"), nullable=False)
    cliente = relationship("Cliente")


    def __repr__(self):
        return f'<Animal: {self.nome_animal}, Raça: {self.raca}, Ano de Nascimento: {self.anoNasci}>'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_Animal(self):
        dados_Animal = {
            "id_animal": self.id_animal,
            "anoNasci": self.anoNasci,
            "nome_animal": self.nome_animal,
            "raca": self.raca,
            "idCliente": self.idCliente
        }
        return dados_Animal



class Veterinario(Base):
    __tablename__ = 'veterinarios'

    id_veterinario = Column(Integer, primary_key=True)
    crmv = Column(Integer, unique=True)
    nomeVet = Column(String(50), nullable=False, index=True)
    salario = Column(Float, nullable=False)


    def __repr__(self):
        return f'<Veterinário: {self.id_veterinario} {self.nomeVet} {self.salario} {self.crmv}>'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_veterinario(self):
        dados_veterinario = {
            "id_veterinario": self.id_veterinario,
            "crmv": self.crmv,
            "nomeVet": self.nomeVet,
            "salario": self.salario,
        }
        return dados_veterinario


class Consulta(Base):
    __tablename__ = 'consultas'

    id_consulta = Column(Integer, primary_key=True)
    data = Column(String, nullable=False)
    hora = Column(Integer, nullable=False)
    idAnimal = Column(Integer, ForeignKey("animais.id_animal"), nullable=False)
    idVeterinario = Column(Integer, ForeignKey('veterinarios.id_veterinario'), nullable=False)
    veterinarios = relationship('Veterinario')
    animais = relationship('Animal')

    def __repr__(self):
        return f'<Consulta: {self.data} {self.hora}>'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_consulta(self):
        dados_consulta = {
            "id_consulta": self.id_consulta,
            "data": self.data,
            "hora": self.hora,
            "idAnimal": self.idAnimal,
            "idVeterinario": self.idVeterinario
        }
        return dados_consulta


def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
