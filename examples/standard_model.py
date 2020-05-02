from treacl import Treacl as tcl

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





