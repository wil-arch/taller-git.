# taller-git.
print ("juego piedra. pi, papel. pa o tijera. ti, ")

jugada_1 = input("ingrese su jugada ines:")
jugada_2 = input ("ingrese su jugada juan:")

if jugada_1 == "pi" and jugada_2 == "ti" :
    print ("gana jugador Ines")
elif jugada_1 == "ti" and jugada_2 == "pa" :
    print ("gana jugador Ines")
elif jugada_1 == "pa" and jugada_2 == "pi" :
    print("gana jugador ines")
elif jugada_1 == jugada_2 :
    print ("han enpatado")    
else:
    print ("gana jugador juan")
    