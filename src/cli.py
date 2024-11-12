import sys
import numpy as np
import src.utils as utils

def process_args():
    datafile_list = utils.get_datafile_list()
    if len(sys.argv) < 2 or sys.argv[1] not in datafile_list:
        msg = '\nPrimeiro argumento inválido...' \
              '\nInforme um dos seguintes arquivos como base de dados:\n'
        msg += ''.join(map(lambda f: '- %s\n' % f, datafile_list))
        raise Exception(msg)
    if len(sys.argv) >= 3:
        method_list = utils.get_method_list()
        if sys.argv[2] not in method_list:
            datafile_name = sys.argv[1]
            data = utils.get_data_from_file(datafile_name)
            system_list = data.keys()
            if sys.argv[2] not in system_list:
                msg = '\nSegundo argumento inválido...' \
                      '\nInforme um dos seguintes métodos para o cálculo:\n'
                msg += '\n'.join(map(lambda m: '- %s' % m, method_list))
                msg += '\nOu uma das seguintes matrizes como base de dados:\n'
                msg += ''.join(map(lambda s: '- %s\n' % s, system_list))
                raise Exception(msg)

def build_result(system, method_name, result):
    return '\n- Solução do sistema "%s" pelo método "%s":\n' \
        'Valores completos: \n%s\nValores arredondados: \n%s\n' \
        % (system.i, method_name, result, np.round(result.copy(), 4)) \
        if result is not None and result.any() else ''
