from flask import render_template, request, redirect, url_for
from src.app import app
from src.models.clientes import Clientes
from flask_controller import FlaskController

class ClientesController(FlaskController):
    @app.route("/clientes")
    def clientes():
        clientes = Clientes.obtener_clientes()
        return render_template('clientes.html', title="Lista de Clientes", clientes=clientes)
    
    @app.route("/clientes/<id>")
    def cliente_por_id(id):
        cliente = Clientes.obtener_cliente_por_id(id)
        return cliente

    @app.route("/form_cliente", methods=['GET', 'POST'])
    def form_cliente():
        if request.method == 'POST':
            nombre = request.form['nombre']
            tipo_identificacion = request.form['tipo_identificacion']
            numero_identificacion = request.form['numero_identificacion']
            direccion = request.form['direccion']
            telefono = request.form['telefono']
            
            cliente = Clientes(nombre=nombre, tipo_identificacion=tipo_identificacion,
                               numero_identificacion=numero_identificacion, direccion=direccion,
                               telefono=telefono)
            Clientes.agregar_cliente(cliente)
            return redirect(url_for('clientes'))
        
        return render_template('form_cliente.html', title="Formulario de Clientes")

    @app.route("/clientes/delete/<id>")
    def eliminar_cliente(id):
        cliente = Clientes.obtener_cliente_por_id(id)
        if cliente:
            Clientes.eliminar_cliente(cliente)
        return redirect(url_for('clientes'))

    @app.route("/clientes/edit/<id>", methods=['GET', 'POST'])
    def editar_cliente(id):
        cliente = Clientes.obtener_cliente_por_id(id)
        if request.method == 'POST':
            cliente.nombre = request.form['nombre']
            cliente.tipo_identificacion = request.form['tipo_identificacion']
            cliente.numero_identificacion = request.form['numero_identificacion']
            cliente.direccion = request.form['direccion']
            cliente.telefono = request.form['telefono']
            
            Clientes.actualizar_cliente(cliente)
            return redirect(url_for('clientes'))
        
        return render_template('form_cliente.html', title="Editar Cliente", cliente=cliente)
