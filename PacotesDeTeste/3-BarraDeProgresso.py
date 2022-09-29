#Recursos da barra de progresso:
from tqdm import tqdm
import time

if __name__ == '__main__':
    print('')
    #Barra de progresso:
    for i in tqdm(range(10)):
        time.sleep(0.5)

    print ('pause')