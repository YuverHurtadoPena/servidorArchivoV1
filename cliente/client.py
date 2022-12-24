import zmq
import os

context = zmq.Context()


servidor = context.socket(zmq.REQ)
servidor.connect("tcp://localhost:5555")


bandera=True
def subirArchivo():
    archivo=input('ingresa la ruta del archivo a subir-->')
    nombre=input('como quieres guardarlo?-->')
    nombreUser=input('ingresa tu nombre-->')
    tuplaArchivo= os.path.splitext(archivo)
    nombreAsig=nombre+tuplaArchivo[1]
    with open(archivo, "rb")as f:
        contenidoArchivo= f.read()
        servidor.send_multipart([contenidoArchivo,opcion.encode("utf-8"),nombreAsig.encode("utf-8"),nombreUser.encode("utf-8")])
        m=servidor.recv_json()
        print(m)



def descargar():
    nombreAsig=input("ingrese el nombre del achivo a descargar-->")
    contenidoArchivoVa=""
    nombreUser=""
    servidor.send_multipart([contenidoArchivoVa.encode("utf-8"),opcion.encode("utf-8"),nombreAsig.encode("utf-8"),nombreUser.encode("utf-8")])
    data=servidor.recv_multipart()
    if data[0].decode("utf-8")!="Noexiste":
        with open(nombreAsig, "wb")as file:
            file.write(data[0])
    else:
        print("El archivo no existe.")

def listarArchivo():
    contenidoArchivoVa=""
    nombreAsig=""
    nombreUser=""
    servidor.send_multipart([contenidoArchivoVa.encode("utf-8"),opcion.encode("utf-8"),nombreAsig.encode("utf-8"),nombreUser.encode("utf-8")])
    info = servidor.recv_json()
    cont=0
    for i in info['infoArchivo']:
        cont=cont+1
        print('---------------------------------')
        print("numero archivo-->"+str(cont))
        print("Nombre Archivo-->"+i['nombreArchivo'])
        print("Nombre usuario-->"+i['nombreUsuario'])
        print('---------------------------------')
    


while bandera!=False:
    print('1.subir archivo')
    print('2.descargar archivo')
    print('3.listar archivo')
    print('4.salir')
    opcion=input('-->')

    if int(opcion)==1:
        subirArchivo()
    if int(opcion)==2:
        descargar()
    if int(opcion)==3:
        listarArchivo()
    if int(opcion)==4:
        print('gracias por usar el programa!!!')
        bandera=False
    
