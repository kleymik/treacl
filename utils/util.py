# supporting functions for treacl - which are not naturally methods
from treacl import Treacl

def paths_to_gml(nodes):
    ''' export data as directed graph in .gml graph format file
        https://gephi.org/users/supported-graph-formats/gml-format/
    nodes: the list of treacl objects to be included in the export
    '''
    nodeDict = {n:ni for ni,n in enumerate(nodes)}   # index the nodes

    outStrG =   ['graph [']
    outStrG +=  ['  comment "This is a sample graph"']
    outStrG +=  ['  directed 1']
    outStrG +=  ['  id 42']
    outStrG +=  ['  label "Hello, I am a graph"']

    outStrN = []
    outStrE = []
    for ni,n in enumerate(nodes):
        outStrN +=  [f'node [id {ni}  label "node {ni}"  thisIsASampleAttribute "foobar" ]']
        for l in n.attrs_list():
            if isinstance(tgt := getattr(n, l), Treacl) and tgt in nodeDict: outStrE += [f'edge [source {ni}  target {nodeDict[tgt]}  label "{ni}->{nodeDict[tgt]}" ]']

    for l in outStrG: print(l); print('')
    for l in outStrN: print(l); print('')
    for l in outStrE: print(l); print(']')




# def treacl_nodeify_links(nodes, links):
#     '''for each link of each node create a node'''
#     for n in nodes:
#         for l in n.attrs_list():
#             linkNode = t()
#             n.l = newNode
#             newNode.(l) = newNode
#
#
