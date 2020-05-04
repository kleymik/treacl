#
#  treacl.py
#
# Treacl - Tree Class - fun exploiting dynamic attibutes in Python
#
# 2018-06-02 kleymik  - derivative of very similar datatypes by myself and others

import re
from pprint import pformat
from textwrap import indent
from collections.abc import Iterable

class Treacl(object):
    ''' Treacl: a tree class'''


    # attribute manipulation

    def __getattr__(self, name):                                  # dunder method that get's called when in the attributes
        '''only called for undefined attributes'''                # does not (yet) exist in the object (__dict__)
        setattr(self, name, vdd := Treacl())                      # I am the walrus
        return vdd

    def delBranch(self, pthLst):                                  # TBD: traverses path, then deletes branch, pruning on the way back up
        if self.hasattr(pthLst[0]):                               # maybe not needed a.b.c = None
            delbranch(self, pth[1:])
            delattr()

    # a bit of support for adding properties to treacl nodes

    __props__ = {"long_name":None,                                 # Treacl "user" properties
                 "type"     :None}                                 # instead of attributes' dunder __dict__
                                                                   # - see README explanation
    def addProp(self, pName, value):
        __props__[pName] = value
        return value

    def delProp(self, pName):
        del __props__[pName]
        return pName

    def getProp(self, pName, value):
        return __props__[pName]

    def listProps(self):
        return [ k for k in __props__.keys() ]


    # some basic traversal methods

    treeMaxDepth = 10_000_000                                        # in case of cycles: to limit searches & traversals
    depthIndent = 4                                                  # indent for tree printing

    def pf_indented(self, v, indent=0):
        """use pprint pformat but then addtional indent for given depth
        """                                                          # (pprint module inserts one less whitespace for first line)
        pfStrings = pformat(v, width=20).split('\n')                 # (indent=1 is default, giving everything one extra whitespace)
        return [('' if num==0 else ' ' * indent) + line for num, line in enumerate(pfStrings)]

    def pptree(self, depth=0):
        '''print treacl tree recursively'''
        if depth < self.treeMaxDepth:
            for at in self.__dict__:                                                      # tbd: if singleton, don't print a CRLF
                atv = getattr(self, at)                                                   # attribute value
                nameStr = ' ' * self.depthIndent * depth + f'{at}: '
                print(nameStr, end='')
                if isinstance(atv, Treacl):
                    print()
                    atv.pptree(depth + 1)                                                 # recurse
                elif isinstance(atv, list) and any([isinstance(e, Treacl) for e in atv]): # recurse into lists only (not any other iterables), if case they contain at leat one Treacl
                    for e in atv:                                                         # note deeper nested lists are not checked
                        if isinstance(e, Treacl): e.pptree(depth + 1)                     # recurse
                        else:
                            for s in self.pf_indented(e, depth=depth+1): print(s)         # use pretty print to print python base datatype
                else:
                    for s in self.pf_indented(atv, len(nameStr)): print(s)                # tbd: keep indent even if multi-line
        else:
            print("Max recursion depth reached %i", treeMaxDepth)

    def tprint(self, depth=0):
        for at in self.__dict__:                                     # tbd: if singleton, don't print a CRLF
            atv = getattr(self, at)                                  # attribute value
            print('\n'+'Z' * self.depthIndent * depth, f'{at}: ', end='')
            treacl_pprint(atv, depth + 1)                            # recurse


    def pathsToList(self, curPath="", resLst=[], depth=0, showValP=False): # list all paths in tree
        '''generate all paths to a given depth'''
        for at in self.__dict__:
            pth = curPath+'.'+f'{at}'
            resLst += [pth]
            if isinstance(atv := getattr(self, at), Treacl): atv.pathsToList(pth, resLst)  # recurse
        return resLst


    def findPaths(self, pattrn, depth=0, showValP=False):                          # list paths that match a pattern
        '''search tree recursively depth first
           find all paths with pattern matching
           anywhere in the path
        '''
        return [ p for p in self.pathsToList() if pattrn in p.split('.')]


    def findPathsRegex(self, regexPattrn, caseSensitive=re.I, depth=0, showValP=False):                          # list paths that match a pattern
        '''search tree recursively depth first
           find all paths with pattern matching
           anywhere in the path
        '''
        lineRePat = re.compile(regexPattrn, re.I)
        return [ p for p in self.pathsToList() if lineRePat.search(p)]


    def findPaths2(self, pattrn, depth=0, showVal=False):                          # list paths that match a pattern
        '''search tree recursively depth first
           find all paths with pattern matching
           anywhere in the path
        '''
        for at in self.__dict__:
            atv = getattr(self, at)  # attribute value
            if isinstance(atv, Treacl):
                atv.pptree(depth + 2)  # recurse
                if pattrn in str(atv):
                    print(' ' * depth, f'{at}:')
            else:
                if pattrn in str(atv):
                    print(' ' * depth, f'{at}=', end='')
                    print(pformat(atv))


    # graph functions

    def ppgraph(self, depth=0, occurDict={}):                                   # same as pptree, but with occurs-check
        '''print graph recursively'''
        for at in self.__dict__:                                  # tbd: if singleton, don't print a CRLF
            atv = getattr(self, at)                               # attribute value
            if isinstance(atv, Treacl):
                print(' ' * depth, f'{at}: ')
                atv.pptree(depth + self.ppIndent)                 # recurse
            else:
                print(' ' * depth, f'{at}= ', end='')
                print(pformat(atv))                               # tbd: keep indent even if multi-line


    # import / export graphs

    def paths_to_dot():
        ''' export data as dot/dotty graph format file'''
        return None

# functions
## cater for Treacl and Treacl inside other datatypes structures list

treeMaxDepth = 10_000_000                                   # in case of cycles: limit any search
depthIndent = 4                                             # indent for tree printing

def treacl_pprint(node, depth=0):                            # not implemented as a method to allow pretty printer
    '''print tree recursively'''                             # that recurses into non-treacl objects too
    if isinstance(node, Treacl):
        if depth < node.treeMaxDepth:
            node.tprint(depth+1)
            # print("AA")
        else:
            print("Max recursion depth reached %i", treeMaxDepth)
    elif isinstance(node, str):
        print(pformat(node))
        # print("BB")
    elif isinstance(node, Iterable):                    # but not a  string:
        for e in node:
            if isinstance(e, Treacl): node.tprint(depth + 1) # recurse
            else:                     treacl_pprint(e, depth=depth+1)               # tbd: keep indent even if multi-line
    else:
        print(pformat(node), end='')


print("Treacl Loaded")
