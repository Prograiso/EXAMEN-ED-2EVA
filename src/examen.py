#EXAMEN FINAL DE PYTHON 2 EVA
def imprimir_lista_inversa(nombres):
   lista_inversa =[""]
   for nombre in range(len(nombres)-1, -1, -1):
      lista_inversa+= nombre[nombres]
   print(lista_inversa) 
   print()  


def buscar_palabra(objetivo, palabras):
    for palabra in palabras:
       if palabra == objetivo:
            return True
    return False


nombres = ["Perantano","Zutano","Fulano","Mengano","exit"]

edades = {
    "Perantano" : int(45),
    "Zutano" : int(50),
    "Fulano" : int(18),
    "Mengano" :int(0)  
}

while True:
    nombre = str(input("Buscar nombre: "))

    if buscar_palabra(nombre, nombres)==True:
        if buscar_palabra(nombre)=="exit":
            print("FIN DEL PROGRAMA")
            break
        print(str(nombre) + " tiene" + str(edades[nombre]) + " años")
    elif buscar_palabra(nombre,nombres)==False:
        print("El nombre no existe...")
    
