from servidor import Servidor


class Gerenciador:
    def __init__(self):
        self.__servidores = []

    @property
    def servidores(self):
        return self.__servidores

    def adicionar_servidor(self, servidor: Servidor):
        if not isinstance(servidor, Servidor):
            raise TypeError("O objeto deve ser da classe Servidor.")

        if self.buscar_servidor(servidor.identificador):
            raise ValueError("Já existe um servidor com esse identificador.")

        self.__servidores.append(servidor)

    def buscar_servidor(self, identificador: int):
        for servidor in self.__servidores:
            if servidor.identificador == identificador:
                return servidor

        return None

    def remover_servidor(self, identificador: int):
        servidor = self.buscar_servidor(identificador)

        if servidor is None:
            raise ValueError("Servidor não encontrado.")

        self.__servidores.remove(servidor)

    def iniciar_servidor(self, identificador: int):
        servidor = self.buscar_servidor(identificador)

        if servidor is None:
            raise ValueError("Servidor não encontrado.")

        servidor.iniciar()

    def parar_servidor(self, identificador: int):
        servidor = self.buscar_servidor(identificador)

        if servidor is None:
            raise ValueError("Servidor não encontrado.")

        servidor.parar()