from treacl import Treacl as tcl

def standard_model_interactions():

    # interactions of Physics' itty-bitty particles
    # https://www.wikiwand.com/en/Standard_Model
    # https://www.theatlantic.com/technology/archive/2012/07/still-confused-about-the-higgs-boson-read-this/259472/
    # https://en.wikipedia.org/wiki/Spin_(physics)#/media/File:Standard_Model_of_Elementary_Particles.svg

    photon = tcl()
    leptons = tcl()           # a grouping
    higgs_boson = tcl()
    gluon = tcl()
    electron,          tau,          muon          = tcl(), tcl(), tcl()
    electron_neutrino, tau_neutrino, muon_neutrino = tcl(), tcl(), tcl()

    up_quark,      down_quark   = tcl(), tcl()
    strange_quark, charm_quark  = tcl(), tcl()
    top_quark,     bottom_quark = tcl(), tcl()

    Wplus_boson, Wminus_boson, Z_boson = tcl(), tcl(), tcl()

    # add pairs of of links to identify which particles/ groups of particles interact

    # example of adding a property: spin quantum number
    photon.addProp('spin', 'one')
    electron.addProp('spin', 'half')
    quarks.addProp('spin', 'half')
    higgs_boson.addProp('spin', 'zero')

    leptons.M = [photon] # .M for members of a grouping
    photon.I             # .I for interacts with, hence must be declared in both directions

    return photon   # all nodes are linked return one to retrun them all



if __name__ == '__main__':

    sm = standard_model_interactions():

    sm.printGraph()

    sm.to_dot() # export in .dot graph format

    print("test: find Paths")
    for p in univ.findPaths("lead"): print(p)






