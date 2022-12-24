import zmq
from libreria import*

context = zmq.Context()
cliente = context.socket(zmq.REP)
cliente.bind("tcp://*:5555")

while True:

    data,opcion,nombreArchi,nombreUser= cliente.recv_multipart()
    if int(opcion.decode("utf-8"))==1:
        guardar(nombreArchi.decode("utf-8"),nombreUser.decode("utf-8"))
        with open(nombreArchi.decode("utf-8"),"wb")as file:
            file.write(data)
            cliente.send_json("archivo guardado con exito.")

    if int(opcion.decode("utf-8"))==2:
        band=False
        JsoneAchivo="data.json"
        info=mostar(JsoneAchivo)
        for i in info['infoArchivo']:
            if i["nombreArchivo"]==nombreArchi.decode("utf-8"):
                band=True
        if band==True:
            with open(nombreArchi, "rb") as f:
                contenido = f.read()
                cliente.send_multipart([contenido])
            band=False
        else:
            m="Noexiste"
            cliente.send_multipart([m.encode("utf-8")])
    
    if int(opcion.decode("utf-8"))==3:
        JsoneAchivo="data.json"
        info=mostar(JsoneAchivo)
        cliente.send_json(info)

