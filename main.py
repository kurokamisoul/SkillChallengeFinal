from services.contacto_services import registrar_contacto, mostrar_contactos, eliminar_contacto
from services.contacto_services import actualizar_contacto, cargar_contactos_json
from services.contacto_services import registrar_contactos_automaticamente, guardar_json 

def menu_contactos():
    contactos=[]
    archivo=None
    while True:
        print('\nMenu de contactos\n1.- Agregar\n2.- Ver\n3.- Eliminar' \
        '\n4.- Actualizar\n5.- Cargar contacos desde archivo\n6.- Generar datos automaticamente' \
        '\n7.- guardar datos en un archivo JSON\n8.- Salir')
        opcion= input('Opcion: ')
        
        match opcion:
            case '1':
                registrar_contacto(contactos, archivo)
            case '2':
                mostrar_contactos(contactos)
            case '3':
                eliminar_contacto(contactos, archivo)
            case '4':
                actualizar_contacto(contactos, archivo)
            case '5':
                contactos=cargar_contactos_json(contactos)
            case '6'    :
                contactos=registrar_contactos_automaticamente(archivo,contactos)
            case '7':
                archivo=guardar_json(contactos,archivo)    
            case '8':
                print('Hasta luego')
                break
            case _:
                print('Opcion no valida')


menu_contactos()