from concurrent.futures.process import _MAX_WINDOWS_WORKERS
from tkinter import *
#import tkinter
import tkinter as tk
import tkinter.font as font
from turtle import bgcolor, width
from typing import Any

import modules
import os
import sys
import subprocess
from papa_pg import *

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


def clear_me():
    text_box.delete(1.0, END)

def work(ff):
    clear_me()
    try:
        u = ff()
        text_box.insert(1.0, u)
    except Exception as ex:
        text_box.insert(1.0, str(ex))

def work_param(ff, param):
    clear_me()
    try:
        u = ff(param)
        text_box.insert(1.0, u)
    except Exception as ex:
        text_box.insert(1.0, str(ex))



def people_priem():
    from people.priem import Priem
    clear_me()
    try:
        u = Priem()
        u.priem_main()
        text_box.insert(1.0, u.info)
    except Exception as ex:
        text_box.insert(1.0, str(ex))
   
def people_otpusk():
    from people.otpusk import Otpusk
    clear_me()
    try:
        u = Otpusk()
        u.otpusk_main()
        text_box.insert(1.0, u.info)
    except Exception as ex:
        text_box.insert(1.0, str(ex))
 
def people_perevod():
    from people.perevod import Perevod
    clear_me()
    try:
        u = Perevod()
        u.perevod_main()
        text_box.insert(1.0, u.info)
    except Exception as ex:
        text_box.insert(1.0, str(ex))

def people_postall():
    from people.postall import Postall
    clear_me()
    try:
        u = Postall()
        u.postall_main()
        text_box.insert(1.0, u.info)
    except Exception as ex:
        text_box.insert(1.0, str(ex))



def some_term():
    from some.pg_term import Term
    text = ''
    clear_me()
    try:
        u = Term()
        u.main_term()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)

def some_site():
    from some.site import main
    u = main
    work(u)

def some_hr_otbor():
    from some.hr_otbor import main
    u = main
    work(u)

def some_summury():
    from some.pg_summury import Summury
    clear_me()
    selected_items  = lb.curselection()
    partner_choise = partners[selected_items[0]]
    text = ''
    try:
        get_terminals_list_partner(partner_choise)
        u = Summury(partner_choise)
        u.main_summury()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)

def some_hr_ab():
    from some.hr_ab import main
    u = main
    work(u)

def some_natasha():
    from some.natasha import main
    u = main
    work(u)

def some_activ_term():
    from some.activ_term import activ_term
    u = activ_term
    work(u)

def some_no_work():
    from some.no_work import main
    u = main
    work(u)



def otbor_text():
    from db.add_otbor import Otbor
    mytext = str(text_box.get(1.0, END)).strip()
    text = ''
    
    try:
        u = Otbor(mytext)
        u.otbor_main()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    clear_me()    
    text_box.insert(1.0, text)
    
def otbor_text_list():
    from db.add_otbor_hard_dep import OtborHardDep
    mytext = str(text_box.get(1.0, END)).strip()
    text = ''
    
    try:
        u = OtborHardDep(mytext)
        u.main_otbor_hard_dep()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    clear_me()    
    text_box.insert(1.0, text)

def otbor_term_text():
    from db.otbor_term_text import main
    mytext = str(text_box.get(1.0, END)).strip()
    work_param(main, mytext)

def otbor_dep_text():
    from db.otbor_dep_text import main
    mytext = str(text_box.get(1.0, END)).strip()
    work_param(main, mytext)

def otbor_fiscal_text():
    from db.otbor_fiscal_text import main
    mytext = str(text_box.get(1.0, END)).strip()
    work_param(main, mytext)

def otbor_serial_text():
    from db.otbor_serial_text import main
    mytext = str(text_box.get(1.0, END)).strip()
    work_param(main, mytext)

def otbor_text_list_term():
    from db.add_otbor_hard_term import OtborHardTerm
    mytext = str(text_box.get(1.0, END)).strip()
    text = ''
    
    try:
        u = OtborHardTerm(mytext)
        u.main_otbor_hard_term()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    clear_me()    
    text_box.insert(1.0, text)




def otbor_text_list_serial():
    from db.add_otbor_serial import OtborSerial
    mytext = str(text_box.get(1.0, END)).strip()
    text = ''
    
    try:
        u = OtborSerial(mytext)
        u.main_otbor_serial()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    clear_me()    
    text_box.insert(1.0, text)


def otbor_text_list_serial_hvost():
    from db.add_otbor_serial_hvost import OtborSerialHvost
    mytext = str(text_box.get(1.0, END)).strip()
    text = ''
    
    try:
        u = OtborSerialHvost(mytext)
        u.main_otbor_serial_hvost()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    clear_me()    
    text_box.insert(1.0, text)

def otbor_serial_file():
    from db.add_otbor_serial_file import OtborSerialFile
    text = ''
    try:
        u = OtborSerialFile()
        u.main_otbor_serial_file()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    clear_me()    
    text_box.insert(1.0, text)

def otbor_fiscal_file():
    from db.otbor_fiscal_file import main
    u = main
    work(u)
    
def otbor_otbor():
    from db.add_otbor_hard import OtborHard
    if modules.lb_status == 'term':
        clear_me()
        values = [lb.get(idx) for idx in lb.curselection()]
        try:
            u = OtborHard(values)
            u.main_otbor_hard()
            text_box.insert(1.0, u.info)
        except Exception as ex:
            text_box.insert(1.0, str(ex))
    elif modules.lb_status == 'partn':
        partner_choise  = partners[lb.curselection()[0]]
        if partner_choise:
            terminals = get_terminals_list_partner(partner_choise)
            clear_lb()
            for item in terminals:
                lb.insert(END, item)
            modules.lb_status = 'term'
    else:
        clear_me()
        text_box.insert(1.0, '\nДа ладно :)')



def monitor_rasklad():
    from monitor.walker import Walker
    clear_me()
    try:
        u = Walker()
        u.walker_main()
        text_box.insert(1.0, u.info)
    except Exception as ex:
        text_box.insert(1.0, str(ex))

def monitor_accback():
    from monitor.accback import accback
    u = accback
    work(u)
    
def monitor_monitor():
    from monitor.monitor import main
    u = main
    work(u)

def monitor_get_rp():
    from monitor.get_rp import get_rp
    u = get_rp
    work(u)
    
def monitor_get_rp_all():
    from monitor.get_rp_all import GetRpAll
    clear_me()
    selected_items  = lb.curselection()
    choise = folders[selected_items[0]]
    text = ''
    try:
        u = GetRpAll(choise)
        u.get_rp_all_main()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
        #text = '123'
    text_box.insert(1.0, text)
 
def monitor_gnetz_copy():
    from monitor.gnetz import Gnetz
    kind = 'copy'
    text = ''
    clear_me()
    try:
        u = Gnetz(kind)
        u.gnetz_main()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)

def monitor_gnetz_move():
    from monitor.gnetz import Gnetz
    kind = 'move'
    text = ''
    clear_me()
    try:
        u = Gnetz(kind)
        u.gnetz_main()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)  

def monitor_gdrive_backup_comon():
    from monitor.gdrive_backup_comon import GdriveBackComon
    text = ''
    clear_me()
    try:
        u = GdriveBackComon()
        u.gdriveback_comon_main()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)  

def monitor_gdrive_backup_date():
    from monitor.gdrive_backup_date import GdriveBackDate
    kind = 'move'
    text = ''
    clear_me()
    try:
        u = GdriveBackDate()
        u.gdrive_back_date_main()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)  



def kabinet_rro():
    from kabinet.rro import main
    u = main
    work(u)

def kabinet_pereezd():
    from kabinet.pereezd import main
    u = main
    work(u)

def kabinet_otmena():
    from kabinet.otmena import main
    u = main
    work(u)
    
def kabinet_prro():
    from kabinet.prro import main
    u = main
    work(u)
    
def kabinet_knigi():
    from kabinet.knigi import main
    u = main
    work(u)


def actual_analis_term():
    from db.analis_term import main
    u = main
    work(u)

def actual_del_otbor_dep():
    from db.del_otbor_dep import DelOtborDep
    text = ''
    clear_me()
    try:
        u = DelOtborDep()
        u.main_del_otbor_dep()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)

def actual_del_otbor_term():
    #from db.del_otbor_term import DelOtborTerm
    info = ''
    q = 'SELECT * FROM OTBOR'
    otbor = get_data(q)
    for line in otbor:
        term = line[0]
        try:
            del_term(term)
            info += f'- {term}\n'
        except Exception as ex:
            info += f'{ex}\n'
    text_box.insert(1.0, info)


def doc_activaciya():
    from doc.activaciya import Activaciya
    text = ''
    clear_me()
    try:
        u = Activaciya()
        u.main_activaciya()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)

def doc_act_peredachi():
    from doc.act_peredachi import ActPeredachi
    text = ''
    clear_me()
    try:
        u = ActPeredachi()
        u.main_act_peredachi()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)

def doc_dep():
    from doc.dep_to_file import DepToFile
    text = ''
    clear_me()
    try:
        u = DepToFile()
        u.main_dep_to_file()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)

def doc_term():
    from doc.term_to_file import TermToFile
    text = ''
    clear_me()
    try:
        u = TermToFile()
        u.main_term_to_file()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)

def doc_logi():
    from doc.logi_to_file import LogiToFile
    text = ''
    clear_me()
    try:
        u = LogiToFile()
        u.main_logi_to_file()
        
        ()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)

def doc_pg_back():
    from doc.doc_pg_back import DocPgBack
    text = ''
    clear_me()
    try:
        u = DocPgBack()
        u.main_doc_pg_back()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)



def edit_dep_from_file():
    from edit.dep_from_file import DepFromFile
    text = ''
    clear_me()
    try:
        u = DepFromFile()
        u.main_dep_from_file()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)

def edit_term_from_file():
    from edit.term_from_file import TermFromFile
    text = ''
    clear_me()
    try:
        u = TermFromFile()
        u.main_term_from_file()
        text += u.info + '\n'
    except Exception as ex:
        text += str(ex) + '\n'
    text_box.insert(1.0, text)




def clear_lb():
    #terms = get_terminals_list()
    lb.delete(0, END)


def mk_partners():
    clear_lb()
    partners = get_partners()
    for partner in partners:
        lb.insert(END, partner)
    modules.lb_status = 'partn'


def mk_terminals():
    clear_lb()
    terminals = get_terminals_list()
    for terminal in terminals:
        lb.insert(END, terminal)
    modules.lb_status = 'term'

def mk_folders():
    clear_lb()
    items = comon_data_list(3)
    for item in items:
        lb.insert(END, item)
    modules.lb_status = 'fold'
 


"""
if modules.lb_status[0] == 'partn':
        partner_choise  = partners[lb.curselection()[0]]
        if partner_choise:
            clear_lb()
            terminals = get_terminals_list_partner(partner_choise)
            for item in terminals:
                lb.insert(END, item)
            modules.lb_status[0] = 'term'
            """

def refresh_lb():
    if modules.lb_status == 'term':
        otbor_otbor()
    elif modules.lb_status == 'partn':
        mk_partners()
    elif modules.lb_status == 'fold':
        mk_folders()
    else:
        mk_terminals()

def mk_term_partn():
    partner_choise  = partners[lb.curselection()[0]]
    if partner_choise:
        terminals = get_terminals_list_partner(partner_choise)
        clear_lb()
        for item in terminals:
            lb.insert(END, item)
        modules.lb_status = 'term'

def refresh_to_access():
    clear_me()
    txt = ''
    
    txt += select_deps_to_file()
    txt += select_terms_to_file()
    
    app_path = 'C:/ToAccessRelease/ToAccess1.exe'
    try:
        os.system(app_path)
        #clear_me()
        txt += 'ToAccess1 finish\n'
    except Exception as ex:
        txt += f'{str(ex)}\n\n'
    text_box.insert(1.0, txt)

def refresh_from_access():
    from db.runsharp import main
    u = main
    work(u)    
        
def refresh_to_access_NO_NO_NO():
    txt = ''
    app_path = 'C:/SharpForPy/SharpForPy.exe'
    try:
        os.system(app_path)
        txt += 'runsharp finish\n'
    except Exception as ex:
        txt += f'{str(ex)}\n\n'
        print(ex)
    #clear_table('departments')
    #clear_table('terminals')

    txt += f'\n{otbor_from_file_full()}\n'
    txt += dep_from_file_full()
    txt += term_from_file_full()

    text_box.insert(1.0, txt)

    """
    app_path = file_to_vec('Config/app_path.txt')[0]
    try:
        subprocess.run(app_path)
    except:
        pass
    u = RefreshAll()
    u.main_refresh()
    """
    #mk_partners()
    mk_terminals() 
    #mk_folders()

def win_dep():
    os.system(f'{PYTHON_NAME} win_dep.pyw')
def win_term():
    os.system(f'{PYTHON_NAME} win_term.pyw')
def win_kabinet():
    os.system(f'{PYTHON_NAME} win_kabinet.pyw')
def win_win():
    os.system(f'{PYTHON_NAME} win.pyw')

def show_otbor():
    clear_me()
    q = 'SELECT * FROM otbor'
    data = get_data(q)
    txt = str(data).replace("[('", '').replace("')]", '').replace('), (', '\n').replace("'", '')
    text_box.insert(1.0, str(txt))

def enter_pressed(event):
    txt = str(text_box.get(1.0, END)).strip()
    #clear_me()
    if ' ' not in txt:
        if len(txt) == 7:
            otbor_text()
        else:
            otbor_text_list_term()
    else:
        split_text = txt.split(' ')
        if len(split_text[0]) == 7:
            if len(split_text) == 2:
                otbor_text()
            else:
                otbor_text_list()
        else:
            otbor_text_list_term()

 
root = Tk()

mainmenu = Menu(root)

font_size = 18
font_style = "Verdana"
root.config(menu=mainmenu)
bigfont = font.Font(family="Veranda",size=20)
#root.option_add("*Font", bigfont)


lb_memu = Menu(mainmenu, tearoff=0, bg = 'cyan', fg='darkblue')
lb_memu.add_command(label="Терминалы", command=mk_terminals, font=(font_style, font_size))
lb_memu.add_command(label="Партнёры", command=mk_partners, font=(font_style, font_size))
lb_memu.add_command(label="Папки", command=mk_folders, font=(font_style, font_size))
lb_memu.add_command(label="Очисти", command=clear_lb, font=(font_style, font_size))


people_memu = Menu(mainmenu, tearoff=0, bg = 'cyan', fg='darkblue')
people_memu.add_command(label="Приём", command=people_priem, font=(font_style, font_size))
people_memu.add_command(label="Отпуск", command=people_otpusk, font=(font_style, font_size))
people_memu.add_command(label="Перевод", command=people_perevod, font=(font_style, font_size))
people_memu.add_command(label="Рассылка", command=people_postall, font=(font_style, font_size))


 
some_memu = Menu(mainmenu, tearoff=0, bg = 'cyan', fg='darkblue')
some_memu.add_command(label="Терминалы", command=some_term, font=(font_style, font_size))
some_memu.add_command(label="Сайт", command=some_site, font=(font_style, font_size))
some_memu.add_command(label="Кадры отбор", command=some_hr_otbor, font=(font_style, font_size))
some_memu.add_command(label="Кадры", command=some_summury, font=(font_style, font_size))
some_memu.add_command(label="Сводка АБ", command=some_hr_ab, font=(font_style, font_size))
some_memu.add_command(label="Наташа", command=some_natasha, font=(font_style, font_size))
some_memu.add_command(label="Активные кассы", command=some_activ_term, font=(font_style, font_size))
some_memu.add_command(label="Нерабочие отделения", command=some_no_work, font=(font_style, font_size))


otbor_memu = Menu(mainmenu, tearoff=0, bg = 'cyan', fg='darkblue')
otbor_memu.add_command(label="Терминалы текст", command=otbor_term_text, font=(font_style, font_size))
otbor_memu.add_command(label="Отделения текст", command=otbor_dep_text, font=(font_style, font_size))
otbor_memu.add_command(label="ФН текст", command=otbor_fiscal_text, font=(font_style, font_size))
otbor_memu.add_command(label="ЗН текст", command=otbor_serial_text, font=(font_style, font_size))

otbor_memu.add_command(label="Выбор", command=otbor_otbor, font=(font_style, font_size))
otbor_memu.add_command(label="Отделения от до", command=otbor_text, font=(font_style, font_size))
otbor_memu.add_command(label="Список отделений", command=otbor_text_list, font=(font_style, font_size))
otbor_memu.add_command(label="Список терминалов", command=otbor_text_list_term, font=(font_style, font_size))
otbor_memu.add_command(label="Список ЗН", command=otbor_text_list_serial, font=(font_style, font_size))
otbor_memu.add_command(label="Хвосты ЗН", command=otbor_text_list_serial_hvost, font=(font_style, font_size))
otbor_memu.add_command(label="ЗН из файла", command=otbor_serial_file, font=(font_style, font_size))
otbor_memu.add_command(label="ФН из файла", command=otbor_fiscal_file, font=(font_style, font_size))
otbor_memu.add_command(label="Покажи", command=show_otbor, font=(font_style, font_size))


refresh_memu = Menu(mainmenu, tearoff=0, bg = 'cyan', fg='darkblue')
refresh_memu.add_command(label="из акцесса", command=refresh_from_access, font=(font_style, font_size))


monitor_memu = Menu(mainmenu, tearoff=0, bg = 'cyan', fg='darkblue')
monitor_memu.add_command(label="Расклад", command=monitor_rasklad, font=(font_style, font_size))
monitor_memu.add_command(label="Бекап", command=monitor_accback, font=(font_style, font_size))
monitor_memu.add_command(label="Монитор", command=monitor_monitor, font=(font_style, font_size))
monitor_memu.add_command(label="РП отбор", command=monitor_get_rp, font=(font_style, font_size))
monitor_memu.add_command(label="РП партнёр", command=monitor_get_rp_all, font=(font_style, font_size))
monitor_memu.add_command(label="Жнец копи", command=monitor_gnetz_copy, font=(font_style, font_size))
monitor_memu.add_command(label="Жнец муви", command=monitor_gnetz_move, font=(font_style, font_size))
monitor_memu.add_command(label="Гугл бекап общий", command=monitor_gdrive_backup_comon, font=(font_style, font_size))
monitor_memu.add_command(label="Гугл бекап дата", command=monitor_gdrive_backup_date, font=(font_style, font_size))


kabinet_memu = Menu(mainmenu, tearoff=0, bg = 'cyan', fg='darkblue')
kabinet_memu.add_command(label="Рро", command=kabinet_rro, font=(font_style, font_size))
kabinet_memu.add_command(label="Переезд", command=kabinet_pereezd, font=(font_style, font_size))
kabinet_memu.add_command(label="Отмена", command=kabinet_otmena, font=(font_style, font_size))
kabinet_memu.add_command(label="Прро", command=kabinet_prro, font=(font_style, font_size))
kabinet_memu.add_command(label="Книги", command=kabinet_knigi, font=(font_style, font_size))


clear_memu = Menu(mainmenu, tearoff=0, bg = 'cyan', fg='darkblue')
clear_memu.add_command(label="Очистка", command=clear_me, font=(font_style, font_size))

actual_memu = Menu(mainmenu, tearoff=0, bg = 'cyan', fg='darkblue')
actual_memu.add_command(label="Анализ терминалы", command=actual_analis_term, font=(font_style, font_size))
actual_memu.add_command(label="Удали отделения отбор", command=actual_del_otbor_dep, font=(font_style, font_size))
actual_memu.add_command(label="Удали терминалы отбор", command=actual_del_otbor_term, font=(font_style, font_size))

doc_memu = Menu(mainmenu, tearoff=0, bg = 'cyan', fg='darkblue')
doc_memu.add_command(label="Бекап", command=doc_pg_back, font=(font_style, font_size))
doc_memu.add_command(label="Активация", command=doc_activaciya, font=(font_style, font_size))
doc_memu.add_command(label="Акт передачи", command=doc_act_peredachi, font=(font_style, font_size))
doc_memu.add_command(label="Отделения", command=doc_dep, font=(font_style, font_size))
doc_memu.add_command(label="Терминалы", command=doc_term, font=(font_style, font_size))
doc_memu.add_command(label="Логи", command=doc_logi, font=(font_style, font_size))


refresh_memu = Menu(mainmenu, tearoff=0, bg = 'cyan', fg='darkblue')
refresh_memu.add_command(label="из акцесса", command=refresh_from_access, font=(font_style, font_size))

edit_memu = Menu(mainmenu, tearoff=0, bg = 'cyan', fg='darkblue')
edit_memu.add_command(label=" + Отделения из файла", command=edit_dep_from_file, font=(font_style, font_size))
edit_memu.add_command(label=" + Терминалы из файла", command=edit_term_from_file, font=(font_style, font_size))
edit_memu.add_command(label="Удали отделения отбор", command=actual_del_otbor_dep, font=(font_style, font_size))
edit_memu.add_command(label="Удали терминалы отбор", command=actual_del_otbor_term, font=(font_style, font_size))


win_memu = Menu(mainmenu, tearoff=0, bg = 'cyan', fg='darkblue')
win_memu.add_command(label="Отделения", command=win_dep, font=(font_style, font_size))
win_memu.add_command(label="Терминалы", command=win_term, font=(font_style, font_size))
win_memu.add_command(label="Кабинет", command=win_kabinet, font=(font_style, font_size))
win_memu.add_command(label="Окно", command=win_win, font=(font_style, font_size))

mainmenu.add_cascade(label="Люди", menu=people_memu)
mainmenu.add_cascade(label="Всячина", menu=some_memu)
mainmenu.add_cascade(label="Монитор", menu=monitor_memu)
mainmenu.add_cascade(label="Кабинет", menu=kabinet_memu)
mainmenu.add_cascade(label="Очистка", menu=clear_memu)
mainmenu.add_cascade(label="Актуаль", menu=actual_memu)
mainmenu.add_cascade(label="Доки", menu=doc_memu)
mainmenu.add_cascade(label="Отбор", menu=otbor_memu)                
mainmenu.add_cascade(label="Обнови", menu=refresh_memu)
mainmenu.add_cascade(label="Окна", menu=win_memu)
mainmenu.add_cascade(label="Добавь", menu=edit_memu)
mainmenu.add_cascade(label="Листбокс", menu=lb_memu)

root.config(menu=mainmenu)

bigfont = font.Font(family="Veranda",size=20)
font_size = 18
font_style = "Verdana"
BOX_WIDH = 10

text_box = Text(font=(font_style, font_size), width=70, foreground='darkmagenta', background='cyan')
text_box.pack(side='left', padx=10, pady=10)
scroll_text = Scrollbar(command=text_box.yview)
scroll_text.pack(side='left', fill=Y)
text_box.config(yscrollcommand=scroll_text.set)

lb = Listbox(selectmode=EXTENDED, font=(font_style, font_size), foreground='blue', background='cyan', width=10)
lb.pack(side='left', fill=Y, padx=10, pady=10)
scroll_terminals = Scrollbar(command=lb.yview)
scroll_terminals.pack(side='left', fill=Y)
lb.config(yscrollcommand=scroll_terminals.set)





buttonFont = font.Font(size=18)

button_clear = tk.Button(text="очисти", command=clear_me, background = 'cyan', foreground='darkgreen')
button_clear.pack(side='top', padx=10, pady=10, fill=X)
button_clear['font'] = buttonFont

button_input = tk.Button(text="из текста", command=otbor_text, background = 'cyan', foreground='darkblue')
button_input.pack(side='top', fill=X)
button_input['font'] = buttonFont

btn = tk.Button(text="из списка", command=otbor_otbor, background = 'cyan', foreground='darkblue')
btn.pack(side='top', fill=X)
btn['font'] = buttonFont

btn_term = tk.Button(text="терминалы", command=mk_terminals, background = 'cyan', foreground='darkblue')
btn_term.pack(side='top', fill=X)
btn_term['font'] = buttonFont

btn_partn = tk.Button(text="партнёры", command=mk_partners, background = 'cyan', foreground='darkblue')
btn_partn.pack(side='top', padx=10, pady=10, fill=X)
btn_partn['font'] = buttonFont

btn_term_partn = tk.Button(text="терм партн", command=mk_term_partn, background = 'cyan', foreground='darkblue')
btn_term_partn.pack(side='top', fill=X)
btn_term_partn['font'] = buttonFont

button_summury_partn = tk.Button(text="кадры партн", command=some_summury, background = 'cyan', foreground='darkblue')
button_summury_partn.pack(side='top', padx=10, pady=10, fill=X)
button_summury_partn['font'] = buttonFont

btn_fold = tk.Button(text="папки", command=mk_folders, background = 'cyan', foreground='darkblue')
btn_fold.pack(side='top', fill=X)
btn_fold['font'] = buttonFont

btn_clearlb = tk.Button(text="сотри лб", command=clear_lb, background = 'cyan', foreground='darkblue')
btn_clearlb.pack(side='top', fill=X)
btn_clearlb['font'] = buttonFont


#button_refresh = tk.Button(text="акцесс", command=refresh_me, background = 'cyan', foreground='darkblue')
button_refresh_from_access = tk.Button(text="из акцесса", command=refresh_from_access, background = 'cyan', foreground='darkgreen')
button_refresh_from_access.pack(side='top', padx=10, pady=10, fill=X)
button_refresh_from_access['font'] = buttonFont


btn_windep = tk.Button(text="отделения", command=win_dep, background = 'cyan', foreground='blue')
btn_windep.pack(side='top', fill=X)
btn_windep['font'] = buttonFont

btn_winterm = tk.Button(text="терминалы", command=win_term, background = 'cyan', foreground='blue')
btn_winterm.pack(side='top', fill=X)
btn_winterm['font'] = buttonFont

btn_winkabinet = tk.Button(text="кабинет", command=win_kabinet, background = 'cyan', foreground='blue')
btn_winkabinet.pack(side='top', fill=X)
btn_winkabinet['font'] = buttonFont


button_refresh_to_access = tk.Button(text="в акцесс", command=refresh_to_access, background = 'cyan', foreground='darkmagenta')
button_refresh_to_access.pack(side='top', padx=10, pady=10, fill=X)
button_refresh_to_access['font'] = buttonFont


partners = get_partners()
folders = comon_data_list(3)

terminals = get_terminals_list()

modules.lb_status = 'term'



root["bg"] = "cyan"
#root.bind('<Return>', enter_pressed)
root.mainloop()