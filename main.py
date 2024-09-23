import sys
import src.cli as cli
import src.methods as methods
import src.utils as utils

try:
    cli.process_args()
    method_name = sys.argv[1]
    datafile_name = sys.argv[2]
    method = getattr(methods, method_name)
    items = utils.get_items_from_datafile(datafile_name)
    for index, matrix in items:
        utils.validate_matrix(matrix, method_name)
        result = cli.build_result(index, method(*matrix))
        print(result)

except Exception as e:
    raise SystemExit(str(e))
