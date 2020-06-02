# supporting functions for treacl - things which are not naturally methods
from treacl import Treacl
from uuid import uuid1

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
    valId = 10000
    for ni,n in enumerate(nodes):

        gmlLinesLstN +=  [f'node [id {ni}  label "node {ni}"  sampleAttrib "{str(n)[:10]}" ]']

        for l in n.attrs_list():
            atvL = [atv] if isinstance(atv := getattr(n, l), Treacl) else atv
            if isinstance(atvL, list) and any([isinstance(e, Treacl) for e in atvL]):
                for e in atvL:                                                            # n.b. deeper nested lists are not checked
                    if isinstance(e, Treacl):
                        gmlLinesLstE += [f'edge [source {ni}  target {nodeDict[e]}  label "{l}" ]']
                    else:                                                                 # not a treacl object
                        valId += 1                                                        # uuid1().int>>96 # prefer to be less stateful than maintaining a counter?
                        v = str(e).replace("'","")                                        # gml can't handle nested quoting
                        gmlLinesLstN += [f'node [id {valId}  label "v={v}" ]']            # extra node for the value
                        gmlLinesLstE += [f'edge [source {ni}  target {valId}  label "{l}" ]']
            else:
                valId += 1                                                                # uuid1().int>>96; # prefer to be less stateful than maintaining a counter
                v = str(atvL).replace("'","")                                             # gml can't handle nested quoting
                gmlLinesLstN += [f'node [id {valId}  label "v={v}" ]']                    # extra node for the value
                gmlLinesLstE += [f'edge [source {ni}  target {valId}  label "{l}" ]']

    return gmlLinesLstG + gmlLinesLstN + gmlLinesLstE + [']']

def paths_to_gml_value(e, ni, l):                                                          # only
    valId = valId += 1                                                        # uuid1().int>>64 # prefer to be less stateful than maintaing a counter
    v = str(atv).replace("'","")
    gmlLinesLstN += [f'node [id {valId}  label "v={v}" ]']                    # extra node for the value
    gmlLinesLstE += [f'edge [source {ni}  target {valId}  label "{l}" ]']
    return valId, gmlLinesLstN, gmlLinesLstE

# def treacl_nodeify_links(nodes, links):
#     '''for each link of each node create a node'''
#     for n in nodes:
#         for l in n.attrs_list():
#             linkNode = t()
#             n.l = newNode
#             newNode.(l) = newNode
#
#
