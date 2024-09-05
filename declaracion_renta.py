Renta_anual = float (input("por favor ingrese su renta anual:"))

if Renta_anual < 1000000 :
    tarifa_impositiva = "5%"

elif 1000000 <= Renta_anual <= 2000000:
    tarifa_impositiva = "15%"

elif 2000000 <= Renta_anual <= 3500000:
    tarifa_impositiva = "20%"
    
elif 3500000 <= Renta_anual <= 6000000:
    tarifa_impositiva = "30%"
else: 
    tarifa_impositiva = "45%"

print("su tarifa impositiva es del:", tarifa_impositiva)

