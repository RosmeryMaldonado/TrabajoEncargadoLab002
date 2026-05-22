from src.usuario import Usuario

class TestUsuario:

    def setup_method(self):
        self.usuario = Usuario("Ana", 20)

    def test_es_mayor_edad(self):
        assert self.usuario.es_mayor_edad() is True