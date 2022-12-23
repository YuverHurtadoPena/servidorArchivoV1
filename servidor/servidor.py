import zmq
context = zmq.Context()
clientes=context.socket(zmq.REP)
clientes.bind('tcp://*:5550')

while True:
    bandL=False
    data,opcion,nombreAsig=clientes.recv_multipart()
    print(opcion)
    clientes.send_json("ok")
    
    if int(opcion.decode("utf-8"))==1:
        with open(nombreAsig.decode("utf-8"), "wb") as f:
            f.write(data)
    
    if int(opcion.decode("utf-8"))==2:
        with open(nombreAsig, "rb") as f:
            contenidoArchivo=f.read()
            clientes.send_multipart([contenidoArchivo])
            print("-----------------------")
            print("el archivo se envio con exito")
            print("-----------------------")