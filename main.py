import sys
import src.cli as cli
import src.methods as methods
import src.utils as utils

try:
    print('\n- Validando argumentos')
    cli.process_args()
    datafile_name = sys.argv[1]
    systems = utils.get_data_from_file(datafile_name)
    if len(sys.argv) >= 3:
        method_name = sys.argv[2]
        method = getattr(methods, method_name)
    else:
        method_list = utils.get_method_list()

    for system in systems:
        print('\n- Iniciando operação com o sistema "%s"' % system.i)
        if len(sys.argv) >= 3:
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
