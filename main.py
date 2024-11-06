import sys
import src.cli as cli
import src.methods as methods
import src.utils as utils

try:
    cli.process_args()
    method_name = sys.argv[1]
    datafile_name = sys.argv[2]
    method = getattr(methods, method_name)
    systems = utils.get_data_from_file(datafile_name)
    for index, system in systems.items():
        x = method(system)
        result = cli.build_result(index, x)
        print(result)

except Exception as e:
    print(str(e))
