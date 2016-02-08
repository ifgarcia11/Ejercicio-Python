total = 0
contar = 1
lista=[1,1]
iteraciones = int(raw_input("Ingrese el numero de iteraciones:"))
while iteraciones != contar:
  sumaTotal =0
  if iteraciones == 1:
    lista=[1]
  elif iteraciones ==2:
     lista=[1,1]
  else:
    if len(lista)!=contar+1:
     a = lista[contar-2]
     b = lista[contar-1]
     sumaTotal=a+b
     lista.append(sumaTotal)
  contar = contar + 1

print(lista)