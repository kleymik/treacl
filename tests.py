import filecmp
from contextlib import redirect_stdout

# import difflib
# def difftest():
#     import difflib
#     with open('file1') as f1:
#         f1_text = f1.read()
#         with open('file2') as f2:
#             f2_text = f2.read()
#             # Find and print the diff:
#             for line in difflib.unified_diff(f1_text, f2_text, fromfile='file1', tofile='file2', lineterm=''):
#                 print line

if __name__ == '__main__':

   test_scripts = [
       #configuration",
       #yaml",
       #xml",
       #json",
       "ssl_x509_cert"
   ]
#       "table",
#       "standard_model",
#       "divide_by_7"
#       "mini_backprop"
#       "quantlib_instruments_hierarchy"

#       "universe"

   for ts in test_scripts:
       print(f"Executing {ts} test")
       with redirect_stdout(outfile := open(f"./tests/{ts}_test.out", 'w')):
           print("-"*100)
           exec(open(f"./examples/{ts}.py").read())
       outfile.close()

       # if filecmp.cmp(f"./tests/{ts}_test.ref", f"./tests/{ts}_test.out"): print("TEST PASSED for: configuration")
       # else:                                                            print("TEST FAILED for: configuration")

    # print("-"*100)
    # exec(open("./examples/yaml.py").read()) #  > tests/yaml_test.out
    # # diff tests/yaml_test.ref tests/yaml_test.out

    # print("-"*100)
    # exec(open("./examples/xml.py").read())
    # # diff tests/xml_test.ref tests/xml_test.out

    # print("-"*100)
    # exec(open("./examples/json.py").read())
    # # diff tests/json_test.ref tests/json_test.out

    # print("-"*100)
    # exec(open("./examples/table.py").read())
    # # diff tests/table_test.ref tests/table_test.out

    # print("-"*100)
    # exec(open("./examples/standard_model.py").read())
    # # diff tests/standard_model_test.ref tests/standard_model_test.out












