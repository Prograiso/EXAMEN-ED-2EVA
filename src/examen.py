#EXAMEN FINAL DE PYTHON 2 EVA
def 


def buscar_palabra(nombres,edades):
    while True:
        objetivo = input("Buscar nombre: ")
        
        for nombre in nombres:
            if objetivo == nombre:
             print((objetivo) +"tiene" (edades[objetivo]+"años"))


nombres = ["Perantano","Zutano","Fulano","Mengano","exit"]

edades = {
    "Perantano" : int(45),
    "Zutano" : int(50),
    "Fulano" : int(18),
    "Mengano" :int(0)  
}


    
