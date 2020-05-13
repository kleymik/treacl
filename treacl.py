#
#  treacl.py
#
# Treacl - Tree Class - fun exploiting dynamic attibutes in Python
#
# 2018-06-02 kleymik  - yet another derivative of very similar tree/graph datatypes

import re
from pprint import pformat
from textwrap import indent
from collections.abc import Iterable

class Treacl(object):
    ''' Treacl: a tree class'''


    # attribute manipulation

    def __getattr__(self, name):                                                          # dunder method that get's called when in the attributes
        '''only called for undefined attributes'''                                        # does not (yet) exist in the object (__dict__)
        setattr(self, name, vdd := Treacl())                                              # I am the walrus
        return vdd

    def __getstate__(self): return vars(self)                                             # otherwise pickle complains
    def __setstate__(self, state): vars(self).update(state)


    # Treacl "user" properties                                                            # as an alternative to attributes in the dunder .__dict__
                                                                                          # see README explanation
    __props = {}

    def __init__(self):
        self.__props = {"long_name": None,
                        "type"     : None }

    def addProp(self, pName, value):
        self.__props[pName] = value
        return value

    def delProp(self, pName):
        del self.__props[pName]
        return pName

    def getProp(self, pName):
        return self.__props[pName]

    def listProps(self):
        return [ k for k in self.__props.keys() ]


    # some basic traversal methods

    treeMaxDepth = 100                                                             # in case of cycles: to limit searches & traversals
    depthIndent = 4                                                                       # indent for tree printing

    def pf_indented(self, v, indent=0):
        '''use pprint pformat but then addtional indent for given depth
        '''                                                                               # (pprint module inserts one less whitespace for first line)
        pfStrings = pformat(v, width=40).split('\n')                                      # (indent=1 is default, giving everything one extra whitespace)
        return [('' if num==0 else ' ' * indent) + line for num, line in enumerate(pfStrings)]

    def pptree(self, depth=0):
        '''print treacl tree recursively'''
        if depth < self.treeMaxDepth:
            for at in [k for k in vars(self).keys() if not k.startswith('_')]:            # same as self.__dict__: # tbd: if singleton, don't print a CRLF
                print(nameStr := ' ' * self.depthIndent * depth + f'{at}: ', end='')
                atv = getattr(self, at)                                                   # attribute value
                if isinstance(atv, Treacl):
                    print()
                    atv.pptree(depth + 1)                                                 # recurse
                elif isinstance(atv, list) and any([isinstance(e, Treacl) for e in atv]): # recurse into lists only (not any other iterables), if case they contain at leat one Treacl
                    print()
                    for e in atv:                                                         # note deeper nested lists are not checked
                        if isinstance(e, Treacl): e.pptree(depth + 1)                     # recurse
                        else:
                            for s in self.pf_indented(e, depth=depth+1): print(s)         # use pretty print to print python base datatype
                else:
                    for s in self.pf_indented(atv, len(nameStr)): print(s)                # tbd: keep indent even if multi-line
        else:
            print(f"Max recursion depth reached {self.treeMaxDepth}")

    def tprint(self, depth=0):
        for at in [k for k in vars(self).keys() if not k.startswith('_')]:                # tbd: if singleton, don't print a CRLF
            atv = getattr(self, at)                                                       # attribute value
            print('\n'+'Z' * self.depthIndent * depth, f'{at}: ', end='')
            treacl_pprint(atv, depth + 1)                                                 # recurse


    def pathsToList(self, curPath="", resLst=[], depth=0, showValP=False):                # list all paths in tree
        '''generate all paths to a given depth'''
        for at in [k for k in vars(self).keys() if not k.startswith('_')]:
            if not at.startswith('_'):
                resLst += [pth := curPath+'.'+f'{at}']
                if isinstance(atv := getattr(self, at), Treacl): atv.pathsToList(pth, resLst) # recurse
        return resLst


    def findPaths(self, pattrn, depth=0, showValP=False):                                 # list paths that match a pattern
        '''search tree recursively depth first
           find all paths with pattern matching
           anywhere in the path
        '''
        return [ p for p in self.pathsToList() if pattrn in p.split('.')]


    def findPathsRegex(self, regexPattrn, caseSensitive=re.I, depth=0, showValP=False):   # list paths that match a regex pattern
        '''search tree recursively depth first
           find all paths with pattern matching
           anywhere in the path
        '''
        lineRePat = re.compile(regexPattrn, re.I)
        return [ p for p in self.pathsToList() if lineRePat.search(p)]


    # graph functions

    def ppgraph(self, depth=0, occurDict={}):
        '''print treacl graph recursively'''

        print(' ' * self.depthIndent * depth+self.getProp("name"))
        occurDict[self] = True
        if depth < self.treeMaxDepth:
            for at in [k for k in vars(self).keys() if not k.startswith('_')]:            # tbd: if singleton, don't print a CRLF
                nameStr = ' ' * self.depthIndent * depth + f'{at}: '
                print(nameStr, end='')
                atv = getattr(self, at)                                                   # attribute value
                if isinstance(atv, Treacl):
                    print()
                    if atv not in occurDict: atv.ppgraph(depth + 1, occurDict=occurDict)  # recurse
                elif isinstance(atv, list) and any([isinstance(e, Treacl) for e in atv]): # recurse into lists only (not any other iterables), if case they contain at leat one Treacl
                    print()
                    for e in atv:                                                         # note deeper nested lists are not checked
                        if isinstance(e, Treacl):
                            if e not in occurDict: e.ppgraph(depth + 1, occurDict=occurDict) # recurse
                        else:
                            for s in self.pf_indented(e, depth=depth+1): print(s)         # use pretty print to print python base datatype
                else:
                    for s in self.pf_indented(atv, len(nameStr)): print(s)                # tbd: keep indent even if multi-line
        else:
            print(f"Max recursion depth reached {treeMaxDepth}")


    # import / export graphs

    def paths_to_dot():
        ''' export data as dot/dotty graph format file
            assumes all nodes are reachable from this point
        '''
        return None

