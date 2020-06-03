# supporting functions for treacl - things which are not naturally methods
from treacl import Treacl
# from uuid import uuid1

def paths_to_gml(nodes):
    ''' export data as directed graph in .gml graph format file
        https://gephi.org/users/supported-graph-formats/gml-format/
        gml likes list of all the nodes, then all of all the edges
      nodes: the list of treacl objects to be included in the export
    '''

    nodeDict = {n:ni for ni,n in enumerate(nodes)}                                        # index the nodes

    gmlLinesLst  =   {'G':['graph ['],                                                    # gml graph pre-amble: properties of the graph
                      'N':[''],                                                           # gml nodes section: properties of the graph
                      'E':['']}                                                           # gml edges section: properties of the edges
    gmlLinesLst['G'] +=  ['  comment "treacl tree converted to graph represented in gml"']
    gmlLinesLst['G'] +=  ['  directed 1']
    gmlLinesLst['G'] +=  ['  id 42']
    gmlLinesLst['G'] +=  ['  label "Graph of Treacl objects"']

    valId = 10000

    for ni,n in enumerate(nodes):

        gmlLinesLst['N'] +=  [f'node [id {ni}  label "node {ni}"  sampleAttrib "{str(n)[:10]}" ]']

        for l in n.attrs_list():
            for e in n.attr_get_aslist(l):                                                # return value as a singleton list, unless it already a list (of Treacl objects)
                if isinstance(e, Treacl):
                    gmlLinesLst['E'] += [f'edge [source {ni}  target {nodeDict[e]}  label "{l}" ]']
                else:
                    valId += 1                                                            # uuid1().int>>96 # prefer to be less stateful than maintaing a counter
                    v = str(e).replace("'","")
                    gmlLinesLst['N'] += [f'node [id {valId}  label "{v}" ]']              # extra node for the value
                    gmlLinesLst['E'] += [f'edge [source {ni}  target {valId}  label "{l}" ]']


    return gmlLinesLst['G'] + gmlLinesLst['N'] + gmlLinesLst['E'] + [']']

# def treacl_nodeify_links(nodes, links):
#     '''for each link of each node create a node'''
#     for n in nodes:
#         for l in n.attrs_list():
#             linkNode = t()
#             n.l = newNode
#             newNode.(l) = newNode
#
#
