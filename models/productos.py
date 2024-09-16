from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.models import session, Base

class Productos(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True)
    descripcion = Column(String(300), unique=True, nullable=False)
    unidad_medida = Column(String(3), unique=False, nullable=False)
    cantidad_stock = Column(Integer, unique=False, nullable=False)
    valor_unitario = Column(Float(10,8))
    categoria = Column(Integer, ForeignKey('categorias.id'), nullable=False)

    def __init__(self, descripcion, unidad_medida, cantidad_stock, valor_unitario, categoria):
        self.descripcion = descripcion
        self.unidad_medida = unidad_medida
        self.cantidad_stock = cantidad_stock
        self.valor_unitario = valor_unitario
        self.categoria = categoria

    @staticmethod
    def agregar_producto(producto):
        session.add(producto)
        session.commit()
        return producto

    @staticmethod
    def obtener_productos():
        return session.query(Productos).all()

    @staticmethod
    def obtener_producto_por_id(id):
        return session.query(Productos).filter(Productos.id == id).one_or_none()

    @staticmethod
    def editar_producto(producto):
        session.commit()

    @staticmethod
    def eliminar_producto(id):
        producto = session.query(Productos).filter(Productos.id == id).one_or_none()
        if producto:
            session.delete(producto)
            session.commit()
