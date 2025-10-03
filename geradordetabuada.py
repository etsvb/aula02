print('=== Gerador de Tabuada ===')
print()

n1 = int (input('Deseja ver a tabuada de: '))
cont = 1
while (cont < 13):
  tab = n1 * cont
  print()
  print(n1, 'x', cont, '= ', tab)
  cont += 1