import json
import os

def guardar(nombreArchivo, nombreUser):
    data={}

    data['infoArchivo']=[]
    with open('data.json')as file:
        filesize=os.path.getsize('data.json')
        if filesize >0:
            dataq=json.load(file)

            dataq['infoArchivo'].append({
                'nombreArchivo':nombreArchivo,
                'nombreUsuario':nombreUser
            })

            with open('data.json','w')as file:
                json.dump(dataq, file, indent=4)
        else:
            data['infoArchivo'].append({
                'nombreArchivo':nombreArchivo,
                'nombreUsuario':nombreUser
            })
            with open('data.json','w')as file:
                json.dump(data, file, indent=4)

def mostrar(nombreArvhivo):
    with open(nombreArvhivo)as file:
        data=json.load(file)
    return data