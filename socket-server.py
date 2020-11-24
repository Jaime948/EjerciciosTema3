import socket
import re

socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = "127.0.0.1"
port = 8001
socket_server.bind((ip,port))
socket_server.listen(15) 
a = r"[aeiouAEIOU]"
b = r"[a-zA-Z]{1,}\b"
c = r"[0-9]"
d = r"[A-Z]\w+"
e = r"[a-zA-Záéíóú]{1,}[^aeiouAEIOUáéíóú\s\W]\b"

print(f"\n\nServidor en ejecucion {ip}:{port}")

while True:
    conexion, address = socket_server.accept()
    print ("Conexión establecida")
    
    while True:
        
        message = conexion.recv(1024)
        message = message.decode()
        print(message)

        comparar = re.findall(a, message)
        cont = 0
        for cv in comparar:
            cont=cont+1
            print(cv)

        mensaje = f"Se encontraron {cont} vocales"
        conexion.send(mensaje.encode('utf-8'))

        comparar = re.findall(b, message)
        cont = 0
        for pl in comparar:
            cont=cont+1
            print(pl)
        
        mensaje = f"Se encontraron {cont} palabras"
        conexion.send(mensaje.encode('utf-8'))

        comparar = re.findall(c, message)
        cont = 0
        for nm in comparar:
            cont=cont+1
            print(nm)

        mensaje = f"Ingreso {cont} numeros"
        conexion.send(mensaje.encode('utf-8'))

        comparar = re.findall(d, message)
        cont = 0
        for pm in comparar:
            cont=cont+1
            print(pm)

        mensaje = f"Ingreso {cont} palabras que inician con mayuscula"
        conexion.send(mensaje.encode('utf-8'))
        
        comparar = re.findall(e, message)
        cont = 0
        for pv1 in comparar:
            cont=cont+1
            print(pv1)

        mensaje = f"Ingreso {cont} palabras que no finalizan con una vocal"
        conexion.send(mensaje.encode('utf-8'))
