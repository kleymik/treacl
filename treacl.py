#
#  treacl.py
#
# Treacl - Tree Class - exploiting dynamic attibutes in Python
#
# 2018-06-02 kleymik  - yet another small tree/graph datatype

import re
from pprint import pformat

class Treacl(object):
    ''' Treacl: a tree class'''


    # attribute manipulation

    def __getattr__(self, name):                                                          # dunder method that get's called when in the attributes
        '''only called for undefined attributes'''                                        # does not (yet) exist in the object (__dict__)
        setattr(self, name, t := Treacl())                                                # I am the walrus
        return t

    def __getstate__(self): return vars(self)                                             # otherwise pickle complains

    def __setstate__(self, state): vars(self).update(state)

    def attrs_list(self): return [k for k in vars(self).keys() if not k.startswith('_')]

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

    treeMaxDepth = 100                                                                    # in case of cycles: to limit searches & traversals
    depthIndent = 4                                                                       # indent for tree printing

    def pformat_indented(self, v, indent=0):
        '''use pprint pformat but then addtional indent for given depth
        '''                                                                               # (pprint module inserts one less whitespace for first line)
        pfStrings = pformat(v, width=40).split('\n')                                      # (indent=1 is default, giving everything one extra whitespace)
        return [('' if num==0 else ' ' * indent) + line for num, line in enumerate(pfStrings)]

    def pptree(self, depth=0):
        '''print treacl tree recursively'''
        if depth < self.treeMaxDepth:
            print()
            for at in self.attrs_list():                                                  # same as self.__dict__: # tbd: if singleton, don't print a CRLF
                print(nameStr := ' ' * self.depthIndent * depth + f'{at}: ', end='')
                atv = getattr(self, at)                                                   # attribute value
                if isinstance(atv, Treacl):
                    atv.pptree(depth + 1)                                                 # recurse
                elif isinstance(atv, list) and any([isinstance(e, Treacl) for e in atv]): # recurse into lists only (not any other iterables), if case they contain at leat one Treacl
                    for e in atv:                                                         # note deeper nested lists are not checked
                        if isinstance(e, Treacl): e.pptree(depth + 1)                     # recurse
                        else:
                            for s in self.pformat_indented(e, depth=depth+1): print(s)    # use pretty print to print python base datatype
                else:
                    for s in self.pformat_indented(atv, len(nameStr)): print(s)           # tbd: keep indent even if multi-line
        else:
            print(f"Max recursion depth reached {self.treeMaxDepth}")

    def tprint(self, depth=0):
        for at in self.attrs_list():                                                      # tbd: if singleton, don't print a CRLF
            atv = getattr(self, at)                                                       # attribute value
            print('\n'+' ' * self.depthIndent * depth, f'{at}: ', end='')
            treacl_pprint(atv, depth + 1)                                                 # recurse


    def tree_paths_to_list(self, varName=""):                                             # list all paths in tree
        '''generate all paths to a given depth'''
        resLst = []
        for at in self.attrs_list():
            resLst += [pth := f'{varName}.{at}']
            atv = getattr(self, at)
            if isinstance(atv, Treacl): resLst += atv.tree_paths_to_list(pth)             # recurse
            elif isinstance(atv, list) and any([isinstance(e, Treacl) for e in atv]):
                for ei,e in enumerate(atv):                                               # note deeper nested lists are not checked
                    resLst += [lpth := f'{varName}.{at}[{ei}]']
                    if isinstance(e, Treacl): resLst += e.tree_paths_to_list(lpth)        # recurse
        return resLst


    def tree_find_paths(self, pattrn, varName=''):                                        # list paths that match a pattern
        '''search tree depth first to find all paths with pattern matching
           attribute anywhere in the path
        '''
        return [ p for p in self.tree_paths_to_list(varName) if pattrn in p.split('.')]


    def tree_find_paths_regex(self, regexPattrn, varName="", reFlags=re.I):               # list paths that match a regex pattern
        '''search tree depth first to find all paths with regular-expression pattern matching
           anywhere in the path
        '''
        lineRePat = re.compile(regexPattrn, reFlags)
        return [ p for p in self.tree_paths_to_list(varName) if lineRePat.search(p)]


    def tree_find_paths_pathex(self, path_expression, varName="", greedyFlg=False):              # list paths that match a path-expression pattern
        '''search tree depth first to find all paths with simple glob-like pattern matching path-expression
             e.g in path-expression "xx.*yy",  the "*yy" => any attribute ending in "yy"
             e.g in path-expression "xx.yy*",  the "yy*" => any attribute beginning with "yy"
             e.g in path-expression "xx.*.yy", the "*"   => any attribute or list element
             greedyFlg==True => include paths that only match any initial part of the path-expression
             greedyFlg==False => exclude paths that only match any initial part of the path-expression
        '''
        resLst = []
        print('pathExpr', path_expression)
        if path_expression:
            if '.' in path_expression: pathCar, pathCdr = path_expression.split('.', maxsplit=1) # excuse my lisp
            else:                      pathCar, pathCdr = path_expression, None
            print('pathCar', pathCar)
            print('pathCdr', pathCdr)
            includePartMatch = pathCdr!=None and greedyFlg
            for at in self.attrs_list():
                if pathCar=='*' \
                   or pathCar==at \
                   or (pathCar.startsswith('*') and pathCar[1:]==at \
                   or (pathCar.endswith('*')    and pathCar[:-1]==at:
                    pth = f'{varName}.{at}'
                    if includePartMatch: resLst += [pth]
                    atv = getattr(self, at)
                    if isinstance(atv, Treacl): resLst += atv.tree_find_paths_pathex(pathCdr, pth)    # recurse
                    elif isinstance(atv, list) and any([isinstance(e, Treacl) for e in atv]):  # note deeper nested lists are not checked
                        for ei,e in enumerate(atv):
                            lpth = f'{varName}.{at}[{ei}]'
                            if includePartMatch: resLst += [lpth]
                            if isinstance(e, Treacl): resLst += e.tree_find_paths_pathex(pathCdr, lpth)# recurse
        return resLst

    # def tree_find_paths_pathexex # tbd extended path-expressions

    # graph functions

    def ppgraph(self, depth=0, occurDict={}):
        '''print treacl graph recursively'''

        print(' ' * self.depthIndent * depth+self.getProp("name"))
        occurDict[self] = True
        if depth < self.treeMaxDepth:
            print()
            for at in self.attrs_list():                                                  # tbd: if singleton, don't print a CRLF
                print(nameStr := ' ' * self.depthIndent * depth + f'{at}: ', end='')
                atv = getattr(self, at)                                                   # attribute value
                if isinstance(atv, Treacl):
                    if atv not in occurDict: atv.ppgraph(depth + 1, occurDict=occurDict)  # recurse
                elif isinstance(atv, list) and any([isinstance(e, Treacl) for e in atv]): # recurse into lists only (not any other iterables), if case they contain at leat one Treacl
                    for e in atv:                                                         # note deeper nested lists are not checked
                        if isinstance(e, Treacl):
                            if e not in occurDict: e.ppgraph(depth + 1, occurDict=occurDict) # recurse
                        else:
                            for s in self.pformat_indented(e, depth=depth+1): print(s)    # use pretty print to print python base datatype
                else:
                    for s in self.pformat_indented(atv, len(nameStr)): print(s)           # tbd: keep indent even if multi-line
        else:
            print(f"Max recursion depth reached {treeMaxDepth}")

    def graph_paths_to_list(self, varName="", resLst=[], curDepth=0, maxDepth=treeMaxDepth, showValP=False):                  # list all paths in tree
        '''generate all paths to a given depth'''
        for at in self.attrs_list():
            resLst += [pth := varName+'.'+f'{at}']
            if isinstance(atv := getattr(self, at), Treacl):
                atv.tree_paths_to_list(pth, resLst, curDepth+1)                           # recurse
        return resLst

    def graph_find_paths(self, pattrn, depth=0, showValP=False):                          # list paths that match a pattern
        '''search graph recursively depth first
           find all paths with pattern matching
           anywhere in the path
        '''
        return [ p for p in self.graph_paths_to_list() if pattrn in p.split('.')]


    def graph_find_paths_regex(self, regexPattrn, caseSensitive=re.I, depth=0, showValP=False):   # list paths that match a regex pattern
        '''search graph recursively depth first
           find all paths with pattern matching
           anywhere in the path
        '''
        lineRePat = re.compile(regexPattrn, re.I)
        return [ p for p in self.graph_paths_to_list() if lineRePat.search(p)]

    # import / export graphs

    def paths_to_dot():
        ''' export data as dot/dotty graph format file
            assumes all nodes are reachable from this point
        '''

        # TBD

        return None

