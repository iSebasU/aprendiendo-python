from random import shuffle

# lista inicial
palitos =["-", "--", "---", "----"]
# mezclar palitos
def mezclar_palitos(palitos):
    shuffle(palitos)
    return palitos

#pedir al usuario elejir  
def probar_suerte():
    intento = ""
    while intento not in ["1", "2", "3", "4"]:
        intento = input("Elige un palito (1-4): ")
    return intento

#comprobar el intento del usuario 
def comprobar_intento(lista,intento):
    seleccion = int(intento) - 1
    if lista[seleccion] == "-":
        print("¡A lavar los platos!.")
    else:
        print("¡Bien hecho! No hay platos para lavar.")
    
    print(f"Te ha tocado {lista[seleccion]} palito.")
    
    
palitos_mezclados = mezclar_palitos(palitos)  
numero_elegido = probar_suerte()
comprobar_intento(palitos_mezclados, numero_elegido)
        