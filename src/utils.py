import json

from . import methods
from os import listdir
from os.path import isfile, join
from inspect import getmembers, isfunction

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
                files.append(file_name)
                file.close()
        if not files:
            msg = 'Nenhum arquivo encontrado para base de dados\n' \
                  'Insira um arquivo JSON na pasta \'%s\'' % DATA_DIR
            raise Exception(msg)
        return files
    except ValueError as e:
        msg = 'O arquivo \'%s\' é inválido - (%s)' % (file_name, str(e))
        raise Exception(msg)

def get_items_from_datafile(file_name):
    file = open(join(DATA_DIR, file_name))
    data = json.loads(file.read())
    file.close()
    if not data:
        msg = 'O arquivo JSON \'%s\' é inválido' % file_name
        raise Exception(msg)
    return data

def validate_matrix(matrix, method):
    # TODO
    if method == 'jacobi':
        return matrix == matrix
    elif method == 'gauss_seidel':
        return matrix == matrix
    else:
        return matrix == matrix
