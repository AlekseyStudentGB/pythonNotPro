from pathlib import Path
import argparse
import logging
from collections import namedtuple

"""Напишите код, который запускается из командной строки и получает на вход
путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
○ имя файла без расширения или название каталога,
○ расширение, если это файл,
○ флаг каталога,
○ название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя
логирование"""

logging.basicConfig(filename='logi.log.',filemode='w',format= '{asctime} {levelname} строкa {lineno}: {msg}',style='{', encoding='UTF-8', level=logging.NOTSET)
logger = logging.getLogger(__name__)
pars = argparse.ArgumentParser()
pars.add_argument('path_dir', metavar='Path', type=str)
arg = pars.parse_args()

inf_dic = {}
logger.info(f'приняли аргумент {arg.path_dir}')
Inf_dir = namedtuple('Inf_dir','name_obj name_parent flag_dir type')
dir_input = Path(arg.path_dir)

for j in dir_input.iterdir():
    f = str(j)
    if j.is_dir():

        name = f[f.rfind('\\') + 1:]
        name_f = f[f[:f.rfind('\\')].rfind('\\')+1: f.rfind('\\')]
        inf_dic[name]= Inf_dir(name, name_f, True, None)
        logger.info(f'найдена дирректория {inf_dic.get(name)}')
    if j.is_file():
        name = f[f.rfind('\\') + 1:f.rfind('.')]
        name_f = f[f[:f.rfind('\\')].rfind('\\') + 1: f.rfind('\\')]
        if len(f[f.rfind('.') + 1:]) < 6:
            type_f = f[f.rfind('.') + 1:]
        else:
            type_f = 'file'
        inf_dic[name] = Inf_dir(name, name_f, False, type_f)
        logger.info(f'найден файл {inf_dic.get(name)}')
