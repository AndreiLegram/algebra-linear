import json

from . import methods
from os import listdir
from os.path import isfile, join
from inspect import getmembers, isfunction
from src.models import LinearSystem

try:
    listdir('data')
    DATA_DIR = 'data'
except FileNotFoundError:
    DATA_DIR = 'algebra-linear/data'

def get_method_list():
    return [m[0] for m in getmembers(methods, isfunction)]

def get_datafile_list():
    try:
        files = []
        for f in listdir(DATA_DIR):
            file_name = join(DATA_DIR, f)
            if isfile(file_name):
                file = open(file_name)
                json.loads(file.read())
                files.append(f)
                file.close()
        if not files:
            msg = 'ERRO: Nenhum arquivo encontrado para base de dados\n' \
                  'Insira um arquivo JSON na pasta \'%s\'' % DATA_DIR
            raise Exception(msg)
        return files
    except ValueError as e:
        msg = 'ERRO: O arquivo \'%s\' é inválido\n' \
              'Mensagem: \'%s\'' % (file_name, str(e))
        raise Exception(msg)

def get_data_from_file(file_name):
    file = open(join(DATA_DIR, file_name))
    data = json.loads(file.read())
    file.close()
    if not data:
        msg = 'ERRO: O arquivo JSON \'%s\' é inválido' % file_name
        raise Exception(msg)
    return data

def get_systems_from_data(data, system_name):
    systems = []
    for i, system_raw in data.items():
        if system_name and i != system_name:
            continue
        if 'A' not in system_raw:
            msg = 'ERRO: O sistema \'%s\' não possui matriz A' % i
            raise Exception(msg)
        systems.append(LinearSystem(i, **system_raw))
    return systems
