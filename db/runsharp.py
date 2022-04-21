import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

import subprocess
from modules import file_to_vec
from papa_pg import *

def main():
    info = ''
    #app_path = file_to_vec('Config/app_path.txt')[0]
    app_path = 'C:/SharpForPy/SharpForPy.exe'
    try:
        #os.startfile('C:/Users/a.zaigraev/source/repos/alexeizaigraev/SharpForPy/bin/Release/SharpForPy.exe')
        subprocess.run(app_path)
        info += '\n\tsuccess sharp\n\n'
    except Exception as ex:
        info += '\n>> no start sharp\n\n'

    clear_table('otbor')
    clear_table('departments')
    clear_table('terminals')

    info += otbor_from_file_full()
    #info += 'otbor ok\n'
    info += dep_from_file_full() + '\n'
    #info += 'dep ok\n'
    info += term_from_file_full() + '\n'
    #info += 'term ok\n'
    return info
