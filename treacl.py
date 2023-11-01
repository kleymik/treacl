#
#  treacl.py
#
# Treacl - a Tree Class - exploiting dynamic attibutes in Python
#
# 2018-06-02 kleymik  - yet another small tree/graph datatype

import re
import sys
from pprint import pformat
import pickle
import json
from fnmatch import fnmatch

class Treacl(object):
    ''' Treacl: a tree class'''


    def __init__(self, **kwargs):
        setattr(self, '_tattrs', [])
        setattr(self, '_props',  {})
        for k,v in kwargs.items(): self._props[k] = v                                     # object constructor kwargs go into props


    # --- attribute manipulation

    def __getattr__(self, name):                                                          # the dunder method that gets called when attribute
        '''only called for undefined attributes'''                                        # does not (yet) exist in the object (__dict__)
        setattr(self, name, t := Treacl())                                                # I am the walrus
        return t

    def __setattr__(self, name, val):
        if not name.startswith("_"): self.__dict__['_tattrs'] += [name]                   # go directly to the dict to avoid setattr infinite recursion
        self.__dict__[name] = val

    def __getstate__(self): return vars(self)                                             # otherwise pickle complains

    def __setstate__(self, state): vars(self).update(state)


    # --- attribute access

    def attrs_list(self, sortedP=False):
        if sortedP==True: return sorted(self._tattrs)
        else:             return self._tattrs

    def gav(self, at):
        '''gav: get attribute value
           one level of indirection to make getattr() function
           a method. And might be handy for interception
        '''
        return getattr(self, at)

    def attr_get_aslist(self, at):                                                        # return value, if it's a singleton Treacl instance, return as a one-item list
        atv = self.gav(at)
        if isinstance(atv, list) and any([isinstance(e, Treacl) for e in atv]): return atv
        else:                                                                   return [atv]

    def has_attr(self, at):                                                              # "treacl" attrs recorded in a separate private dict
        return at in self._tattrs

    def evp(self, pth):                                                                   # very short name is better than "eval_path",  danger eval is hackable!
        ''' eval path expression: return value or node at end of given path'''            # use some kind of reduce(gav,path.splt('.') ??
        return eval(f"self{pth}")


    # --- "user" properties                                                               # as an alternative to attributes in the dunder .__dict__
                                                                                          # see README explanation
    def setProp(self, pName, value):                                                      # setProp rather than addProp since it will replace if prop already exists
        self._props[pName] = value
        return value

    def delProp(self, pName):
        del self._props[pName]
        return pName

    def getProp(self, pName):
        return self._props[pName]

    def listProps(self):
        return [*self._props]                                                             # return dict keys as a list


    # --- inspection utilities

    def st(self):                                                                         # see tree of attributes and type
        for f in self.tree_paths_to_list():                                               # TBD: omit type if it endswith "Treacl"
            vType = str(type(eval("self"+f))).split("'")[1]
            print("  {0:<40s} {1:s}".format(f, "" if vType.endswith('Treacl') else vType))

    def stp(self, tstExpr='..'):                                                          # see tree paths according to path expression
        for p in self.tree_find_paths_pathex(tstExpr): print(p)

    def stv(self):    self.pptree(maxDepth=1)                                             # convenience inspection methods
    def stvv(self):   self.pptree(maxDepth=2)
    def stvvv(self):  self.pptree(maxDepth=3)
    def stvvvv(self): self.pptree(maxDepth=4)


    # --- tree traversal methods

    _depthIndent      =    4                                                               # number of spaces indent for tree printing
    _valPrintMaxWidth =   40                                                               # for pformat # width is max horizontal number of characters, e.g when printing a list
    _ppMaxDepth       = 1000                                                               # default maximum depth for indented printing/exporting of treacl trees or graphs

    def pformat_indented(self, v, indent=0):
        '''use pprint pformat but then add additional indent for given depth'''           # pprint module inserts one less whitespace for first line
        pfStrings = pformat(v, width=self._valPrintMaxWidth).split('\n')
        return [ ('' if num==0 else ' ' * indent) + line for num, line in enumerate(pfStrings) ]

    def ppattrs(self, sortedP=False, file=sys.stdout):
        '''pretty print one level: treacl object attributes and their values'''
        print(file=file)                                                                  # TBD: if singleton, don't print a CRLF
        for at in self.attrs_list(sortedP=sortedP):                                       # same as self.__dict__:
            print(nameStr := ' ' * self._depthIndent * 0 + f'{at}: ', end='', file=file)
            for atv in self.attr_get_aslist(at):                                          # deeper nested lists are not checked
                for s in self.pformat_indented(atv, len(nameStr)): print(s, file=file)    # use pretty print to print python base datatype
                                                                                          # TBD: add justShow = type|size|subnodes|·..
    def pptree(self, depth=0, sortedP=False, file=sys.stdout, maxDepth=_ppMaxDepth):
        '''pretty print many levels: treacl object attributes and their values'''
        print(file=file)                                                                  # TBD: if singleton, don't print a CRLF
        if depth<maxDepth:
            for at in self.attrs_list(sortedP=sortedP):                                   # same as self.__dict__:
                print(nameStr := ' ' * self._depthIndent * depth + f'{at}: ', end='', file=file)
                for atv in self.attr_get_aslist(at):                                      # more deeply nested lists are not checked
                    if isinstance(atv, Treacl):
                        atv.pptree(depth + 1, file=file, maxDepth=maxDepth)               # recurse
                    else:
                        for s in self.pformat_indented(atv, len(nameStr)): print(s, file=file)# use pretty print to print python base datatype

    def tree_paths_to_list(self, cpth=""):                                                # list all paths in tree
        '''generate all paths to a given depth'''
        resLst = []
        for at in self.attrs_list():
            resLst += [pth := f'{cpth}.{at}']
            if isinstance(atv := self.gav(at), Treacl):
                resLst += atv.tree_paths_to_list(pth)                                     # recurse
            elif isinstance(atv, list) and any([isinstance(e, Treacl) for e in atv]):
                for ei,e in enumerate(atv):                                               # more deeply nested lists are not scanned for Treacl nodes
                    resLst += [lpth := f'{cpth}.{at}[{ei}]']
                    if isinstance(e, Treacl): resLst += e.tree_paths_to_list(lpth)        # recurse
        return resLst

    def tree_leaf_paths_to_list(self, cpth=""):                                           # list all leaf paths in tree (no intermediate paths)
        '''generate all leaf paths'''
        resLst = []
        for at in self.attrs_list():
            if   isinstance(atv := self.gav(at), Treacl): resLst += atv.tree_leaf_paths_to_list(f'{cpth}.{at}')  # recurse
            elif isinstance(atv, list) and any([isinstance(e, Treacl) for e in atv]):
                for pth in [ e.tree_leaf_paths_to_list(f'{cpth}.{at}[{ei}]') for ei,e in enumerate(atv) if isinstance(e, Treacl) ]: resLst += pth # keep collated list flat
            else: resLst += [f'{cpth}.{at}']
        return resLst

    def tree_nodes_to_list(self):                                                         # list all treacl nodes in tree
        '''return a list of all the treacl nodes in the tree'''                           # tbd make into a generator
        resLst = [self]
        for atvL in [ self.attr_get_aslist(at) for at in self.attrs_list() ]:             # iterate over attribute values: which could be a list one or more Treacl Instances, or other
            resLst += [ t for v in atvL if isinstance(v, Treacl)                          # flattened list of lists
                            for t in v.tree_nodes_to_list() ]
        return resLst

    def tree_find_paths(self, pthElem, varName=''):                                       # list paths that with a simple string equality match
        '''search tree depth first to find all paths with pattern matching
           attribute anywhere in the path
        '''
        return [ p for p in self.tree_paths_to_list(varName) if pthElem in p.split('.')]

    def tree_find_paths_regex(self, regexPattrn, varName="", reFlags=re.I):               # list paths that match a regex pattern
        '''search tree depth first to find all paths with regular-expression pattern matching
           anywhere in the path
        '''
        lineRePat = re.compile(regexPattrn, reFlags)
        return [ p for p in self.tree_paths_to_list(varName) if lineRePat.search(p)]

    def tree_find_paths_pathex(self, pthXpr, valP=False, printP=False, caseFoldP=False):  # leavesOnly=False list paths that match a path-expression pattern
        '''generate all paths matching path expression pthXpr:
             e.g. in path expression "..",                     => all paths
             e.g. in path expression "..xyz..",                => all paths containing "xyx" as attribute (= path member) anywhere in path
             e.g. in path expression "..xyz",                  => all paths with leaf attribute equal to xyz (i.e end of path)
             e.g. in path expression "xx..*yy",      the "*yy" => all paths containg "xx" as attribute, with leaf attribute ending in "yy"
             e.g. in path expression "xx..yy*",      the "yy*" => all paths beginning with attribute "xx" and ending with attribute "yy"
             e.g. in path expression "..~*xyz*",     the "~"   => complmentary set: all paths that do not match with attribute "*xyz*"
             e.g. in path expression "..=*xvy*",     the "="   => any leaf value whose string repr matches
             e.g. in path expression "..=~*xvy*",    the "="   => any leaf value whose string repr matches
         TBD e.g. in path expression "..abc*|*xyz.." the "|"   => alternation path matches abc* OR *xyz
         TBD e.g. in path expression ".*abc*"        the "."   => only first level attributes matching "abc"
         TBD e.g. in path expression ".*abc*.."      the "."   => all paths under first level attributes matching "abc"

          attribute matching is based on "glob" style matching typically used on unix path names
          the python library module "fnmatch" is used for this (even though it's
          not file paths that we are attempting to match). glob style matching
          is simpler than regex:
                Pattern   Meaning
                *         matches everything
                ?         matches any single character
                [seq]     matches any character in seq
                [!seq]    matches any character not in seq
          The glob style matching is applied to the attributes composing a path, not the path as a whole
        '''

        if caseFoldP:
            pthLst = [p.lower() for p in self.tree_leaf_paths_to_list()]                  # start with all paths, then exclude during path expression traversal
            pthXpr = pthXpr.lower()
        else:
            pthLst = self.tree_leaf_paths_to_list()                                       # start with all paths, then exclude during path expression traversal

        selPthLst = self.tree_find_paths_pathex_filter(pthLst, pthXpr)                    # leavesOnly=Falselist paths that match a path-expression pattern

        if printP:
            if valP:
                for p in selPthLst: print(p, '=', self.evp(p))
            else:
                for p in selPthLst: print(p)

        if   valP==True:        return dict([ (p, self.evp(p)) for p in selPthLst ])
        elif valP==False:       return selPthLst
        elif valP=='valsOnly':  return [ self.evp(p) for p in selPthLst ]                 # just the values in a list
        elif valP=='singleton': return [ self.evp(p) for p in selPthLst ][0]              # assumes there is only on element in the list
        elif valP=='asTree':    return None                                               # merge the paths back into a tree

        # assumes only one value is found and extracts it from the list
        # list(rr.tree_find_paths_pathex('..*sigType*', valP=1, printP=0).values())[0]

    def tree_find_paths_pathex_filter(self, pthLst, pthXpr): # leavesOnly=Falselist paths that match a path-expression pattern

        while pthXpr!='':                             # traverse path expression, filtering the list of all paths by the current component of the path expression

            if  pthXpr.startswith('..'):              # match all => keeping going, no paths filtered out

                pthXpr = pthXpr[2:]

            else:                                     # match string => no paths filtered out

                if '.' in pthXpr:                     # keep traversing path expression
                    splitPoint = pthXpr.index('.')
                    mtchElm, pthXpr = pthXpr[:splitPoint], pthXpr[splitPoint:]
                    if mtchElm.startswith('~'):
                        pthLst = [ p for p in pthLst if not any([ fnmatch(e, mtchElm[1:]) for e in p.split('.') ]) ]
                    else:
                        pthLst = [ p for p in pthLst if     any([ fnmatch(e, mtchElm)     for e in p.split('.') ]) ]

                elif pthXpr.startswith('='):          # path expression ends with a value-match predicate
                    mtchElm, pthXpr = pthXpr, ''
                    if mtchElm[1:].startswith('~'):
                        pthLst = [ p for p in pthLst if not fnmatch(str(self.evp(p)), mtchElm[2:]) ] # match path leaf value# use fnmatch.filter?
                    else:
                        pthLst = [ p for p in pthLst if     fnmatch(str(self.evp(p)), mtchElm[1:]) ] # match path leaf value# use fnmatch.filter?

                else:                                 # path expression ends with a value-match predicate
                    mtchElm, pthXpr = pthXpr, ''
                    if mtchElm.startswith('~'):
                        pthLst = [ p for p in pthLst if not fnmatch(p.split('.')[-1], mtchElm[1:]) ] # match path leaf # use fnmatch.filter?
                    else:
                        pthLst = [ p for p in pthLst if     fnmatch(p.split('.')[-1], mtchElm) ]     # match path leaf # use fnmatch.filter?

        return pthLst


    def pathRecurse(pthExpr):
        resLst = []
        for at in self.attrs_list():
            if   isinstance(atv := self.gav(at), Treacl): resLst += atv.pathRecurse(pthExpr, f'{cpth}.{at}')                   # recurse
            elif isinstance(atv, list) and any([isinstance(e, Treacl) for e in atv]):
                for pth in [ e.pathRecurse(pthExpr, f'{cpth}.{at}[{ei}]') for ei,e in enumerate(atv) if isinstance(e, Treacl) ]: resLst += pth # keep collated list flat
            else: resLst += [f'{cpth}.{at}']


    def tree_to_json(self, depth=0, file=sys.stdout, maxDepth=_ppMaxDepth):
        '''generate json version of the treacl structure
           delegating other datatypes to json.dumps() where possible'''
        if depth<maxDepth:
            print("{", file=file)
            for at in (atL := self.attrs_list()):                                             # same as self.__dict__:
                print(nameStr := (' ' * self._depthIndent * depth) + f' "{at}": ', end='', file=file)
                if isinstance(atv := self.gav(at), Treacl):
                    atv.tree_to_json(depth + 1, file=file, maxDepth=maxDepth)                 # recurse
                elif isinstance(atv, list) and any([isinstance(e, Treacl) for e in atv]):     # deeper nested lists are not checked
                    print("[", file=file)
                    for ate in atv:
                        ate.tree_to_json(depth + 1, file=file, maxDepth=maxDepth)             # recurse
                        if ate is not atv[-1]: print(",", file=file)
                    print("]", file=file)
                else:
                    try:    print(json.dumps(atv, indent=self._depthIndent * (depth+1)), file=file, end='') # use a to_json method if the datatype has one?
                    except: print(f'"{type(atv)}"', file=file, end='')
                if at is not atL[-1]: print(",", file=file)                                   # in json, no comma allowed after last item in dict or list
            print('}', file=file, end='')
        else:
            print('"elided..."', file=file)
        if depth==0: print(file=file)

    # def tree_find_paths_pathexex  # TBD extended path-expressions
    # def tree_diff(self, rhTree):  # compute difference between trees

    # --- graph traversal methods

    def ppgraph(self, depth=0, occurDict={}, sortedP=False, maxDepth=_ppMaxDepth):
        '''print treacl graph recursively'''                                              # print(' ' * self._depthIndent * depth+self.getProp("name"))
        occurDict[self] = True                                                            # TBD: by changing this to a counter, one could cycle up to a limit
        for at in self.attrs_list(sortedP=sortedP):                                       # TBD: if singleton, don't print a CRLF
            print()
            print(nameStr := ' ' * self._depthIndent * depth + f'{at}: ', end='')
            for atv in self.attr_get_aslist(at):                                          # deeper nested lists are not checked
                if isinstance(atv, Treacl):
                    if atv not in occurDict: atv.ppgraph(depth + 1, occurDict=occurDict, maxDepth=maxDepth)  # recurse
                else:
                    for s in self.pformat_indented(atv, len(nameStr)): print(s, end='')   # use pretty print to print python base datatype

    def graph_paths_to_list(self, varName="", occurDict={}):                              # list all paths in graph
        '''generate all paths to a given depth'''
        occurDict[self] = True
        resLst = []
        for at in self.attrs_list():
            resLst += [pth := f'{varName}.{at}']
            atv = self.gav(at)
            if isinstance(atv, Treacl):
                if atv not in occurDict: resLst += atv.graph_paths_to_list(pth, occurDict)# recurse
            elif isinstance(atv, list) and any([isinstance(e, Treacl) for e in atv]):     # n.b. more deeply nested lists are not checked
                for ei,e in enumerate(atv):
                    resLst += [lpth := f'{varName}.{at}[{ei}]']
                    if isinstance(e, Treacl):
                        if e not in occurDict: resLst += e.graph_paths_to_list(lpth, occurDict) # recurse
        return resLst

    def graph_nodes_to_list(self, occurDict={}):                                          # list all paths in graph
        '''return a list of all the nodes in the graph'''                                 # tbd make into a generator
        resLst = [self]
        occurDict[self] = True                                                            # a bit redundant to have both occurDict and resLstw
        for atvL in [ self.attr_get_aslist(at) for at in self.attrs_list() ]:             # iterate over attribute values: which could be (i) a Treacl instance, a list with maybe Treacl Instances, (iii) neither
            resLst += [ t for v in atvL if isinstance(v, Treacl) and v not in occurDict   # flattened list of lists
                             for t in v.graph_nodes_to_list(occurDict) ]
        return resLst

    def graph_find_paths(self, pattrn, depth=0, showValP=False):                          # list paths that match a pattern
        '''search graph recursively depth first
           find all paths with pattern matching
           anywhere in the path
        '''
        return [ p for p in self.graph_paths_to_list() if pattrn in p.split('.') ]

    def graph_find_paths_regex(self, regexPattrn, caseSensitive=re.I, depth=0, showValP=False):   # list paths that match a regex pattern
        '''search graph recursively depth first
           find all paths with pattern matching
           anywhere in the path
        '''
        lineRePat = re.compile(regexPattrn, re.I)
        return [ p for p in self.graph_paths_to_list() if lineRePat.search(p) ]

    def graph_save(self, fPath):
        '''super simple - save treacl graph/tree and all attached data using pickle'''
        with open(fPath,'wb') as f: pickle.dump(self, f)


# --- functions

def treacl_load(fPath):                                                                   # module function rather than class method, since it creates treacl instances
    '''super simple - load treacl graph/tree and all attached data using pickle'''
    with open(fPath, 'rb') as fb: return pickle.load(fb)

