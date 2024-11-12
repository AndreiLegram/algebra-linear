import sys
import src.cli as cli
import src.methods as methods
import src.utils as utils

try:
    print('\n- Validando argumentos')
    cli.process_args()
    method = method_name = system_name = None
    if len(sys.argv) >= 3:
        try:
            method = getattr(methods, sys.argv[2])
            method_name = sys.argv[2]
        except AttributeError:
            system_name = sys.argv[2]

    data = utils.get_data_from_file(sys.argv[1])
    systems = utils.get_systems_from_data(data, system_name)
    print('\n------------')
    for system in systems:
        print('\n- Iniciando operação com o sistema "%s"\n' \
            '\nMatriz A:\n%s\n\nVetor b:\n%s' \
            % (system.i, system.A, system.b))
        if len(sys.argv) >= 3 and method:
            if method:
                x = method(system)
                result = cli.build_result(system, method_name, x)
                print('%s\n------------' % result)
        else:
            print('\n------------')
            for method_name in utils.get_method_list():
                method = getattr(methods, method_name)
                x = method(system)
                result = cli.build_result(system, method_name, x)
                print('%s\n------------' % result)

except Exception as e:
    print(str(e))
