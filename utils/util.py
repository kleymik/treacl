# supporting functions for treacl - things which are not naturally methods
from treacl import Treacl
import uuid import uuid1

def paths_to_gml(nodes):
    ''' export data as directed graph in .gml graph format file
        https://gephi.org/users/supported-graph-formats/gml-format/
    nodes: the list of treacl objects to be included in the export
    gml likes all nodes, then all edges
    '''

    nodeDict = {n:ni for ni,n in enumerate(nodes)}   # index the nodes

    gmlLinesLstG =   ['']
    gmlLinesLstG =   ['graph [']
    gmlLinesLstG +=  ['  comment "treacl tree converted to graph represented in gml"']
    gmlLinesLstG +=  ['  directed 1']
    gmlLinesLstG +=  ['  id 42']
    gmlLinesLstG +=  ['  label "Graph of Treacl objects"']

    gmlLinesLstN = ['']
    gmlLinesLstE = ['']
    for ni,n in enumerate(nodes):

        gmlLinesLstN +=  [f'node [id {ni}  label "node {ni}"  sampleAttrib "{str(n)}" ]']

        for li,l in enumerate(n.attrs_list()):
            atv = getattr(n, l)
            if isinstance(atv, Treacl):
                if atv in nodeDict:
                    gmlLinesLstE += [f'edge [source {ni}  target {nodeDict[atv]}  label "{l}" ]']
            elif isinstance(atv, list) and any([isinstance(e, Treacl) for e in atv]):
                for ei,e in enumerate(atv):                                               # note deeper nested lists are not checked
                    if isinstance(e, Treacl):
                        gmlLinesLstE += [f'edge [source {ni}  target {nodeDict[e]}  label "{l}" ]']
                    else:                                                                 # not a treacl object
                        valId = uuid1().int>>64                                           # prefer to be less stateful than maintaing a counter
                        v = str(atv).replace("'","")
                        gmlLinesLstN += [f'node [id {valId}  label "v={v}" ]']            # extra node for the value
                        gmlLinesLstE += [f'edge [source {ni}  target {valId}  label "{l}" ]']
            else:
                valId = uuid1().int>>64                                                   # prefer to be less stateful than maintaing a counter
                v = str(atv).replace("'","")
                gmlLinesLstN += [f'node [id {valId}  label "v={v}" ]']                    # extra node for the value
                gmlLinesLstE += [f'edge [source {ni}  target {valId}  label "{l}" ]']

    return gmlLinesLstG + gmlLinesLstN + gmlLinesLstE + [']']

# def paths_to_gml_value(atv, ni, l):                                                          # only
#         valId = uuid1().int>>64                                                   # prefer to be less stateful than maintaing a counter
#         v = str(atv).replace("'","")
#         gmlLinesLstN += [f'node [id {valId}  label "v={v}" ]']                    # extra node for the value
#         gmlLinesLstE += [f'edge [source {ni}  target {valId}  label "{l}" ]']
#         return gmlLinesLstN, gmlLinesLstE

# def treacl_nodeify_links(nodes, links):
#     '''for each link of each node create a node'''
#     for n in nodes:
#         for l in n.attrs_list():
#             linkNode = t()
#             n.l = newNode
#             newNode.(l) = newNode
#
#
