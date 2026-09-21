from servidor import Servidor


servidor = Servidor(
    1,
    "servidor-web",
    "192.168.1.10",
    "Ubuntu"
)

print("Nome:", servidor.nome)
print("IP:", servidor.ip)
print("Sistema:", servidor.sistema)
print("Status:", servidor.status)

servidor.iniciar()

print("Status após iniciar:", servidor.status)

servidor.parar()

print("Status após parar:", servidor.status)