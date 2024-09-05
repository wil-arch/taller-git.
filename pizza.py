print("Menu de pizzas")
print("Eres vegetariano?")
print("Si (s) o No (n)")
vegetariano = input(print("s o n"))
if vegetariano == "s":
    print ("los ingredientes vegetarianos son:")
    print ("Tofu")
    print ("Pimenton")
    ingrediente = input (print ("Escoja un ingrediente Tofu (t) o pimenton (p) "))
if ingrediente == "t y p":
    print ("Por favor escoja un solo ingrediente")
elif ingrediente == "t" or "p":
    print ("Gracias por su elección, su pizza ya esta siendo preparada") 
else:
    print ("los ingredientes son:")
    print ("Peperoni")
    print ("Jamon")
    print ("Salmon") 
ingrediente_no_vegetariano = input(print("Escoja un ingrediente peperoni (p), jamon (j), salmon(s)"))
if ingrediente_no_vegetariano == "p y j" or "j y s" or "p y s" or "p y j y s":
    print ("Por favor escoja un solo ingrediente")
elif ingrediente_no_vegetariano == "p" or "j" or "s":
    print ("Gracias por su elección, su pizza ya esta siendo preparada")