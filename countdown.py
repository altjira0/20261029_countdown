
import time
import json
#1. Leemos el JSON y lo guardamos en un diccionario con json.load(file)
with open("colorcables.json", "r") as file:
     cables = json.load(file)



#2. Función que pregunta qué cable cortar
def intentar_desactivar():
    cable = input("Ingresa el color del cable que deseas cortar: ")
    
    if cable.lower() in cables["desactivan"]:
        print("Bomba desactivada! Salvaste tu kulito")
        return True 
    
    elif cable in cables["no_hacen_nada"]:
        print("No ha pasado nada...")
        return False
    else: 
         print("Ese cable no existe")
    return False



#3. Cuenta atrás de 10 a 0
for number in range(10,-1,-1):
    time.sleep(1)

    if (number % 2 == 0):
            if intentar_desactivar():
                break


    if number == 5:
           print("...")
          #para que se salte el elemento en el que le dices que salte y sigue con la cuenta
    
    if number <= 5 and number >= 3:
        continue
    if number == 0:
        print("Booooooommmm (pringi)! ")
        break

    print(number)
    
