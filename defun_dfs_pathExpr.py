    # def tree_find_paths_pathex2(self, pthExpr, curPth=".", greedyFlg=False):       # list paths that match a path-expression pattern
    #     '''search tree depth first to find all paths with simple glob-like pattern matching path-expression
    #          e.g in path-expression "..",                => all paths
    #          e.g in path-expression "..xyz..",           => all paths containing "xyx" as a path member
    #          e.g in path-expression "..xpz",             => all paths with leaves xyz
    #          e.g in path-expression "xx.*yy",  the "*yy" => any attribute ending in "yy"
    #          e.g in path-expression "xx.yy*",  the "yy*" => any attribute beginning with "yy"
    #          e.g in path-expression "xx.*.yy", the "*"   => any attribute or list element
    #     '''
    #     # TBD bfs vs dfs
    #     #
    #     resLst = []
    #     print('pathExpr', pthExpr)
    #     if pthExpr:
    #         curAttrs = self.attrs_list()
    #         if len(pthExpr)==0:
    #             pass
    #         elif pthExpr="..":
    #             for at in curAttrs:
    #                 e.tree_find_paths_pathex2(pthExpr, curPth+"."+at)  # "propagate wild card"
    #         elif pthExpr.startswith(".") and len(pthExpr)==1:
    #             pth = f'{varName}.{at}'
    #             if includePartMatch: resLst += [pth]
    #             if isinstance(atv := getattr(self, at), Treacl):
    #                 resLst += atv.tree_find_paths_pathex2(pathCdr, pth)                    # recurse
    #             elif isinstance(atv, list) and any([isinstance(e, Treacl) for e in atv]): # deeper nested lists are not checked
    #                 for ei,e in enumerate(atv):
    #                     lpth = f'{varName}.{at}[{ei}]'
    #                     if includePartMatch: resLst += [lpth]
    #                     if isinstance(e, Treacl): resLst += e.tree_find_paths_pathex2(pathCdr, lpth)  # recurse
    #     return resLst
