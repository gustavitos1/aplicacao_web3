from flask import Flask, render_template, url_for, request, redirect, flash
from models import Veterinario, Animal, Consulta, Cliente, db_session
from sqlalchemy import select

app = Flask(__name__)
app.config['SECRET_KEY'] = '<KEY>'


@app.route('/')
def inicio():
    return render_template('inicio.html')


@app.route('/cadastro_clientes')
def cadastro_clientes():
    return render_template('cadastro_clientes.html')


@app.route('/cadastro_animais')
def cadastro_animais():
    return render_template('cadastro_animais.html')


@app.route('/agendar_consultas')
def agendar_consultas():
    return render_template('agendar_consultas.html')


@app.route('/cadastro_veterinarios')
def cadastro_veterinarios():
    return render_template('cadastro_veterinarios.html')


@app.route('/relatorios')
def relatorios():
    return render_template('relatorios.html')


@app.route('/estoque')
def estoque():
    return render_template('estoque.html')


@app.route('/veterinarios', methods=['GET'])
def veterinarios():
    # Consulta os veterinários no banco de dados
    sql_veterinarios = select(Veterinario)

    lista_veterinarios = db_session.execute(sql_veterinarios).scalars().all()

    # Verifica a lista de veterinários
    print(lista_veterinarios)

    # Renderiza a página de veterinários passando a lista
    return render_template("veterinarios.html", lista_de_veterinarios=lista_veterinarios)


@app.route('/cadastro_veterinario', methods=['POST', 'GET'])
def cadastro_veterinario():
    if request.method == "POST":
        if not request.form["form_crmv"] or not request.form["form_nomeVet"] or not request.form["form_salario"]:
            flash(message="Preencher todos os campos", category="error")
        else:
            form_evento = Veterinario(
                crmv=request.form["form_crmv"],
                nomeVet=request.form["form_nomeVet"],
                salario=request.form["form_salario"]
            )
            db_session.add(form_evento)
            db_session.commit()
            flash(message="Veterinário cadastrado com sucesso!", category="success")
            return redirect(url_for('veterinarios'))
    return render_template('cadastro_veterinarios.html')

@app.route('/animais', methods=['GET'])
def animais():
    # Consulta os animais no banco de dados
    sql_animais = select(Animal)

    # Serializa a lista de animais
    lista_animais = db_session.execute(sql_animais).scalars().all()

    # Verifica a lista de animais
    print(lista_animais)

    # Renderiza a página de animais passando a lista
    return render_template("animais.html", lista_de_animais=lista_animais)

@app.route('/clientes', methods=['GET'])
def clientes():
    # Consulta os clientes no banco de dados
    sql_clientes = select(Cliente)

    # Serializa a lista de clientes
    lista_clientes = db_session.execute(sql_clientes).scalars().all()

    # Verifica a lista de clientes
    print(lista_clientes)

    # Renderiza a página de clientes passando a lista
    return render_template("clientes.html", lista_de_clientes=lista_clientes)

@app.route('/consultas', methods=['GET'])
def consultas():
    # Consulta as consultas no banco de dados
    sql_consultas = select(Consulta)

    # Serializa a lista de consultas
    lista_consultas = db_session.execute(sql_consultas).scalars().all()

    # Verifica a lista de consultas
    print(lista_consultas)

    # Renderiza a página de consultas passando a lista
    return render_template("consultas.html", lista_de_consultas=lista_consultas)

@app.route('/cadastro_cliente', methods=['POST', 'GET'])
def cadastro_cliente():
    if request.method == "POST":
        # Verifica se os campos obrigatórios estão preenchidos
        if not request.form["form_CPF"] or not request.form["form_nome"] or not request.form["form_Telefone"]:
            flash(message="Preencher todos os campos", category="error")
        else:
            form_cliente = Cliente(
                CPF=request.form["form_CPF"],
                Nome=request.form["form_nome"],
                Telefone=request.form["form_Telefone"]
            )
            db_session.add(form_cliente)
            db_session.commit()
            flash(message="Cliente cadastrado com sucesso!", category="success")
            return redirect(url_for('clientes'))
    return render_template('cadastro_clientes.html')

@app.route('/cadastro_animal', methods=['POST', 'GET'])
def cadastro_animal():
    if request.method == "POST":
        # Verifica se os campos obrigatórios estão preenchidos
        if not request.form["form_nome_animal"] or not request.form["form_raca"] or not request.form["form_data_nascimento"] or not request.form["form_CPF_dono"]:
            flash(message="Preencher todos os campos", category="error")
        else:
            form_animal = Animal(
                nome_animal=request.form["form_nome_animal"],
                raca=request.form["form_raca"],
                anoNasci=request.form["form_data_nascimento"],
                CPF=request.form["form_CPF_dono"]
            )
            db_session.add(form_animal)
            db_session.commit()
            flash(message="Animal cadastrado com sucesso!", category="success")
            return redirect(url_for('animais'))
    return render_template('cadastro_animais.html')

@app.route('/cadastro_consulta', methods=['POST', 'GET'])
def cadastro_consulta():
    if request.method == "POST":
        if not request.form["form_data"] or not request.form["form_hora"] or not request.form["form_id_animal"] or not request.form["form_crmv"]:
            flash(message="Preencher todos os campos", category="error")
        else:
            form_consulta = Consulta(
                data=request.form["form_data"],
                hora=request.form["form_hora"],
                id_animal=request.form["form_id_animal"],
                idVeterinario=request.form["form_idVeterinario"]
            )
            db_session.add(form_consulta)
            db_session.commit()
            flash(message="Consulta cadastrada com sucesso!", category="success")
            return redirect(url_for('consultas'))
    return render_template('agendar_consultas.html')


@app.route('/editar_veterinario/<int:id_veterinario>', methods=['GET', 'POST'])
def editar_veterinario(id_veterinario):
    veterinario = db_session.query(Veterinario).filter_by(id_veterinario=id_veterinario).first()

    if not veterinario:
        flash("Veterinário não encontrado.", category="error")
        return redirect(url_for('veterinarios'))

    if request.method == 'POST':
        veterinario.crmv = request.form['form_crmv']
        veterinario.nomeVet = request.form['form_nomeVet']
        veterinario.salario = request.form['form_salario']

        db_session.commit()
        flash("Veterinário atualizado com sucesso!", category="success")
        return redirect(url_for('veterinarios'))

    return render_template(
        'editar_veterinario.html',
        veterinario=veterinario
    )

@app.route('/editar_animal/<int:id_animal>', methods=['GET', 'POST'])
def editar_animal(id_animal):
    animal = db_session.query(Animal).filter_by(id_animal=id_animal).first()

    if not animal:
        flash("Animal não encontrado.", category="error")
        return redirect(url_for('animais'))

    if request.method == 'POST':
        animal.nome_animal = request.form['form_nome_animal']
        animal.raca = request.form['form_raca']
        animal.anoNasci = request.form['form_anoNasci']

        db_session.commit()
        flash("Animal atualizado com sucesso!", category="success")
        return redirect(url_for('animais'))

    return render_template(
        'editar_animal.html',
        animal=animal
    )


if __name__ == '__main__':
    app.run(debug=True)

