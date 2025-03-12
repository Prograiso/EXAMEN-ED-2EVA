#EXAMEN FINAL DE PYTHON 2 EVA
def buscar_palabra(nombres,edades):
    objetivo = input("Buscar nombre: ")
    for nombre in nombres:
        if objetivo == nombre:
            printstr((objetivo) +"tiene" (edades[objetivo]+"años"))


nombres = ["Perantano","Zutano","Fulano","Mengano"]

edades = {
    "Perantano" : int(45),
    "Zutano" : int(50),
    "Fulano" : int(18),
    "Mengano" :int(0)  
}


    
