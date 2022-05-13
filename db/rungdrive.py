import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from papa_pg import *

def main():
    info = ''
    

    clear_table('otbor')
    clear_table('departments')
    clear_table('terminals')

    info += dep_from_gdrive() + '\n'
    #info += 'dep ok\n'
    info += term_from_gdrive() + '\n'
    #info += 'term ok\n'
    return info
