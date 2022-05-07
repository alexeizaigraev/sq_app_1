from modules import *
import psycopg2
from datetime import datetime
import shutil



def db_operator(execstr, vec=[]):
    info = ''
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        info += "open\n"
        cur = con.cursor()
        if vec:
            vec =  good_vec(vec)
            cur.execute(execstr, vec)
        else:
            cur.execute(execstr)
        con.commit()
    except Exception as error:
        info += str(error) + '\n'
    finally:
        if con:
            cur.close()
            con.close()
    return info

def get_data(query):
    arr = []
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        cur.execute(query)
        rows = cur.fetchall()
    except:
        pass
    finally:
        if con:
            cur.close()
            con.close()
    return rows
 
            
def clear_table(table):
    db_operator(f'DELETE FROM {table}')

def vec_to_query(vec):
    for i in range(len(vec)):
        vec[i] = f"'{vec[i]}'"
    return ','.join(vec)

def refresh_table(table_name, fname):
    clear_table(table_name)
    info = ''
    count = 0
    q_err = 0
    arr = file_to_arr_nosharp(fname)[1:]
    con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
    cur = con.cursor()
    for vec in arr:
        vec =  good_vec(vec)
        query = f'''INSERT INTO {table_name} VALUES ({vec_to_query(vec)});'''       
        try:
            cur.execute(query)
            count += 1 
        except Exception as ex:
            info += str(ex) + '\n'
            q_err += 1
    con.commit()
    if con:
        cur.close()
        con.close()
    if q_err == 0:
        info += f'success refresh {count=} {table_name}\n\n'
    else:
        info += f'{q_err=} {count=} refresh {table_name}\n\n'
    return info


#______________________________


def term_from_file_full():
    return refresh_table('terminals', IN_DATA_PATH + 'terminals.csv')

def dep_from_file_full():
    return refresh_table('departments', IN_DATA_PATH + 'departments.csv')

def insert_all_otbor(arr):
    clear_table('otbor')
    info = ''
    count = 0
    q_err = 0
    con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
    cur = con.cursor()
    for vec in arr:
        #vec =  good_vec(vec)
        query = f''' INSERT INTO otbor (term, dep)
VALUES ('{vec[0]}', '{vec[1]}')'''
        try:
            cur.execute(query)
            count += 1 
        except Exception as ex:
            info += str(ex) + '\n'
            q_err += 1
    con.commit()
    if con:
        cur.close()
        con.close()
    if q_err == 0:
        info += f'success refresh {count=} otbor\n\n'
    else:
        info += f'\t{q_err=} {count=} refresh otbor\n\n'
    return info



def otbor_from_file_full():
    arr = file_to_arr_nosharp(IN_DATA_PATH + 'otbor.csv')[1:]
    return insert_all_otbor(arr)



#_____________________

def title_string(s):
    return s.title()

def insert_all_deps():
    return refresh_table('departments', 'departments.csv')

def mk_finish0(reg_date, mod):
    
    didi = {
        'Екселлiо FP-280': 7,
        'Екселлiо FP-700': 7,
        'Екселлiо FPP-350': 0,
        'Екселлiо FPU-550ES': 7,
        'Екселлiо FPU-550ES': 7,
        'Екселлiо FP-280': 5,
        'ПРРО': 10,
        'УЕ РККС': 0,
        }
    dd, mm, yy = reg_date.split('.')
    #yy = yy[:4]
    new_year = int(yy) + didi[mod]
    return f'{dd}.{mm}.{new_year}'


def good_date(vec):
    positions = [4, 15, 20, 21,]
    for pos in positions:
        vec[pos] = vec[pos][:10]
    return vec

def make_finish(vec):
    model = vec[2]
    register = vec[20]
    finish = vec[21]
    if not finish and register and model:
        try:
            vec[21] = mk_finish0(register, model)
        except:
            pass
            return vec


def date_log():
    ddd = datetime.now().date()
    d = str(ddd.day)
    if len(d) == 1:
        d = '0' + d
    m = str(ddd.month)
    if len(m) == 1:
        m = '0' + m
    y = str(ddd.year)
    return f'{y}.{m}.{d}'


def table_to_file(tname):
    info = ''
    q_err = 0
    arr = []
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        cur.execute(f'SELECT *  FROM {tname}')
        rows = cur.fetchall()
    except (Exception) as error:
        q_err += 1
        info == str(error) + '\n'
    finally:
        if con:
            cur.close()
            con.close()

    if tname == 'departments':
        text = 'department;region;district_region;district_city;city_type;city;street;street_type;hous;post_index;partner;status;register;edrpou;address;partner_name;id_terminal;koatu;tax_id;koatu2\n'
    else:
        text = 'department;termial;model;serial_number;date_manufacture;soft;producer;rne_rro;sealing;fiscal_number;oro_serial;oro_number;ticket_serial;ticket_1sheet;ticket_number;sending;books_arhiv;tickets_arhiv;to_rro;owner_rro;register;finish\n'

    for vec in rows:
        text += ';'.join(vec) + '\n'
    fname = f'{IN_DATA_PATH}{tname}.csv'
    text_to_file(text, fname)
    info += fname + '\n'
    try:
        fname_new = f'{PG_BACKUP_PATH}{date_log()}_{tname}.csv'
        shutil.copy(fname, fname_new)
        info += fname_new + '\n'
    except Exception as ex:
        info += f'\n{ex}\n'

    return info


def select_terms_to_file():
    return table_to_file('terminals')
 
def select_deps_to_file():
    return table_to_file('departments')


def select_deps():
    return get_data('SELECT * FROM departments')
        
def select_terms():
    return get_data('SELECT * FROM terminals')


def get_list(query):
    arr = []
    rows = get_data(query)
    for line in rows:
        if line[0]:
            arr.append(line[0])
    return arr


def get_partners():
    query = f'''SELECT DISTINCT partner
FROM departments
ORDER BY partner;'''
    return get_list(query)

def get_terminals_list():
    query = f'''SELECT termial FROM terminals
ORDER BY termial'''
    return get_list(query)

def get_terminals_list_partner(partner):
    query = f'''SELECT termial FROM terminals, departments
    WHERE departments.department = terminals.department
    AND departments.partner = '{partner}'
ORDER BY termial;'''
    return get_list(query)

def get_departments_list():
    query = f'''SELECT department FROM departments
ORDER BY department'''
    return get_list(query)


def get_otbor_deps():
    query = f'''SELECT dep FROM otbor
ORDER BY dep'''
    return get_list(query)

def get_model_list():
    query = f'''SELECT DISTINCT model FROM terminals
ORDER BY model'''
    return get_list(query)

def get_city_types():
    vec = ['',]
    query = 'SELECT DISTINCT city_type FROM departments ORDER BY city_type'
    return vec + get_list(query)

def get_street_types():
    vec = ['',]
    query = 'SELECT DISTINCT street_type FROM departments ORDER BY street_type'
    return vec + get_list(query)

def get_owners():
    vec = ['',]
    query = 'SELECT DISTINCT owner_rro FROM terminals ORDER BY owner_rro'
    return vec + get_list(query)

def get_models():
    vec = ['',]
    query = 'SELECT DISTINCT model FROM terminals ORDER BY model'
    return vec + get_list(query)

def get_softs():
    vec = ['',]
    query = 'SELECT DISTINCT soft FROM terminals ORDER BY soft DESC'
    return vec + get_list(query)

def get_seals():
    vec = ['',]
    query = 'SELECT DISTINCT sealing FROM terminals ORDER BY sealing DESC'
    return vec + get_list(query)

def col_key_pg(hh, key_col_num = -1):
    os.system('cls')
    print('\n\n')
    s = set()
    for line in hh:
        try:
            key = line[key_col_num]
            s.add(key)
        except:
            #('>> no key', key)
            pass
    
    listkey = list(s)
    for i in range(len(listkey)):
        if not listkey[i]:
            continue
        p_cyan(f'\t{i} {listkey[i]}')
    
    #print('')
    print('\n\n\n -> ', end = '')
    choise = int(input())
    os.system('cls')
    
    return listkey[choise]


def get_kabinet_pereezd_old_data():
    query = '''SELECT terminals.department,
departments.post_index, departments.region,
departments.city, departments.street, departments.hous,
departments.koatu, departments.tax_id,
terminals.model, terminals.serial_number, terminals.soft,
terminals.producer, terminals.date_manufacture,
terminals.rne_rro, terminals.fiscal_number, terminals.oro_serial, terminals.ticket_serial,
terminals.to_rro,
otbor.term
FROM otbor, terminals, departments
WHERE otbor.term = terminals.termial
AND departments.department = terminals.department
ORDER BY terminals.termial;'''
    return get_data(query)




def get_history_data():
    query = '''SELECT terminals.termial, terminals.department,
terminals.serial_number, departments.address
FROM terminals, departments, otbor
WHERE terminals.department = departments.department
AND terminals.termial = otbor.term
ORDER BY terminals.termial;'''
    return get_data(query)

def get_activ_term_data():
    query = '''SELECT terminals.termial, terminals.department,
departments.address, departments.partner
FROM terminals, departments
WHERE terminals.department = departments.department
ORDER BY terminals.termial;'''
    return get_data(query)

def get_one_term_data(term):
    query = f'''SELECT * 
FROM terminals
WHERE terminals.termial = '{term}';'''
    return get_data(query)

def get_one_dep_data(dep):
    query = f'''SELECT * 
FROM departments
WHERE departments.department = '{dep}';'''
    return get_data(query)







def loger_pg(kind):
    info = ''
    data = get_history_data()
    nau = date_log()
    con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
    cur = con.cursor()
    for vec in data:
        query = f""" INSERT INTO logi (department, termial, serial_number, address, datalog, kind)
VALUES ('{vec[0]}', '{vec[1]}', '{vec[2]}', '{vec[3]}', '{nau}', '{kind}');"""
        db_operator(query)
    info += '\n'
    try:
        info += select_terms_to_file()
        info += select_deps_to_file()
        info += '\n'
    except Exception as ex:
        info += str(ex)
    return info
    



def del_dep(dep):
    q=f"""DELETE FROM public.departments
	WHERE department = '{dep}';
    """
    db_operator(q)

def del_term(key):
    q=f"""DELETE FROM public.terminals
	WHERE termial = '{key}';
    """
    db_operator(q)


def get_one_dep_data(dep):
    q = f"""SELECT * FROM departments WHERE department = '{dep}';"""
    return get_data(q)


def title_string(s):
    return s.title()


def refresh_one_term(vec):
    vec = good_vec(vec)
    info = ''
    try:
        del_term(vec[1])
    except:
        pass
    query = f'''INSERT INTO public.terminals(
	department, termial, model, serial_number, date_manufacture, soft, producer, rne_rro, sealing, fiscal_number, oro_serial, oro_number, ticket_serial, ticket_1sheet, ticket_number, sending, books_arhiv, tickets_arhiv, to_rro, owner_rro, register, finish)
	VALUES ('{vec[0]}', '{vec[1]}', '{vec[2]}', '{vec[3]}', '{vec[4]}', '{vec[5]}', '{vec[6]}', '{vec[7]}', '{vec[8]}', '{vec[9]}', '{vec[10]}', '{vec[11]}', '{vec[12]}', '{vec[13]}', '{vec[14]}', '{vec[15]}', '{vec[16]}', '{vec[17]}', '{vec[18]}', '{vec[19]}', '{vec[20]}', '{vec[21]}');'''
    db_operator(query)
    

   
def refresh_one_dep(vec):
    vec = good_vec(vec)
    info = ''
    vec.append('')
    try:
        del_dep(vec[0])
    except:
        pass
    query = f"""INSERT INTO departments (department, region, district_region, district_city, city_type, city, street, street_type, hous, post_index, partner, status, register, edrpou, address, partner_name, id_terminal, koatu, tax_id, koatu2)
    VALUES ('{vec[0]}', '{vec[1]}', '{vec[2]}', '{vec[3]}', '{vec[4]}', '{vec[5]}', '{vec[6]}', '{vec[7]}', '{vec[8]}', '{vec[9]}', '{vec[10]}', '{vec[11]}', '{vec[12]}', '{vec[13]}', '{vec[14]}', '{vec[15]}', '{vec[16]}', '{vec[17]}', '{vec[18]}' , '{vec[19]}');"""
    db_operator(query)


#edit___________________________

def mk_txt(key_field):
    if len(key_field) < 8:
        txt = ""
        heads = file_to_arr_nosharp(IN_DATA_PATH + "departments.csv")[0]
        heads.append('koatu2')
        txt_arr = []
        for i in range(len(heads)):
            heads[i] = f'{heads[i]};'
        try:
            data = get_one_dep_data(key_field)[0]
            for i in range(len(data)):
                try:
                    heads[i] += data[i]
                except:
                    pass
        except:
            pass
        return '\n'.join(heads)
    else:
        txt = ""
        heads = file_to_arr_nosharp(IN_DATA_PATH + "terminals.csv")[0]
        txt_arr = []
        for i in range(len(heads)):
            heads[i] = f'{heads[i]};'
        try:
            data = get_one_term_data(key_field)[0]
            for i in range(len(data)):
                try:
                    heads[i] += data[i]
                except:
                    pass
        except:
            pass
        return '\n'.join(heads)


def get_key_from_textbox(txt):
    arr = txt.split('\n')
    try:
        dep = arr[0].split(';')[1]
        term = arr[1].split(';')[1]
        if dep and term and dep in term:
            return arr[1].split(';')[1]
    except:
        pass
    return arr[0].split(';')[1]

def get_data_from_textbox(txt):
    vec = []
    for line in txt.split('\n'):
        try:
            vec.append(line.split(';')[1])
        except:
            vec.append(line)
    return vec

  
def next_dep(dep):
    vec = get_departments_list()
    if dep in vec:
        if vec.index(dep) < len(vec) - 1:
            return vec[vec.index(dep) + 1]
        else:
            return vec[0]
    else:
        return(str(vec))

def pred_dep(dep):
    vec = get_departments_list()
    if dep in vec:
        if vec.index(dep) > 0:
            return vec[vec.index(dep) - 1]
        else:
            return vec[len(vec) -1]

def next_term(term):
    vec = get_terminals_list()
    if term in vec:
        if vec.index(term) < len(vec) - 1:
            return vec[vec.index(term) + 1]
        else:
            return vec[0] 

def pred_term(term):
    vec = get_terminals_list()
    if term in vec:
        if vec.index(term) > 0:
            return vec[vec.index(term) - 1]
        else:
            return vec[len(vec) -1]

def get_address(dep):
    query = f"select * from departments WHERE department = '{dep}'"
    arr = get_data(query)
    return arr[0][14]

def get_koatu(dep):
    query = f"select * from departments WHERE department = '{dep}'"
    arr = get_data(query)
    return arr[0][17]

def get_tax_id(dep):
    query = f"select * from departments WHERE department = '{dep}'"
    arr = get_data(query)
    return arr[0][18]
    
def get_koatu2(dep):
    query = f"select * from departments WHERE department = '{dep}'"
    arr = get_data(query)
    city = arr[0][5].strip()
    distrCity = arr[0][3].strip()
    koatu = arr[0][17].strip()
    if not city:
        city = ''
    if not distrCity:
        distrCity = ''
    if not koatu:
        koatu = ''
    rez = ""
    try:
        rez = mk_koatu2(city, distrCity, koatu)
    except:
        pass
    return rez

def get_serial_list():
    query = f'''SELECT DISTINCT serial_number FROM terminals
ORDER BY serial_number'''
    return get_list(query)

def get_fiscal_list():
    query = f'''SELECT DISTINCT fiscal_number FROM terminals
ORDER BY fiscal_number'''
    return get_list(query)

verb = False

#print(get_term_by_fiscal_hvost('248'))

#print(get_term_by_serial_hvost('2390 8888'))

#number = '80'
#print(get_data(f"SELECT termial, department FROM terminals WHERE fiscal_number LIKE '%{number}%'"))


