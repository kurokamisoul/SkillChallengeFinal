from models.contacto import crear_contacto
from faker  import Faker
from datetime import date
import json
import tkinter as tk
from tkinter import filedialog

TOTAL_CONTACTOS = 15

fake= Faker("es_MX")

def generar_id(contactos):
    if not contactos:
        return 1
    return max(contacto['id'] for contacto in contactos)+1

def validar_telefono(telefono):
    while len(telefono)>10 or len(telefono)<10 or not telefono.isdigit():
        if len(telefono)>10 or len(telefono)<10:
            print('El telefono debe de contener 10 caracteres numericos')
        if not telefono.isdigit():
            print('El numero solo debe contener nuemeros')    
        telefono=input('ingresa el telefono')
    return telefono

def validar_email(email):
    while not email.strip() or '@' not in email or '.' not in email.split('@')[1]:
        if not email.strip():
            print("El campo email no debe ser vacio")
        if '@' not in email:
            print("El campo email debe tener @")
        
        elif '.' not in email.split('@')[1]:
            print("El campo email debe tener un dominio")
        email= input('ingresa el email ')
    return email

def registrar_contacto(contactos, archivo):
    nombre_contacto = input('ingresa el nombre ')
    telefono = validar_telefono(input('ingresa el telefono '))
    email = validar_email(input('ingresa el email '))
    fecha_creacion = date.today().strftime('%d/%m/%Y')
    contacto = crear_contacto(generar_id(contactos) ,nombre_contacto, telefono, email, fecha_creacion)
    contactos.append(contacto)
    print(f"El contacto {contacto["nombre_contacto"]} se agrego correctamente")
    if archivo:
        guardar_json(contactos, archivo)
    return contacto

def registrar_contactos_automaticamente(archivo, contactos):
    for _ in range(TOTAL_CONTACTOS):
        telefono = str(fake.random_number(digits=10, fix_len=True))
        contacto=crear_contacto(generar_id(contactos), fake.name(),telefono , fake.email(), date.today().strftime('%d/%m/%Y'))
        contactos.append(contacto)
    if archivo:
        guardar_json(contactos, archivo)
    return contactos

def actualizar_contacto(contactos,archivo):
    nombre= input('Nombre del contacto que desea actualizar: ')
    for contacto in contactos:
        if contacto['nombre_contacto'].lower() == nombre.lower():
            contacto['nombre_contacto'] = input('ingresa el nombre ')
            contacto['telefono'] = validar_telefono(input('ingresa el telefono '))
            contacto['email'] = validar_email(input('ingresa el email '))
            print("se actualizo el contacto")
            if archivo:
                guardar_json(contactos, archivo)
            return
    print("Sin resultados")    


def eliminar_contacto(contactos, archivo):
    nombre= input('Nombre del contacto que desea eliminar: ')
    for contacto in contactos:
        if contacto['nombre_contacto'].lower() == nombre.lower():
            contactos.remove(contacto)
            if archivo:
                guardar_json(contactos, archivo)
            print("Contacto eliminado")
            return
    print("Sin resultados")

def mostrar_contactos(contactos):
    for contacto in contactos:
        print(contacto)

def cargar_json(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
    except json.JSONDecodeError:
        print("archivo corrupto")
        return[]

def guardar_json(contactos, archivo):
    if archivo:
      ruta_archivo=archivo
    else:    
        root = tk.Tk()
        root.withdraw()
        ruta_archivo= filedialog.asksaveasfilename(
        defaultextension=".json",
        filetypes=[("Archivos JSON", "*.json"), ("Todos los archivos", "*.*")],
        title="Guardar archivo JSON"
        )
    try:
        with open(ruta_archivo, 'w', encoding='utf-8') as file:
            json.dump(contactos,file, ensure_ascii=False, indent=2)
            return ruta_archivo
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

def importar_contactos_archivo(contactos, datos_contactos_archivo):
    for dato_contacto in datos_contactos_archivo:
        contacto= crear_contacto(
            generar_id(contactos),
            dato_contacto['nombre_contacto'],
            dato_contacto['telefono'],
            dato_contacto['email'],
            dato_contacto['fecha_creacion']
            )
        contactos.append(contacto)
    return contactos    
            
def cargar_contactos_json(contactos):
    root = tk.Tk()
    root.withdraw()
    ruta_archivo = filedialog.askopenfilename(
        title="Selecciona un archivo JSON",
        filetypes=[("Archivos JSON", "*.json"), ("Todos los archivos", "*.*")]
    )
    datos_contactos_archivo=cargar_json(ruta_archivo)
    if contactos:
        contactos= importar_contactos_archivo(contactos, datos_contactos_archivo)
    else:
        contactos= datos_contactos_archivo
    print("se cargo la informacion con exito")
    return contactos

