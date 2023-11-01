from treacl import Treacl as t

# interactions of Physics' itty-bitty field-particles
# taken from (see the diagrams)
#  https://www.wikiwand.com/en/Standard_Model
#  https://www.theatlantic.com/technology/archive/2012/07/still-confused-about-the-BEH-boson-read-this/259472/
#  https://en.wikipedia.org/wiki/Spin_(physics)#/media/File:Standard_Model_of_Elementary_Particles.svg

# here the dot attributes are used to declare/encode two
# relationships: grouping and interaction
#  grouping/membership is declared via the ".M" attribute
#  interaction is declared         via the ".I" attribute

# additional properties are separately recorded in "Treacl._props"
# since attributes are reserved to emphasize the main tree/graph structure

def standard_model_interactions():

    # elementary particles and their groupings
    ep   = t(name="elementary particles", type="grouping")

    # fermions
    fm   = t(name="fermions",             type="grouping",   spin='1/2')
    # leptons
    lp   = t(name="leptons",              type="grouping")
    #  neutral leptons
    lpn  = t(name="neutral leptons",      type="grouping",   charge='0')
    en   = t(name="electron neutrino",    type="elementary")
    tn   = t(name="tau neutrino",         type="elementary")
    mnn  = t(name="muon neutrino",        type="elementary")
    lpn.M = [en, tn, mnn]
    #  charged leptons
    lpc  = t(name="charged leptons",      type="grouping",   charge='-1')
    el   = t(name="electron",             type="elementary")
    tau  = t(name="tau",                  type="elementary")
    mn   = t(name="muon",                 type="elementary")
    lpc.M = [el, tau, mn]
    lp.M = [lpn, lpc]
    # quarks
    qk   = t(name="quarks",               type="grouping")
    #  quarks up/down
    qkud = t(name="up/down quarks",       type="grouping")
    qku  = t(name="up quark",             type="grouping",   charge='2/3')
    qkd  = t(name="down quark",           type="grouping",   charge='-1/3')
    qkud.M = [qku, qkd]
    #  quarks charm/strange
    qkcs = t(name="charm strange quarks", type="grouping")
    qkc  = t(name="charm quark",          type="elementary", charge='2/3')
    qks  = t(name="strange quark",        type="elementary", charge='-1/3')
    qkcs.M = [qkc, qks]
    #  quarks top/bottom
    qktb = t(name="top/bottom quarks",    type="grouping")
    qkt  = t(name="top quark",            type="elementary", charge='2/3')
    qkb  = t(name="bottom quark",         type="elementary", charge='-1/3')
    qktb.M = [qkt, qkb]
    qk.M = [qkud, qkcs, qktb]
    fm.M = [lp, qk]

    # bosons
    bn   = t(name="bosons",               type="grouping")
    # weak bosons
    wb   = t(name="weak bosons",          type="grouping",   spin='1')
    wp   = t(name="w-plus boson",         type="elementary", spin='1')
    wm   = t(name="w-minus boson",        type="elementary", spin='1')
    zb   = t(name="z boson",              type="elementary", spin='1')
    wb.M = [wp, wm, zb]

    # gluon
    gn   = t(name="gluon",                type="elementary", spin='1')
    # photon
    ph   = t(name="photon",               type="elementary", spin='1')
    # BEH boson
    hg   = t(name="BEH",                  type="elementary", spin='0')
    bn.M = [wb, gn, ph, hg]

    ep.M = [fm, bn] # currently, it seems the universe consists of bosons and fermions

    # Interactions
    # add both-ways links to identify which particles/groups of particles interact
    # self interactions are inherently both-ways
    gn.I  = [gn, qk]
    ph.I  = [lpc, wp, wm, qk]
    hg.I  = [hg, wb, qk, lpc]
    wb.I  = [wb, hg, lp, qk]
    lp.I  = [wb]
    qk.I  = [gn, ph, hg, wb]
    lpc.I = [ph, hg]
    wp.I  = [ph]
    wp.I  = [ph]

    return ep   # all elementary particles


if __name__ == '__main__':

    sm = standard_model_interactions()

    sm.ppgraph()
    print()
    for p in sm.graph_paths_to_list(varName="sm"): print(p)
    print()






