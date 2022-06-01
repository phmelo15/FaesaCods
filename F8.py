#Faça um programa que faça um cronometro imprimindo minutos e segundos. Dica: procure pela função sleep da biblioteca os

import time
import os
for i in range(14, -1, -1):
  for j in range(59, -1, -1):
    os.system("clear")
    print(f'\r{i:02d}:{j:02d}')
    time.sleep(1)
    