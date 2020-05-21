from treacl import Treacl as t

# interactions of Physics' itty-bitty field-particles
# taken from (see the diagrams)
#  https://www.wikiwand.com/en/Standard_Model
#  https://www.theatlantic.com/technology/archive/2012/07/still-confused-about-the-higgs-boson-read-this/259472/
#  https://en.wikipedia.org/wiki/Spin_(physics)#/media/File:Standard_Model_of_Elementary_Particles.svg

# here the dot attributes are used to declare/encode two
# relationships: grouping and interaction
#  grouping/membership is declared via the ".M" attribute
#  interaction is declared         via the ".I" attribute

# some additional properties are separately recorded to illustrate using properties ("Treacl.__prop")
# since attributes are reserved to emphasize the main tree/graph structure

def standard_model_interactions():

    # elementary particles and their groupings
    ep = t();           ep.addProp('name', "elementary particles");   ep.addProp('type', "grouping")

    # fermions
    fm = t();           fm.addProp('name', "fermions");               fm.addProp('type', "grouping")
    # leptons
    lp = t();           lp.addProp('name', "leptons");                lp.addProp('type', "grouping")
    #  neutral leptons
    lpn = t();         lpn.addProp('name', "neutral leptons");       lpn.addProp('type', "grouping")
    en = t();           en.addProp('name', "electron neutrino");      en.addProp('type', "elementary")
    tn = t();           tn.addProp('name', "tau neutrino");           tn.addProp('type', "elementary")
    mnn = t();         mnn.addProp('name', "muon neutrino");         mnn.addProp('type', "elementary")
    lpn.M = [en, tn, mnn]
    #  charged leptons
    lpc = t();         lpc.addProp('name', "charged leptons");       lpc.addProp('type', "grouping")
    el = t();           el.addProp('name', "electron");               el.addProp('type', "elementary")
    tau = t();         tau.addProp('name', "tau");                   tau.addProp('type', "elementary")
    mn = t();           mn.addProp('name', "muon");                   mn.addProp('type', "elementary")
    lpc.M = [el, tau, mn]
    lp.M = [lpn, lpc]
    # quarks
    qk = t();           qk.addProp('name', "quarks");                 qk.addProp('type', "grouping")
    #  quarks up/down
    qkud = t();       qkud.addProp('name', "up/down quarks");       qkud.addProp('type', "grouping")
    qku = t();         qku.addProp('name', "up quark");              qku.addProp('type', "grouping")
    qkd = t();         qkd.addProp('name', "down quark");            qkd.addProp('type', "grouping")
    qkud.M = [qku, qkd]
    #  quarks charm/strange
    qkcs = t();       qkcs.addProp('name', "charm strange quarks"); qkcs.addProp('type', "grouping")
    qkc = t();         qkc.addProp('name', "charm quark");           qkc.addProp('type', "elementary")
    qks = t();         qks.addProp('name', "strange quark");         qks.addProp('type', "elementary")
    qkcs.M = [qkc, qks]
    #  quarks top/bottom
    qktb = t();       qktb.addProp('name', "top/bottom quarks");   qktb.addProp('type', "grouping")
    qkt = t();         qkt.addProp('name', "top quark");            qkt.addProp('type', "elementary")
    qkb = t();         qkb.addProp('name', "bottom quark");         qkb.addProp('type', "elementary")
    qktb.M = [qkt, qkb]
    qk.M = [qkud, qkcs, qktb]
    fm.M = [lp, qk]

    # bosons
    bn = t();           bn.addProp('name', "fermions");               bn.addProp('type', "grouping")
    # weak bosons
    wb = t();           wb.addProp('name', "weak bosons");            wb.addProp('type', "grouping")
    wp = t();           wp.addProp('name', "w-plus boson");           wp.addProp('type', "elementary")
    wm = t();           wm.addProp('name', "w-minus boson");          wm.addProp('type', "elementary")
    zb = t();           zb.addProp('name', "z boson");                zb.addProp('type', "elementary")
    wb.M = [wp, wm, zb]

    # gluon
    gn = t();           gn.addProp('name', "gluon");                  gn.addProp('type', "elementary")
    # photon
    ph = t();           ph.addProp('name', "photon");                 ph.addProp('type', "elementary")
    # higgs boson
    hg = t();           hg.addProp('name', "higgs");                  hg.addProp('type', "elementary")
    bn.M = [wb, gn, ph, hg]

    ep.M = [fm, bn] # currently, it seems the universe consists of bosons and fermions

    # Interactions
    # add both-ways links to identify which particles/ groups of particles interact
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

    # more properties
    # charge
    lpn.addProp('charge', '0')
    lpc.addProp('charge', '-1')
    qku.addProp('charge', '2/3')
    qkd.addProp('charge', '-1/3')
    qkc.addProp('charge', '2/3')
    qks.addProp('charge', '-1/3')
    qkt.addProp('charge', '2/3')
    qkb.addProp('charge', '-1/3')
    # spin
    ph.addProp('spin', '1/2')
    wb.addProp('spin', '1')
    gn.addProp('spin', '1')
    ph.addProp('spin', '1')
    hg.addProp('spin', '0')

    return ep   # all elementary particles


if __name__ == '__main__':

    sm = standard_model_interactions()

    sm.ppgraph()
    print()
    for p in sm.graph_paths_to_list(varName="sm"): print(p)
    print()






