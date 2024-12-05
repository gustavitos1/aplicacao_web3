from models import Cliente, Animal, Veterinario, Consulta, db_session
from sqlalchemy.exc import SQLAlchemyError

# Funções para Cliente
def inserir_cliente():
    try:
        cliente = Cliente(
            CPF=input('CPF: '),
            Nome=input('Nome: '),
            Telefone=input('Telefone: ')
        )
        db_session.add(cliente)
        db_session.commit()
        print(f"Cliente {cliente.Nome} inserido com sucesso.")
    except SQLAlchemyError as e:
        db_session.rollback()
        print(f"Erro ao inserir cliente: {e}")

def consulta_clientes():
    try:
        clientes = db_session.query(Cliente).all()
        for cliente in clientes:
            print(cliente)
    except SQLAlchemyError as e:
        print(f"Erro ao consultar clientes: {e}")

def atualizar_cliente():
    cpf = input('CPF do cliente: ')
    try:
        cliente = db_session.query(Cliente).filter_by(CPF=cpf).first()
        if cliente:
            print(cliente)
            cliente.Nome = input('Novo Nome: ')
            cliente.telefone = input('Novo Telefone: ')
            db_session.commit()
            print("Cliente atualizado com sucesso.")
        else:
            print(f"Cliente com CPF {cpf} não encontrado.")
    except SQLAlchemyError as e:
        db_session.rollback()
        print(f"Erro ao atualizar cliente: {e}")

def deletar_cliente():
    cpf = input('CPF do cliente: ')
    try:
        cliente = db_session.query(Cliente).filter_by(CPF=cpf).first()
        if cliente:
            db_session.delete(cliente)
            db_session.commit()
            print(f"Cliente com CPF {cpf} deletado com sucesso.")
        else:
            print(f"Cliente com CPF {cpf} não encontrado.")
    except SQLAlchemyError as e:
        db_session.rollback()
        print(f"Erro ao deletar cliente: {e}")

# Funções para Animal
def inserir_animal():
    try:
        animal = Animal(
            nome_animal=input('Nome do Animal: '),
            raca=input('Raça: '),
            anoNasci=input('Data de Nascimento (YYYY-MM-DD): '),
            CPF=input('CPF do Dono: ')
        )
        db_session.add(animal)
        db_session.commit()
        print(f"Animal {animal.nome_animal} inserido com sucesso.")
    except SQLAlchemyError as e:
        db_session.rollback()
        print(f"Erro ao inserir animal: {e}")

def consulta_animal():
    try:
        animais = db_session.query(Animal).all()
        for animal in animais:
            print(animal)
    except SQLAlchemyError as e:
        print(f"Erro ao consultar animais: {e}")

def atualizar_animal():
    id_animal = int(input('ID do animal: '))
    try:
        animal = db_session.query(Animal).filter_by(id_animal=id_animal).first()
        if animal:
            animal.nome_animal = input('Novo Nome: ')
            animal.raca = input('Nova Raça: ')
            animal.anoNasci = input('Nova Data de Nascimento (YYYY-MM-DD): ')
            db_session.commit()
            print("Animal atualizado com sucesso.")
        else:
            print(f"Animal com ID {id_animal} não encontrado.")
    except SQLAlchemyError as e:
        db_session.rollback()
        print(f"Erro ao atualizar animal: {e}")

def deletar_animal():
    id_animal = int(input('ID do animal: '))
    try:
        animal = db_session.query(Animal).filter_by(id_animal=id_animal).first()
        if animal:
            db_session.delete(animal)
            db_session.commit()
            print(f"Animal com ID {id_animal} deletado com sucesso.")
        else:
            print(f"Animal com ID {id_animal} não encontrado.")
    except SQLAlchemyError as e:
        db_session.rollback()
        print(f"Erro ao deletar animal: {e}")

# Funções para Veterinário
def inserir_veterinario():
    try:
        veterinario = Veterinario(
            id_veterinario=input('ID do veterinário: '),
            crmv=input('CRMV: '),
            nomeVet=input('Nome: '),
            salario=float(input('Salário: ')),
            data_emissao=input('Data de Emissão do CRMV (YYYY-MM-DD): ')
        )
        db_session.add(veterinario)
        db_session.commit()
        print(f"Veterinário {veterinario.nomeVet} inserido com sucesso.")
    except SQLAlchemyError as e:
        db_session.rollback()
        print(f"Erro ao inserir veterinário: {e}")

def consulta_veterinarios():
    try:
        veterinarios = db_session.query(Veterinario).all()
        for vet in veterinarios:
            print(vet)
    except SQLAlchemyError as e:
        print(f"Erro ao consultar veterinários: {e}")

def atualizar_veterinario():
    crmv = input('CRMV do veterinário: ')
    try:
        vet = db_session.query(Veterinario).filter_by(crmv=crmv).first()
        if vet:
            vet.nomeVet = input('Novo Nome: ')
            vet.salario = float(input('Novo Salário: '))
            vet.data_emissao = input('Nova Data de Emissão (YYYY-MM-DD): ')
            db_session.commit()
            print("Veterinário atualizado com sucesso.")
        else:
            print(f"Veterinário com CRMV {crmv} não encontrado.")
    except SQLAlchemyError as e:
        db_session.rollback()
        print(f"Erro ao atualizar veterinário: {e}")

def deletar_veterinario():
    crmv = input('CRMV do veterinário: ')
    try:
        vet = db_session.query(Veterinario).filter_by(crmv=crmv).first()
        if vet:
            db_session.delete(vet)
            db_session.commit()
            print(f"Veterinário com CRMV {crmv} deletado com sucesso.")
        else:
            print(f"Veterinário com CRMV {crmv} não encontrado.")
    except SQLAlchemyError as e:
        db_session.rollback()
        print(f"Erro ao deletar veterinário: {e}")

# Funções para Consulta
def inserir_consulta():
    try:
        consulta = Consulta(
            data=input('Data da Consulta (YYYY-MM-DD): '),
            hora=input('Hora da Consulta (HH:MM): '),
            id_animal=int(input('ID do Animal: ')),
            crmv=input('CRMV do Veterinário: ')
        )
        db_session.add(consulta)
        db_session.commit()
        print(f"Consulta para o animal {consulta.id_animal} inserida com sucesso.")
    except SQLAlchemyError as e:
        db_session.rollback()
        print(f"Erro ao inserir consulta: {e}")

def consulta_consultas():
    try:
        consultas = db_session.query(Consulta).all()
        for consulta in consultas:
            print(consulta)
    except SQLAlchemyError as e:
        print(f"Erro ao consultar consultas: {e}")

def atualizar_consulta():
    id_consulta = int(input('ID da consulta: '))
    try:
        consulta = db_session.query(Consulta).filter_by(id=id_consulta).first()
        if consulta:
            consulta.data = input('Nova Data (YYYY-MM-DD): ')
            consulta.hora = input('Nova Hora (HH:MM): ')
            db_session.commit()
            print("Consulta atualizada com sucesso.")
        else:
            print(f"Consulta com ID {id_consulta} não encontrada.")
    except SQLAlchemyError as e:
        db_session.rollback()
        print(f"Erro ao atualizar consulta: {e}")

def deletar_consulta():
    id_consulta = int(input('ID da consulta: '))
    try:
        consulta = db_session.query(Consulta).filter_by(id=id_consulta).first()
        if consulta:
            db_session.delete(consulta)
            db_session.commit()
            print(f"Consulta com ID {id_consulta} deletada com sucesso.")
        else:
            print(f"Consulta com ID {id_consulta} não encontrada.")
    except SQLAlchemyError as e:
        db_session.rollback()
        print(f"Erro ao deletar consulta: {e}")

# Menu principal
if __name__ == '__main__':
    while True:
        escolha = int(input("\nMenu:\n1 - Cliente\n2 - Animal\n3 - Veterinário\n4 - Consulta\n5 - Sair\nEscolha: "))
        if escolha == 1:
            while True:
                escolha1 = int(input("\n1 - Inserir\n2 - Consultar\n3 - Atualizar\n4 - Deletar\n5 - Voltar\nEscolha: "))
                if escolha1 == 1:
                    inserir_cliente()
                elif escolha1 == 2:
                    consulta_clientes()
                elif escolha1 == 3:
                    atualizar_cliente()
                elif escolha1 == 4:
                    deletar_cliente()
                elif escolha1 == 5:
                    break
        elif escolha == 2:
            while True:
                escolha1 = int(input("\n1 - Inserir\n2 - Consultar\n3 - Atualizar\n4 - Deletar\n5 - Voltar\nEscolha: "))
                if escolha1 == 1:
                    inserir_animal()
                elif escolha1 == 2:
                    consulta_animal()
                elif escolha1 == 3:
                    atualizar_animal()
                elif escolha1 == 4:
                    deletar_animal()
                elif escolha1 == 5:
                    break
        elif escolha == 3:
            while True:
                escolha1 = int(input("\n1 - Inserir\n2 - Consultar\n3 - Atualizar\n4 - Deletar\n5 - Voltar\nEscolha: "))
                if escolha1 == 1:
                    inserir_veterinario()
                elif escolha1 == 2:
                    consulta_veterinarios()
                elif escolha1 == 3:
                    atualizar_veterinario()
                elif escolha1 == 4:
                    deletar_veterinario()
                elif escolha1 == 5:
                    break
        elif escolha == 4:
            while True:
                escolha1 = int(input("\n1 - Inserir\n2 - Consultar\n3 - Atualizar\n4 - Deletar\n5 - Voltar\nEscolha: "))
                if escolha1 == 1:
                    inserir_consulta()
                elif escolha1 == 2:
                    consulta_consultas()
                elif escolha1 == 3:
                    atualizar_consulta()
                elif escolha1 == 4:
                    deletar_consulta()
                elif escolha1 == 5:
                    break
        elif escolha == 5:
            break
        else:
            print("Escolha inválida.")

