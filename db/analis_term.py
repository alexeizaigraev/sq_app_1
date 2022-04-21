import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import get_data

def base_data():
    q = """SELECT terminals.termial, 
departments.department, departments.street, 
departments.hous, departments.address
FROM public.terminals, public.departments
WHERE terminals.department = departments.department
AND departments.partner != 'intime'
AND terminals.model != 'УЕ РККС'
AND terminals.model != 'УЕРККС'"""
    return get_data(q)


def niseStr(str):
    return str.replace("’", '').replace("'", '').replace(' ', '').replace('-', '').replace('`', '').lower() 


def strInBoth(str1, str2):
    str1 = niseStr(str1)
    str2 = niseStr(str2)
    if ( str1 in str2 ) or ( str2 in str1 ):
        return True
    return False


def main():
    info = ''
    count = 0
    termData = file_to_arr(IN_DATA_PATH + "terminals_sverka.csv")
    data = base_data()
    for item in data:
        termBase = item[0]
        depBase = item[1]
        streetBase = item[2]
        housBase = item[3]
        #addBase = item[4]

        for termLine in termData:
            if termLine[0] == termBase and 'tru' in termLine[1]:
                if strInBoth(termLine[2], streetBase) and strInBoth(termLine[2], housBase):
                    continue
                else:
                    info += f'{ termLine[0]}\nтерминал: \t{termLine[2]}\n_____база: \t{streetBase} {housBase}\n\n'
                    count += 1
                    
    info = f'\n\tошибок {count}\n\n{info}'
    save_and_show(info, 'info.txt')
    return info