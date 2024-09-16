from flask import render_template, request, redirect, url_for
from src.app import app
from src.models.productos import Productos
from src.models.categorias import Categorias
from flask_controller import FlaskController
from flask_restful import Api
from src.apis.productos_api import ProductosApi

class ProductosController(FlaskController):
    api = Api(app)
    
    api.add_resource(ProductosApi, '/api/productos')
    
    @app.route("/agregar_producto", methods=['GET','POST'])    
    def agregar_producto():
        if request.method == 'POST':
            descripcion = request.form.get('descripcion')
            valor_unitario = request.form.get('valor_unitario')
            cantidad_stock = request.form.get('cantidad_stock')
            unidad_medida = request.form.get('unidad_medida')
            categoria = request.form.get('categoria')
            productos = Productos(descripcion, unidad_medida, cantidad_stock, valor_unitario, categoria)
            Productos.agregar_producto(productos)
            return redirect(url_for('productos'))
        categorias = Categorias.obtener_categorias()
        return render_template("formulario_producto.html", categorias=categorias)

    @app.route("/productos")
    def productos():
        productos = Productos.obtener_productos()
        return render_template("productos.html", productos=productos)

    @app.route("/editar_producto/<int:id>", methods=['GET', 'POST'])
    def editar_producto(id):
        producto = Productos.obtener_producto_por_id(id)
        if request.method == 'POST':
            producto.descripcion = request.form.get('descripcion')
            producto.valor_unitario = request.form.get('valor_unitario')
            producto.cantidad_stock = request.form.get('cantidad_stock')
            producto.unidad_medida = request.form.get('unidad_medida')
            producto.categoria = request.form.get('categoria')
            Productos.editar_producto(producto)
            return redirect(url_for('productos'))
        categorias = Categorias.obtener_categorias()
        return render_template("editar_producto.html", producto=producto, categorias=categorias)

    @app.route("/eliminar_producto/<int:id>")
    def eliminar_producto(id):
        Productos.eliminar_producto(id)
        return redirect(url_for('productos'))
