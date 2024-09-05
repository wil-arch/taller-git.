print("Bienvenidos a pizzeria Bella Napoli")
pizza_vegetariana = "pimiento - tofu "
pizza_no_vegetariana = "peperoni - jamon - salmon"
ingrediente_fijo = "mozzarela - tomate"
menu_pizza = pizza_vegetariana, pizza_no_vegetariana

tipo_pizza = input ("quieres una pizza vegetariana (si/no):")
if tipo_pizza == "si" :   
      print ("ingredintes disponibles:")
      opcion_1 = print ("opcion 1:", pizza_vegetariana)
      opcion_2 = print ("opcion 2:", pizza_no_vegetariana)
      tipo_opcion = input ("escribe una opcion:")

      if tipo_opcion == "opcion 1" :
         print ("su pizza es vegetariana y contiene los siguientes ingredientes:", pizza_vegetariana, ingrediente_fijo)
      else:
         print ("su pizza no es vegetariana y contiene los siguientes ingredintes:", pizza_no_vegetariana, ingrediente_fijo)
else:
      print ("su eleccion es la pizza no vegetariana y contiene los siguientes ingredientes:", pizza_no_vegetariana, ingrediente_fijo)
      


        
    
    








