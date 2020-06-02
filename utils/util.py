# supporting functions for treacl - things which are not naturally methods
from treacl import Treacl
# from uuid import uuid1

def paths_to_gml(nodes):
    ''' export data as directed graph in .gml graph format file
        https://gephi.org/users/supported-graph-formats/gml-format/
        gml likes list of all the nodes, then all of all the edges
      nodes: the list of treacl objects to be included in the export
    '''

    nodeDict = {n:ni for ni,n in enumerate(nodes)}                                               # index the nodes

    gmlLinesLst  =   {'G':['graph ['],
                      'N':[''],
                      'E':['']}
    gmlLinesLst['G'] +=  ['  comment "treacl tree converted to graph represented in gml"']
    gmlLinesLst['G'] +=  ['  directed 1']
    gmlLinesLst['G'] +=  ['  id 42']
    gmlLinesLst['G'] +=  ['  label "Graph of Treacl objects"']

    valId = 10000

    for ni,n in enumerate(nodes):

        gmlLinesLst['N'] +=  [f'node [id {ni}  label "node {ni}"  sampleAttrib "{str(n)[:10]}" ]']

        for l in n.attrs_list():
            if isinstance(atvL := n.attr_getl(l), list) and any([isinstance(e, Treacl) for e in atvL]): # n.b. deeper nested lists are not checked
                for e in atvL:
                    if isinstance(e, Treacl): gmlLinesLst['E'] += [f'edge [source {ni}  target {nodeDict[e]}  label "{l}" ]']
                    else: valId, gmlLinesLst = paths_to_gml_value(e, ni, l, valId, gmlLinesLst)  # not a treacl object
            else: valId, gmlLinesLst = paths_to_gml_value(atvL, ni, l, valId, gmlLinesLst)       # not a treacl object

    return gmlLinesLst['G'] + gmlLinesLst['N'] + gmlLinesLst['E'] + [']']

def paths_to_gml_value(e, ni, l, valId, linesLst):                                               # only
    valId += 1                                                                                   # uuid1().int>>96 # prefer to be less stateful than maintaing a counter
    v = str(e).replace("'","")
    linesLst['N'] += [f'node [id {valId}  label "v={v}" ]']                                      # extra node for the value
    linesLst['E'] += [f'edge [source {ni}  target {valId}  label "{l}" ]']
    return valId, linesLst

# def treacl_nodeify_links(nodes, links):
#     '''for each link of each node create a node'''
#     for n in nodes:
#         for l in n.attrs_list():
#             linkNode = t()
#             n.l = newNode
#             newNode.(l) = newNode
#
#
