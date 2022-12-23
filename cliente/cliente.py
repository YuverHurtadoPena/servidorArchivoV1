import zmq
import os
context = zmq.Context()
servidor=context.socket(zmq.REQ)
servidor.connect('tcp://localhost:5550')
bandera=True

def subirArchivo():
    archivo=input('Ingresa ruta del archivo a subir-->')
    nombre=input('como quieres guardarlo?-->')
    tuplaArchivo = os.path.splitext(archivo)
    file_extension = tuplaArchivo[1]
    nombreAsig=nombre+file_extension
    with open(archivo, "rb") as f:
        contenidoArchivo=f.read()
        servidor.send_multipart([contenidoArchivo,opcion.encode("utf-8"),nombreAsig.encode("utf-8")])
        x=servidor.recv()
        print("-----------------------")
        print("Tu archivo se envio con exito")
        print("Este es el nombre asignado: ",nombreAsig)
        print("-----------------------")

def descargarArchivo():
     nombreAsig=input('Ingresa nombre del archivo->')
     contenidoArchivoVa=""
     servidor.send_multipart([contenidoArchivoVa.encode("utf-8"),opcion.encode("utf-8"),nombreAsig.encode("utf-8")])
     data=servidor.recv_multipart()
     with open(nombreAsig, "wb") as f:
                f.write(data)
    
while bandera!=False:

    print('1.SUBIR ARCHIVO')
    print('2.DESCARGAR DE MIS ARCHIVOS')
    print('6.SALIR')
    opcion=input('-->')
    if int(opcion)==1:
        subirArchivo()
    if int(opcion)==2:
        descargarArchivo()
    if int(opcion)==3:
        os.system ("cls")
        print('Gracias por usar la aplicacion!!!')
        bandera=False
    if int(opcion)>3 or  int(opcion)<1:
        print('opcion incorrecta!!!')