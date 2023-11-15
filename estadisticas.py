categoria1 = 0
categoria2 = 0
categoria3 = 0
categoria4 = 0
acumulador = 0
entrada = str(input("¿Hay un animal a registrar? "))
while entrada == "si":
  acumulador +=1 
  edad = int(input("Ingrese la edad del animal "))
  if edad < 2:
    categoria1 +=1
  elif edad >=2 and edad <5:
    categoria2 +=1
  elif edad >= 5 and edad<10:
    categoria3 +=1
  elif edad >=10:
    categoria4 +=1
  entrada = str(input("¿Hay un animal a registrar? "))
o1= categoria1*100 / acumulador
o2= categoria2*100 / acumulador
o3= categoria3*100 / acumulador
o4= categoria4*100 / acumulador

print(f"El porcentaje por la primera categoria es de {o1}, de la segunda {o2}, de la tercera {o3}, y la cuarta de {o4}")
