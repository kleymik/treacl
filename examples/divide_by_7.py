from treacl import Treacl as t

# a directed graph example
# graph traversal divisible by 7 test
# traversing this graph computes whether a number if divisble by 7
#   i.e. f(n) = {n mod 7 == 0}
# FROM: http://blog.tanyakhanova.com/2009/divisibilty-by-7-is-a-walk
#   T. Khovanova & D. Wilson
#   Each node as two directed links: a "B" (Black) link and a "W" (White) link
#   the recipe indicates whether and how many time to follow B or W link,
#   depending on the given digit in the number. If traversal returns to initial
#   node after traversing the graph with all the digits in the number then
#   the number is divisble by 7
#
#   The first function creates the graph by naming each node and
#   using these node name  to specifiy the "B" and "W" links between them
#
#   The second function creates the graph wiithout needing to name the nodes,
#   the various paths are declared until all the links in the graph have been
#   specified. Though it is only a bit more succinct, it demonstrates
#   specifying a graph without having to resort to exogenous naming of the nodes.

def divisible_by_7_graph():
    '''set up divisibe-by-y graph by declaration
       of named nodes
    '''
    allNodes = { e: t() for e in "abcdefg" }                          # create 7 alphabetically labelled nodes
    #             Black Links                      White Links
    allNodes['a'].B = allNodes['b']; allNodes['a'].W = allNodes['a'] ; allNodes['a'].v = 'a' # node a has a self loop
    allNodes['b'].B = allNodes['c']; allNodes['b'].W = allNodes['f'] ; allNodes['b'].v = 'b'
    allNodes['c'].B = allNodes['f']; allNodes['c'].W = allNodes['d'] ; allNodes['c'].v = 'c'
    allNodes['d'].B = allNodes['a']; allNodes['d'].W = allNodes['g'] ; allNodes['d'].v = 'd'
    allNodes['e'].B = allNodes['d']; allNodes['e'].W = allNodes['b'] ; allNodes['e'].v = 'e'
    allNodes['f'].B = allNodes['g']; allNodes['f'].W = allNodes['c'] ; allNodes['f'].v = 'f'
    allNodes['g'].B = allNodes['e']; allNodes['g'].W = allNodes['e'] ; allNodes['g'].v = 'g'  # same for Black and White ;

    return allNodes['a']


def divisible_by_7_graph_compact():
    '''set up divisibe-by-y graph by declaration of links
       This graph is identical to that of the function above,
       but expressed by decompositing into a set of line path expressions
    '''

    a = t(); a.v ='a'
    b = t(); b.v ='b'
    c = t(); c.v ='c'
    d = t(); d.v ='d'
    e = t(); e.v ='e'
    f = t(); f.v ='f'
    g = t(); g.v ='e'

    g7 = a                     # the starting node of the graph
    g7.W = g7                  #   i) self cycle  a->a White
    g7.B = b
    g7.B.B = c
    g7.B.W = f
    g7.B.B.B = f
    g7.B.B.W = d
    g7.B.B.B.B = g
    g7.B.B.B.B.B = e
    g7.B.B.B.B.W = e
    g7.B.B.B.B.B.B = d
    g7.B.B.B.B.B.W = b

    g7.B.B.B.B.B.B.B = g7
    g7.W = g7.B                 # a
    g7.B.W = g7.B.B.B           # f
    g7.B.B.W = g7.B.B.B.B.B.B   # d
    g7.B.B.B.W = g7.B.B         # c
    g7.B.B.B.B.W = g7.B.B.B.B.B # e
    g7.B.B.B.B.B.W = g7.B       # b
    g7.B.B.B.B.B.B.W = g7.B.B.B.B # g
    # g7.B.B.W.B = g7            #  ii) outer cycle a->b->c->d->a Black
    # g7.B.W. B.B.B = g7.B.B.W    # iii) inner cycle a->b->f->g->e->d Black
    # g7.B.W.B.W.W = g7.B        #  iv) single link e->b White
    # g7.B.B.B = g7.B.W          #   v) single link c->f Black
    # g7.B.W.W = g7.B.B          #  vi) single link f->c White
    # g7.B.W.B.B.B.W = g7.B.W.B  # vii) single link d->g White

    return g7

def test_divisible_by_7(testNum, g7graph):            # is this divisible by 7?):

    nxt = g7graph
    print()
    for d in [int(d) for d in str(testNum)]: # convert the integer to a list of digits
        for i in range(d):                   # print(f"{d} {i}")
            nxt = nxt.B                      # for digits "d" times, move along BLACK edges
            # print("B",end='')
        nxt = nxt.W                          # then complete by one step along WHITE edge, repeat until all digits processed
        #print("W",end='')

    print()
    if nxt is g7graph: print("Divisible by 7")  # back at start?
    else:              print("Not Divisible by 7")

if __name__ == '__main__':

    g7 = divisible_by_7_graph()
    g7.ppgraph(sortedP=True)
    for v in [77]: #[5, 7, 77, 78, 37237366262681625, 37237366262681627]:
        test_divisible_by_7(v, g7)
        print(f"{v}-----{v%7}")

    g7c = divisible_by_7_graph_compact()
    g7c.ppgraph(sortedP=True)
    for v in [77]: # [5, 7, 77, 78, 37237366262681625, 37237366262681627]:
        test_divisible_by_7(v, g7c)
        print(f"{v}-----{v%7}")





