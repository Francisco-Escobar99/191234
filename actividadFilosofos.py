import time
import random
import threading
import queue 


queue = queue.Queue(maxsize=5); ##cuantos hilos pueden ser agregados en la cola

#funcion
def tenedor_filosofo(): 
    item = 0
    while True:
        if not queue.full(): 
            item += 1
            queue.put(item) 
            print('\nFilosofo', item, 'esta comiendo') 

            time_sleep = random.randint(1,3)  #tiempo de ejecusion
            time.sleep(time_sleep)
            if item ==5:
               break
            
           

def filosofo(): 
    while True:
        if not queue.empty(): # verifica que no haya un proceso en cola
            item = queue.get() # se extrae el recurso 
            queue.task_done() # indicar que la tarea esta completada
            print('\nFilosofo', item, 'ha terminado de comer')

            time_sleep = random.randint(1,3) #tiempo de ejecusion
            time.sleep(time_sleep)
            if item ==5:
               break
            

if __name__ == '__main__':
    tenedor_hilo = threading.Thread(target=tenedor_filosofo)
    filosofo_hilo = threading.Thread(target=filosofo)

    tenedor_hilo.start()
    filosofo_hilo.start()