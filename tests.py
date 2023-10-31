import filecmp
from contextlib import redirect_stdout
import sys
import difflib
from glob import glob

'''run each example and then do a diff on its output versus the tests/*.ref reference output'''

if __name__ == '__main__':

   print(sys.argv)
   for f in sorted(glob("./tests/*.ref")): print(f)

   if sys.argv[1]=='all':
       testScripts = ["configuration",  "divide_by_7", "json", "ssl_x509_cert", "standard_model", "table", "universe", "yaml", "xml"]
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
               #outfile.close()
           with open(refOutFile) as fRef: refText = fRef.readlines()
           with open(newOutFile) as fOut: outText = fOut.readlines()
           numDiffLines = 0
           for l in difflib.ndiff(refText, outText):
               if l[0] in ['+', '-']:
                   print(l, end='')
                   numDiffLines +=1
           print(f"{ts} test  num diffs = {numDiffLines//2}")
           print()
           print("Done")
       else:                             # to stdout
           exec(open(f"./examples/{ts}.py").read())
           print()





