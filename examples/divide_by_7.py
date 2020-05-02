def test_3_divide_by_7():
    # a directed graph example - divisible by 7
    allNodes = { e: tcl() for e in "abcdefg" }                        # create 7 alphabetically labelled nodes
    allNodes['a'].B = allNodes['b']; allNodes['a'].W = allNodes['a']  # node a has a self loop
    allNodes['b'].B = allNodes['c']; allNodes['b'].W = allNodes['f']
    allNodes['c'].B = allNodes['f']; allNodes['c'].W = allNodes['d']
    allNodes['d'].B = allNodes['a']; allNodes['d'].W = allNodes['g']
    allNodes['e'].B = allNodes['d']; allNodes['e'].W = allNodes['b']
    allNodes['f'].B = allNodes['g']; allNodes['f'].W = allNodes['c']
    allNodes['g'].B = allNodes['e']; allNodes['g'].W = allNodes['e']  # same for Black and White

    return allNodes['a']


def test_3_divide_by_7_compact():
    # a directed graph example - divisible by 7
    # this graph is identical to the one in test_3_div7 but expressed
    # by decomposition into a set of line path expressions
    # extra credit for a minimal set of line path expressions
    mod7 = tcl()              # the starting node of the graph
    mod7.W = mod7                #   i) self cycle  a->a White
    mod7.B.B.W.B = mod7          #  ii) outer cycle a->b->c->d->a Black
    mod7.B.W.B.B.B = mod7.B.B.W  # iii) inner cycle a->b->f->g->e->d Black
    mod7.B.W.B.W.W = mod7.B      #  iv) single link e->b White
    mod7.B.B.B = mod7.B.W        #   v) single link c->f Black
    mod7.B.W.W = mod7.B.B        #  vi) single link f->c White

    return mod7

def test_2_divisble_by_7():
    # a directed graph example
    # traversing this graph computes whether a number if divisble by 7, i.e. f(n) = {n mod 7 == 0}
    # see http://blog.tanyakhanova.com/2009/divisibilty-by-7-is-a-walk

    mod7 = test_3_div7()
    mod7 = test_3_div7_compact()

    testNum = 37237366262681625              # is this divisible by 7?

    for d in [int(d) for d in str(testNum)]: # convert the integer to a list of digits
        for _i in range(d): nxt = nxt.B      # for digits "d" times, move along BLACK edges
        nxt = nxt.W                          # then complete by one step along WHITE edge, repeat until all digits processed

    if nxt is mod7: print("Divisible by 7")  # back at start?
    else:           print("Not Divisible by 7")

def standard_model_interactions():

    # interactions of Physics' itty-bitty particles
    # https://www.wikiwand.com/en/Standard_Model
    # https://www.theatlantic.com/technology/archive/2012/07/still-confused-about-the-higgs-boson-read-this/259472/

    photon = tcl()

    leptons = tcl()

    higgs_boson = tcl()

    gluon = tcl()

    electron,          tau,          muon          = tcl(), tcl(), tcl()
    electron_neutrino, tau_neutrino, muon_neutrino = tcl(), tcl(), tcl()

    up_quark,      down_quark   = tcl(), tcl()
    strange_quark, charm_quark  = tcl(), tcl()
    top_quark,     bottom_quark = tcl(), tcl()

    Wplus_boson, Wminus_boson, Z_boson = tcl(), tcl(), tcl()

    return photon

def test_n_json():

    # json sample from json wikipedia page
    person = tcl()
    person.firstName = "Jonn"
    person.lastName  = "Smith"
    person.age       = 25
    person.address.streetAddress = "21 2nd Street"
    person.address.city          = "New York"
    person.address.state         =  "NY"
    person.address.postalCode    =  "10021"
    person.address.phoneNumbers  = [ tcl(), tcl() ]
    person.address.phoneNumbers[0].type   = "home"
    person.address.phoneNumbers[0].number = "212 555-1234"
    person.address.phoneNumbers[1].type   = "fax"
    person.address.phoneNumbers[1].number = "646 555-4567"
    person.sex.type = "male"

    # json form:
    # {
    #   "first name": "John",
    #   "last name": "Smith",
    #   "age": 25,
    #   "address": {
    #       "street address": "21 2nd Street",
    #       "city": "New York",
    #       "state": "NY",
    #       "postal code": "10021"
    #   },
    #   "phone numbers": [
    #       {
    #           "type": "home",
    #           "number": "212 555-1234"
    #       },
    #       {
    #           "type": "fax",
    #           "number": "646 555-4567"
    #       }
    #   ],
    #   "sex": {
    #       "type": "male"
    #   }
    # }

    # or similarly with XML, in XML-with-properties form:
    #
    # <person firstName="John" lastName="Smith" age="25">
    #   <address streetAddress="21 2nd Street" city="New York" state="NY" postalCode="10021" />
    #   <phoneNumbers>
    #     <phoneNumber type="home" number="212 555-1234"/>
    #     <phoneNumber type="fax" number="646 555-4567"/>
    #   </phoneNumbers>
    #   <sex type="male"/>
    # </person>


def test_pascal():

    a = tcl()
    a.setProp('num',1)
    a.l.parSum()

if __name__ == '__main__':

    test_1_config()

    test_2_universe()

    test_eg_3()

    print("test: find Paths")
    for p in univ.findPaths("lead"): print(p)

    if False:
        # path expressions
        config.findPaths("*")                    ## all paths
        config.findPaths("config*")              ## all paths starting "config"
        config.findPaths("*config")              ## all paths ending "config"
        config.findPaths("*config*")             ## all paths containing "config"
        config.findPaths("*config*bar*")         ## all paths containing "config" followed by "bar"
        config.findPaths("*[[A-Z]]*")            ## all paths containing regexp "[A-Z]"
        config.findPaths("*[[A-Z]]*")            ## all paths containing regexp "[A-Z]*"
        config.findPaths("*a:=config*a*")        ## all paths containing regexp "[A-Z]*"
        config.findPaths("*.config.*")           ## all paths with a branch exactly "config"
        config.findPaths("*ForAll().Exists*a*")  ## all paths containing regexp "[A-Z]*"

    print("Done")


    # univ.addProp('role','The Big One')





