import sys
import src.cli as cli
import src.methods as methods
import src.utils as utils

try:
    cli.process_args()
    method_name = sys.argv[1]
    datafile_name = sys.argv[2]
    method = getattr(methods, method_name)
    json = utils.get_data_from_file(datafile_name)
    for index, matrix in json.items():
        kwargs = utils.get_method_kwargs(matrix, method_name)
        print(cli.build_result(index, method(**kwargs)))

except Exception as e:
    print(str(e))
