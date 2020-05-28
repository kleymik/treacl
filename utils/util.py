# supporting functions for treacl - which are not naturally methods
from treacl import Treacl


def paths_to_gml(nodes):
    ''' export data as directed graph in dot/dotty/graphviz  graph format file
    nodes: the list of treacl objects to be included in the export
    '''
    nodeDict = {n:ni for ni,n in enumerate(nodes)}   # index the nodes

    outStr =   ['graph [']
    outStr +=  ['  comment "This is a sample graph"']
    outStr +=  ['  directed 1']
    outStr +=  ['  id 42']
    outStr +=  ['  label "Hello, I am a graph"']
    outStr +=  ['']

    for ni,n in enumerate(nodes):
        outStr +=  ['node [']
        outStr +=  [f'   id {ni}']
        outStr +=  [f'   label "node {ni}"']
        outStr +=  ['   thisIsASampleAttribute "foobar"']
        outStr +=  ['     ]']
        for l in n.attrs_list():
            tgt = getattr(n, l)
            if isinstance(tgt, Treacl) and tgt in nodeDict:
                outStr += ['edge [']
                outStr += [f'    source {ni}']
                outStr += [f'    target {nodeDict[tgt]}']
                outStr += [f'    label "Edge from {ni} to {nodeDict[tgt]}"]']
                outStr += [     ']']
        outStr +=  ['']
    outStr +=  [']']

    for l in outStr: print(l)

# graph [
#   comment "This is a sample graph"
#   directed 1
#   id 42
#   label "Hello, I am a graph"
#   node [
#       id 1
#       label "node 1"
#       thisIsASampleAttribute 42
#   ]
#   node [
#       id 2
#       label "node 2"
#       thisIsASampleAttribute 43
#   ]
#   node [
#       id 3
#       label "node 3"
#       thisIsASampleAttribute 44
#   ]
#   edge [
#       source 1
#       target 2
#       label "Edge from node 1 to node 2"
#   ]
#   edge [
#       source 2
#       target 3
#       label "Edge from node 2 to node 3"
#   ]
#   edge [
#       source 3
#       target 1
#       label "Edge from node 3 to node 1"
#   ]
# ]

# "dot" format
# digraph {
#     a -> b[label="0.2",weight="0.2"];
#     a -> c[label="0.4",weight="0.4"];
#     c -> b[label="0.6",weight="0.6"];
#     c -> e[label="0.6",weight="0.6"];
#     e -> e[label="0.1",weight="0.1"];
#     e -> b[label="0.7",weight="0.7"];
# }


# #
# #  treacl.py
# #
# # Treacl - Tree Class - fun exploiting dynamic attibutes in Python
# #
# # 2018-06-02 kleymik  - yet another derivative of very similar tree/graph datatypes

# from collections.abc import Iterable

# treeMaxDepth = 10_000_000                                   # in case of cycles: limit any search
# depthIndent = 4                                             # indent for tree printing
#
# def treacl_pprint(node, depth=0):                            # not implemented as a method to allow pretty printer
#     '''print tree recursively'''                             # that recurses into non-treacl objects too
#     if isinstance(node, Treacl):
#         if depth < node.treeMaxDepth:
#             node.tprint(depth+1)
#             # print("AA")
#         else:
#             print("Max recursion depth reached %i", treeMaxDepth)
#     elif isinstance(node, str):
#         print(pformat(node))
#         # print("BB")
#     elif isinstance(node, Iterable):                    # but not a  string:
#         for e in node:
#             if isinstance(e, Treacl): node.tprint(depth + 1) # recurse
#             else:                     treacl_pprint(e, depth=depth+1)               # tbd: keep indent even if multi-line
#     else:
#         print(pformat(node), end='')
#
#
# def treacl_nodeify_links(nodes, links):
#     '''for each link of each node create a node'''
#     for n in nodes:
#         for l in n.attrs_list():
#             linkNode = t()
#             n.l = newNode
#             newNode.(l) = newNode
#
#
