import filecmp
from contextlib import redirect_stdout
import sys
import difflib
from glob import glob

if __name__ == '__main__':

   print(sys.argv)
   for f in sorted(glob("./tests/*.ref")): print(f)

   if sys.argv[1]=='all':
       testScripts = ["configuration", "json", "ssl_x509_cert", "yaml", "xml"]
       #testScripts = ["configuration", "yaml", "xml", "json", "universe", "ssl_x509_cert", "standard_model", "table", "divide_by_7"]
       checkOuputDiffs = True
   else:
       testScripts = sys.argv[1:]
       checkOuputDiffs = False

   for ts in testScripts:
       print("-"*100, end='')
       print(f"Executing {ts} test")
       if checkOuputDiffs:               # output to files
           refOutFile = f"./tests/{ts}_test.ref"
           newOutFile = f"./tests/{ts}_test.out"
           with redirect_stdout(outfile := open(newOutFile, 'w')):
               exec(open(f"./examples/{ts}.py").read())
               outfile.close()
           with open(refOutFile) as f1: f1Text = f1.readlines()
           with open(newOutFile) as f2: f2Text = f2.readlines()
           numDiffLines = 0
           for l in difflib.ndiff(f1Text, f2Text):
               if l[0] in ['+', '-']:
                   print(l, end='')
                   numDiffLines +=1
           print(f"{ts} test  num diffs = {numDiffLines//2}")
       else:                             # to stdout
           exec(open(f"./examples/{ts}.py").read())
           print

#    print("Done")




