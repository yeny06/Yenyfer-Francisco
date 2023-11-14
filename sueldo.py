entrada = str(input("¿Hay un vendedor? "))
while entrada == "si":
  nombre = str(input("Ingrese el nombre del vendedor: "))
  salario_base = int(input("Ingrese el salario base del vendedor"))
  ventas = int(input("Ingrese las ventas realizadas por el  vendedor"))
  if ventas < 3500:
    p= salario_base*.07
    sueldo= salario_base+p
  elif ventas >= 3500 or ventas <= 7000:
    p= salario_base*.1
    sueldo= salario_base+p
  elif ventas > 7000:
    p= salario_base*.15
    sueldo= salario_base+p
  else:
    sueldo = 0

  print(f"El vendedor{nombre} tiene un salario total de  {sueldo}")
  entrada = str(input("¿Hay otro vendedor? "))  
