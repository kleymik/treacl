#
#  treacl.py
#
# Treacl - Tree Class - fun exploiting dynamic attibutes in python
#
# 2018-06-02 kleymik  - derivative of very similar datatypes by myself and others

import re
from pprint import pformat
from textwrap import indent

class Treacl(object):
    ''' Treacl: a tree class'''

	# attribute manipulation

    def __getattr__(self, name):
        '''only called for undefined attributes'''
        setattr(self, name, vdd := Treacl())                      # I am the walrus
        return vdd

    def delBranch(self, pthLst):                                  # TBD: traverses path, then deletes branch, pruning on the way back up
        if self.hasattr(pthLst[0]):                               # maybe not needed a.b.c = None
            delbranch(self, pth[1:])
            delattr()


	# a bit of support for treacl node properties
	
    tProps = {"long_name":None, "type":None}                      # Treacl "user" properties instead of attributes - see README explanation

    def addProp(self, pName, value):
		tProps[pName] = value
        return value
	
    def getProp(self, pName, value):
		try:
			return tProps[pName]
		except AttributeError:
			print('No %s property' % pName)


	# some basic traversal methods
	
    searchMaxDepth = 10_000_000                                   # in case of cycles: limit any search
    ppIndent = 4                                                  # indent for tree printing
	
    def pptree(self, depth=0):
        '''print tree recursively'''
        for at in self.__dict__:                                  # tbd: if singleton, don't print a CRLF
            atv = getattr(self, at)                               # attribute value
            if isinstance(atv, Treacl):
                print(' ' * depth, f'{at}: ')
                atv.pptree(depth + self.ppIndent)                 # recurse
            else:
                print(' ' * depth, f'{at}= ', end='')
                print(pformat(atv))                               # tbd: keep indent even if multi-line
                # print(indent(pformat(atv),' '*depth))
                # g1 = pformat(atv)
                # pdb.set_trace()
                # ilines = indent(pformat(atv).splitlines(True),' '*depth)
                # for l in ilines: print('X', l)

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
    def ppgraph(self, depth=0):                                   # same as pptree, but with occurs-check
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







