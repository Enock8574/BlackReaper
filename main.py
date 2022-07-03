from scripts.ddos import *
def ascii():

    print("  ______ _            _     ______  ")                         
    print(" | ___ \ |          | |    | ___ \                          ")
    print(" | |_/ / | __ _  ___| | __ | |_/ /___  __ _ _ __   ___ _ __ ")
    print(" | ___ \ |/ _` |/ __| |/ / |    // _ \/ _` | '_ \ / _ \ '__| ")
    print(" | |_/ / | (_| | (__|   <  | |\ \  __/ (_| | |_) |  __/ |   ")
    print(" \____/|_|\__,_|\___|_|\_\ \_| \_\___|\__,_| .__/ \___|_| ")  
    print("                                           | |   ")           
    print("                                           |_| ")
    print("Raping your trash security since 2022 :p ")                                                                    
    
# Funcion para el menu principal
print(ascii())
def menu():
    print("1.Ataque DDoS")
    print("2.Transferencia de Archivos")
    print("3.Salir")
menu()
op=int(input("Ingrese una opcion: "))
while op !=0:
    if op == 1:
        print("\n")
        ddos_func()
        pass
    elif op == 2:
        print("XD")
        print("\n")
        pass
    elif op == 3:
        print("Saliendo del Sistema... \n Recuerde ser cuidadoso a la hora de realizar pruebas de pentest <3")
        exit()
        print("\n")
    menu()
    op=int(input("Ingrese una opcion: "))

