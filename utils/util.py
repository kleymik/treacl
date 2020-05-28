# supporting functions for treacl - which are not naturally methods
from treacl import Treacl

def paths_to_gml(nodes):
    ''' export data as directed graph in .gml graph format file
        https://gephi.org/users/supported-graph-formats/gml-format/
    nodes: the list of treacl objects to be included in the export
    '''
    nodeDict = {n:ni for ni,n in enumerate(nodes)}   # index the nodes

    outStrG =   ['graph [']
    outStrG +=  ['  comment "treacl tree converted to graph represented in gml"']
    outStrG +=  ['  directed 1']
    outStrG +=  ['  id 42']
    outStrG +=  ['  label "Graph of Treacl objects"']

    outStrN = []
    outStrE = []
    for ni,n in enumerate(nodes):
        outStrN +=  [f'node [id {ni}  label "node {ni}"  sampleAttrib "{str(n)}" ]']
        for li,l in enumerate(n.attrs_list()):
            atv = getattr(n, l)
            if isinstance(atv, Treacl):
                if atv in nodeDict:
                    outStrE += [f'edge [source {ni}  target {nodeDict[atv]}  label "{l}" ]']
            elif isinstance(atv, list) and any([isinstance(e, Treacl) for e in atv]):
                for e in atv:                                                         # note deeper nested lists are not checked
                    if isinstance(e, Treacl):
                        outStrE += [f'edge [source {ni}  target {nodeDict[e]}  label "{l}" ]']
                    else:
                        valId = (ni+1)*10000+(li+1)                          # not a treacl object
                        v = str(atv).replace("'","")
                        outStrN += [f'node [id {valId}  label "v={v}" ]']    # extra node for the value
                        outStrE += [f'edge [source {ni}  target {valId}  label "{l}" ]']

            else:
                valId = (ni+1)*10000+(li+1)                                  # not a treacl object
                v = str(atv).replace("'","")
                outStrN += [f'node [id {valId}  label "v={v}" ]']            # extra node for the value
                outStrE += [f'edge [source {ni}  target {valId}  label "{l}" ]']
    print('')
    for l in outStrG: print(l)
    print('')
    for l in outStrN: print(l)
    print('')
    for l in outStrE: print(l)
    print('')
    print(']')

    return outStrG + outStrN + outStrE+[']']

# def treacl_nodeify_links(nodes, links):
#     '''for each link of each node create a node'''
#     for n in nodes:
#         for l in n.attrs_list():
#             linkNode = t()
#             n.l = newNode
#             newNode.(l) = newNode
#
#
