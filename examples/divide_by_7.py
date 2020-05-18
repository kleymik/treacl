from treacl import Treacl as t

# a directed graph example
# graph traversal divisible-by-7 test
# traversing this graph computes whether a number if divisble by 7
#   i.e. f(n) = {n mod 7 == 0}
# FROM: http://blog.tanyakhanova.com/2009/divisibilty-by-7-is-a-walk
#   T. Khovanova & D. Wilson
#   Each node as two directed links: a "B" (Black) link and a "W" (White) link
#   the recipe indicates whether and how many time to follow the B link or the W link,
#   depending on the given digit in the number. If traversal returns to initial
#   node after traversing the graph with all the digits in the number, then
#   the number is divisble by 7.
#
#   The 1st function (divisible_by_7_graph) creates the graph by naming each node and
#   using these node name to specifiy the "B" and "W" links between them
#
#   The 2nd function divisible_by_7_graph_pathex) creates the graph wiithout needing
#   to name the nodes, the various paths are declared until all the links in the
#   graph have been specified. Though it is only a bit more succinct, it demonstrates
#   specifying a graph without having to resort to exogenous naming of the nodes.

def divisible_by_7_graph():
    '''set up divisibe-by-y graph by declaration
       of named nodes
    '''

    allNodes = { e: t() for e in "abcdefg" }                                                # create 7 alphabetically labelled nodes
    #             Black Links                      White Links
    allNodes['a'].B = allNodes['b']; allNodes['a'].W = allNodes['a']; allNodes['a'].v = 'a' # node 'a' has a self loop
    allNodes['b'].B = allNodes['c']; allNodes['b'].W = allNodes['d']; allNodes['b'].v = 'b'
    allNodes['c'].B = allNodes['d']; allNodes['c'].W = allNodes['g']; allNodes['c'].v = 'c'
    allNodes['d'].B = allNodes['e']; allNodes['d'].W = allNodes['c']; allNodes['d'].v = 'd'
    allNodes['e'].B = allNodes['f']; allNodes['e'].W = allNodes['f']; allNodes['e'].v = 'e' # same destination node for Black and for White
    allNodes['f'].B = allNodes['g']; allNodes['f'].W = allNodes['b']; allNodes['f'].v = 'f'
    allNodes['g'].B = allNodes['a']; allNodes['g'].W = allNodes['e']; allNodes['g'].v = 'g'

    return allNodes['a']


def divisible_by_7_graph_pathex():
    '''set up divisibe-by-y graph by declaration of links
       This graph is identical to that of the function above,
       but expressed by decomposing it into a set of line path expressions
    '''

    g7 = t()
    g7.B.B.B.B.B.B.B = g7         # Black loop
    g7.W = g7                     # a; White forward and backward jumps
    g7.B.W = g7.B.B.B             # b
    g7.B.B.W = g7.B.B.B.B.B.B     # c
    g7.B.B.B.W = g7.B.B           # d
    g7.B.B.B.B.W = g7.B.B.B.B.B   # e
    g7.B.B.B.B.B.W = g7.B         # f
    g7.B.B.B.B.B.B.W = g7.B.B.B.B # g

    return g7

def test_divisible_by_7(testNum, g7graph):
    '''traverse graph to test if divisible by 7'''
    nxt = g7graph
    for d in [int(d) for d in str(testNum)]:      # convert the integer to a list of digits
        for i in range(d): nxt = nxt.B            # for digits "d" times, move along BLACK edges; print(f"{d} {i}"); print("B",end='')
        nxt = nxt.W                               # then complete by one step along WHITE edge, repeat until all digits processed; print("W",end='')
    return (nxt is g7graph)                       # is divisible by 7 if back at start


if __name__ == '__main__':

    g7 = divisible_by_7_graph()
    g7.ppgraph(sortedP=True)
    for num in [5, 7, 77, 78, 37237366262681625, 37237366262681627]:
        print(f"\n{num}-----{num%7}")
        if test_divisible_by_7(num, g7): print("Divisible by 7")
        else:                            print("Not divisible by 7")

    g7c = divisible_by_7_graph_pathex()
    g7c.ppgraph(sortedP=True)
    for num in [5, 7, 77, 78, 37237366262681625, 37237366262681627]:
        print(f"\n\n{num}-----{num%7}")
        if test_divisible_by_7(num, g7c): print("Divisible by 7")
        else:                             print("Not divisible by 7")







