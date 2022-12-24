import json
import os

def guardar(nombreArchvio, nombreUsuer):#DAO(objeto de acceso a dato)
    data = {}
    data['infoArchivo'] = []
    with open('data.json') as file:
        filesize = os.path.getsize('data.json')
        if filesize >0:
            dataq = json.load(file)
            
            dataq['infoArchivo'].append({
                'nombreArchivo': nombreArchvio,
                'nombreUsuario': nombreUsuer
                })
            with open('data.json', 'w') as file:
                json.dump(dataq, file, indent=4)
        else:
            data['infoArchivo'].append({
                'nombreArchivo': nombreArchvio,
                'nombreUsuario': nombreUsuer
                })
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)

def mostar(nombreAchivo):
    with open(nombreAchivo) as file:
        data = json.load(file)     
    return data
