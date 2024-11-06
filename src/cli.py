import sys
import numpy as np
import src.utils as utils

def process_args():
    datafile_list = utils.get_datafile_list()
    if len(sys.argv) < 2 or sys.argv[1] not in datafile_list:
        msg = 'Primeiro argumento inválido...\n' \
              'Informe um dos seguintes arquivos como base de dados:\n'
        msg += '\n'.join(map(lambda f: '- %s' % f, datafile_list))
        raise Exception(msg)
    if len(sys.argv) >= 3:
        method_list = utils.get_method_list()
        if sys.argv[2] not in method_list:
            msg = 'Segundo argumento inválido...\n' \
                  'Informe um dos seguintes métodos para o cálculo:\n'
            msg += '\n'.join(map(lambda m: '- %s' % m, method_list))
            raise Exception(msg)

def build_result(system, method_name, result):
    rounded_result = np.round(result.copy(), 4)
    return '\n- Solução do sistema "%s" pelo método "%s":\n' \
        'Valores absolutos: \n%s\nValores arredondados: \n%s\n' \
        % (system.i, method_name, result, rounded_result)
