class Servidor:
    def __init__(self, identificador: int, nome: str, ip: str, sistema: str):
        self.__identificador = identificador
        self.__nome = nome
        self.__ip = ip
        self.__sistema = sistema
        self.__status = "Desligado"

    @property
    def identificador(self):
        return self.__identificador

    @identificador.setter
    def identificador(self, identificador):
        self.__identificador = identificador

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def ip(self):
        return self.__ip

    @ip.setter
    def ip(self, ip):
        self.__ip = ip

    @property
    def sistema(self):
        return self.__sistema

    @sistema.setter
    def sistema(self, sistema):
        self.__sistema = sistema

    @property
    def status(self):
        return self.__status

    def iniciar(self):
        self.__status = "Ligado"

    def parar(self):
        self.__status = "Desligado"