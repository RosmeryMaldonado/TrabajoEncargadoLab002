import pytest

from src.inventario import Producto, Inventario


def test_creacion_producto():
    producto = Producto("Laptop", 3500, 10)

    assert producto.nombre == "Laptop"
    assert producto.precio == 3500
    assert producto.stock == 10


def test_vender_producto():
    producto = Producto("Mouse", 50, 5)

    producto.vender(2)

    assert producto.stock == 3


def test_reabastecer_producto():
    producto = Producto("Teclado", 100, 2)

    producto.reabastecer(5)

    assert producto.stock == 7


def test_actualizar_precio():
    producto = Producto("Monitor", 800, 4)

    producto.actualizar_precio(1000)

    assert producto.precio == 1000


def test_agregar_producto_inventario():
    inventario = Inventario()

    producto = Producto("Laptop", 3500, 10)

    inventario.agregar_producto(producto)

    assert len(inventario.productos) == 1


def test_buscar_producto_existente():
    inventario = Inventario()

    producto = Producto("Mouse", 50, 5)

    inventario.agregar_producto(producto)

    resultado = inventario.buscar_producto("Mouse")

    assert resultado is not None
    assert resultado.nombre == "Mouse"


def test_buscar_producto_inexistente():
    inventario = Inventario()

    resultado = inventario.buscar_producto("Tablet")

    assert resultado is None


# =========================
# PRUEBAS QUE FALLARÁN
# =========================

# Deberán corregir el sistema
# para que estas pruebas funcionen correctamente.


# def test_no_permitir_stock_negativo():
#     producto = Producto("Laptop", 3000, 5)

#     with pytest.raises(ValueError):
#         producto.vender(10)


# def test_no_permitir_precio_negativo():
#     producto = Producto("Mouse", 50, 5)

#     with pytest.raises(ValueError):
#         producto.actualizar_precio(-100)


# def test_no_permitir_reabastecimiento_negativo():
#     producto = Producto("Teclado", 100, 5)

#     with pytest.raises(ValueError):
#         producto.reabastecer(-5)


# def test_no_permitir_cantidad_negativa_venta():
#     producto = Producto("Monitor", 800, 5)

#     with pytest.raises(ValueError):
#         producto.vender(-1)


# def test_no_permitir_productos_duplicados():
#     inventario = Inventario()

#     producto1 = Producto("Laptop", 3000, 5)
#     producto2 = Producto("Laptop", 4000, 8)

#     inventario.agregar_producto(producto1)

#     with pytest.raises(ValueError):
#         inventario.agregar_producto(producto2)