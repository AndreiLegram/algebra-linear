import sys
import src.utils as utils

def process_args():
    method_list = utils.get_method_list()
    datafile_list = utils.get_datafile_list()
    if len(sys.argv) < 2 or sys.argv[1] not in method_list:
        msg = 'Primeiro argumento inválido...\n' \
              'Informe um dos seguintes métodos para o cálculo:\n'
        msg += '\n'.join(map(lambda m: '- %s' % m, method_list))
        raise Exception(msg)
    if len(sys.argv) < 3 or sys.argv[2] not in datafile_list:
        msg = 'Segundo argumento inválido...\n' \
              'Informe um dos seguintes arquivos como base de dados:\n'
        msg += '\n'.join(map(lambda f: '- %s' % f, datafile_list))
        raise Exception(msg)

def build_result(index, result):
    # TODO build_result
    return {index: result}