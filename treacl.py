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

    def attrs_list(self, sortedP=False):
        attrs = [k for k in vars(self).keys() if not k.startswith('_')]
        if sortedP==True: return sorted(attrs)
        else:             return attrs

    # Treacl "user" properties                                                            # as an alternative to attributes in the dunder .__dict__
                                                                                          # see README explanation
    __props = {}

    def __init__(self):
        self.__props = {"name": None,                                                     # making assumption that having at least "name" seems sensible, so ok to have core code that references it
                        "type": None }

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

    treeMaxDepth     = 1000                                                               # in case of cycles: to limit searches & traversals
    depthIndent      =    4                                                               # number of spaces indent for tree printing
    valPrintMaxWidth =   40                                                               # for pformat # width is max horizontal number of characters, e.g when printing a list

    def pformat_indented(self, v, indent=0):
        '''use pprint pformat but then add additional indent for given depth'''           # pprint module inserts one less whitespace for first line
        pfStrings = pformat(v, width=self.valPrintMaxWidth).split('\n')
        return [('' if num==0 else ' ' * indent) + line for num, line in enumerate(pfStrings)]

    def pptree(self, depth=0, sortedP=False):
        '''print treacl tree recursively'''
        if depth < self.treeMaxDepth:
            print()                                                                       # TBD: if singleton, don't print a CRLF
            for at in self.attrs_list(sortedP=sortedP):                                   # same as self.__dict__:
                print(nameStr := ' ' * self.depthIndent * depth + f'{at}: ', end='')
                atv = getattr(self, at)                                                   # atv = attribute value
                if isinstance(atv, Treacl): atv.pptree(depth + 1)                         # recurse
                elif isinstance(atv, list) and any([isinstance(e, Treacl) for e in atv]): # recurse into lists only (not any other iterables), if case they contain at leat one Treacl
                    for e in atv:                                                         # note deeper nested lists are not checked
                        if isinstance(e, Treacl): e.pptree(depth + 1)                     # recurse
                        else:
                            for s in self.pformat_indented(e, depth=depth+1): print(s)    # use pretty print to print python base datatype
                else:
                    for s in self.pformat_indented(atv, len(nameStr)): print(s)           # TBD: keep indent even if multi-line
        else:
            print(f"Max recursion depth reached {self.treeMaxDepth}")

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

    def tree_nodes_to_list(self):                                                         # list all paths in tree
        '''return a list of all the nodes in the tree'''                                  # tbd make into a generator
        resLst = [self]
        for atv in [ getattr(self, at) for at in self.attrs_list() ]:                     # iterate over attribute values: which could be (i) a Treacl instance, a list with maybe Treacl Instances, (iii) neither
            if isinstance(atvL := [atv] if isinstance(atv, Treacl) else atv, list):       # ok yes slighlty cryptic - put it in a list if it's a singleton Treacl object
                resLst += [t for v in atvL if isinstance(v, Treacl) for t in v.tree_nodes_to_list()]  # flatened list of lists
        return resLst

    def tree_find_paths(self, pattrn, varName=''):                                        # list paths that with a simple pattern match
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

    def tree_find_paths_pathex(self, path_expression, varName="", greedyFlg=False):       # list paths that match a path-expression pattern
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
            pathCar, _, pathCdr = path_expression.partition('.')
            includePartMatch = pathCdr!='' and greedyFlg
            for at in self.attrs_list():
                if pathCar=='*' \
                   or pathCar==at \
                   or (pathCar.startswith('*') and pathCar[1:]==at) \
                   or (pathCar.endswith('*')    and pathCar[:-1]==at):
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

    # def tree_find_paths_pathexex # TBD extended path-expressions

    # graph functions

    def ppgraph(self, depth=0, occurDict={}, sortedP=False):
        '''print treacl graph recursively'''                                          # print(' ' * self.depthIndent * depth+self.getProp("name"))
        occurDict[self] = True                                                        # TBD: by changing this to a counter, one could cycle up to a limit
        for at in self.attrs_list(sortedP=sortedP):                                   # TBD: if singleton, don't print a CRLF
            print()
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
                for s in self.pformat_indented(atv, len(nameStr)): print(s,end='')    # TBD: keep indent even if multi-line

    def graph_paths_to_list(self, varName="", occurDict={}):                          # list all paths in graph
        '''generate all paths to a given depth'''
        occurDict[self] = True
        resLst = []
        for at in self.attrs_list():
            resLst += [pth := f'{varName}.{at}']
            atv = getattr(self, at)
            if isinstance(atv, Treacl):
                if atv not in occurDict: resLst += atv.graph_paths_to_list(pth, occurDict) # recurse
            elif isinstance(atv, list) and any([isinstance(e, Treacl) for e in atv]):      # n.b. more deeply nested lists are not checked
                for ei,e in enumerate(atv):
                    resLst += [lpth := f'{varName}.{at}[{ei}]']
                    if isinstance(e, Treacl):
                        if e not in occurDict: resLst += e.graph_paths_to_list(lpth, occurDict) # recurse
        return resLst

    def graph_nodes_to_list(self, occurDict={}):                                     # list all paths in tree
        '''return a list of all the nodes in the tree'''                             # tbd make into a generator
        occurDict[self] = True                                                       # a bit redundant to have both occurDict and resLst
        resLst = [self]
        for at in self.attrs_list():
            atv = getattr(self, at)
            if isinstance(atv, Treacl):
                if atv not in occurDict: resLst += atv.tree_nodes_to_list(occurDict) # recurse
            elif isinstance(atv, list) and any([isinstance(e, Treacl) for e in atv]):
                for e in atv:                                                        # note deeper nested lists are not checked
                    if isinstance(e, Treacl):
                        if e not in occurDict: resLst += e.tree_nodes_to_list(occurDict) # recurse
        return resLst

    def graph_nodes_to_list1(self):                                                         # list all paths in tree
        '''return a list of all the nodes in the tree'''                                  # tbd make into a generator
        resLst = [self]
        for atv in [ getattr(self, at) for at in self.attrs_list() ]:                     # iterate over attribute values: which could be (i) a Treacl instance, a list with maybe Treacl Instances, (iii) neither
            if isinstance(atvL := [atv] if isinstance(atv, Treacl) else atv, list):       # ok yes slighlty cryptic - put it in a list if it's a singleton Treacl object
                resLst += [t for v in atvL if isinstance(v, Treacl) for t in v.graph_nodes_to_list1()]  # flatened list of lists
        return resLst

    def graph_find_paths(self, pattrn, depth=0, showValP=False):                           # list paths that match a pattern
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


        return None

