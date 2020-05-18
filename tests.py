import filecmp
from contextlib import redirect_stdout

if __name__ == '__main__':

   test_scripts = [
       "configuration",
       "yaml",
       "xml",
       "json",
       "universe",
       "ssl_x509_cert",
       "standard_model",
       "table",
       "divide_by_7"
   ]

   checkOuputDiffs = False

   for ts in test_scripts:
       print(f"Executing {ts} test")
       if checkOuputDiffs:
           with redirect_stdout(outfile := open(f"./tests/{ts}_test.out", 'w')):
               exec(open(f"./examples/{ts}.py").read())
           outfile.close()
       else:
           print("-"*100)
           exec(open(f"./examples/{ts}.py").read())
           print


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











