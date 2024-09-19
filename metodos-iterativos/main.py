import sys
import json
from inspect import getmembers, isfunction
import metodos

try:
    metodos_tuple_list = getmembers(metodos, isfunction)
    metodos_list = [m[0] for m in metodos_tuple_list]

    if len(sys.argv) < 2 or sys.argv[1] not in metodos_list:
        msg = 'Informe um dos seguintes argumentos:\n'
        msg += '\n'.join(map(lambda m: '- %s' % m, metodos_list))
        raise SystemExit(msg)

    m_file = open('matrizes.json')
    matrizes = json.loads(m_file.read())
    m_file.close()

    for indice, matriz in matrizes.items():
        print(indice, matriz)

    metodos.jacobi()
    metodos.gauss_seidel()
except Exception as e:
    print(e)
