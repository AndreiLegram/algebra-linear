import sys
import src.cli as cli
import src.methods as methods
import src.utils as utils

try:
    print('\n- Validando argumentos')
    cli.process_args()
    datafile_name = sys.argv[1]
    data = utils.get_data_from_file(datafile_name)
    systems = utils.get_systems_from_data(data)
    method_list = utils.get_method_list()
    if len(sys.argv) >= 3:
        method = getattr(methods, sys.argv[2])
        if not method:
            system_name = sys.argv[2]

    for system in systems:
        if system_name and system.i != system_name:
            continue
        print('\n- Iniciando operação com o sistema "%s"' % system.i)
        if len(sys.argv) >= 3 and method:
            if method:
                x = method(system)
                result = cli.build_result(system, method_name, x)
                print(result)
        else:
            print('\n------------')
            for method_name in method_list:
                method = getattr(methods, method_name)
                x = method(system)
                result = cli.build_result(system, method_name, x)
                print('%s\n------------' % result)

except Exception as e:
    print(str(e))
