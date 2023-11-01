from treacl import Treacl as t
import utils.util as ut

# interactions of Physics' itty-bitty field-particles
# taken from (see the diagrams)
#  https://www.wikiwand.com/en/Standard_Model
#  https://www.theatlantic.com/technology/archive/2012/07/still-confused-about-the-BEH-boson-read-this/259472/
#  https://en.wikipedia.org/wiki/Spin_(physics)#/media/File:Standard_Model_of_Elementary_Particles.svg

# here the dot attributes are used to declare/encode two
# relationships: grouping and interaction
#  grouping/membership is declared via the ".M" attribute
#  interaction is declared         via the ".I" attribute

# some additional properties are separately recorded to illustrate using properties ("Treacl.__prop")
# since attributes are reserved to emphasize the main tree/graph structure

def standard_model_interactions():

    # elementary particles and their groupings
    ep = t();           ep.name = "elementary particles";   ep.setProp('type', "grouping")

    # fermions
    fm = t();           fm.name = "fermions";               fm.setProp('type', "grouping")
    # leptons
    lp = t();           lp.name = "leptons";                lp.setProp('type', "grouping")
    #  neutral leptons
    lpn = t();         lpn.name = "neutral leptons";       lpn.setProp('type', "grouping")
    en = t();           en.name = "electron neutrino";      en.setProp('type', "elementary")
    tn = t();           tn.name = "tau neutrino";           tn.setProp('type', "elementary")
    mnn = t();         mnn.name = "muon neutrino";         mnn.setProp('type', "elementary")
    lpn.M = [en, tn, mnn]
    #  charged leptons
    lpc = t();         lpc.name = "charged leptons";       lpc.setProp('type', "grouping")
    el = t();           el.name = "electron";               el.setProp('type', "elementary")
    tau = t();         tau.name = "tau";                   tau.setProp('type', "elementary")
    mn = t();           mn.name = "muon";                   mn.setProp('type', "elementary")
    lpc.M = [el, tau, mn]
    lp.M = [lpn, lpc]
    # quarks
    qk = t();           qk.name = "quarks";                 qk.setProp('type', "grouping")
    #  quarks up/down
    qkud = t();       qkud.name = "up/down quarks";       qkud.setProp('type', "grouping")
    qku = t();         qku.name = "up quark";              qku.setProp('type', "grouping")
    qkd = t();         qkd.name = "down quark";            qkd.setProp('type', "grouping")
    qkud.M = [qku, qkd]
    #  quarks charm/strange
    qkcs = t();       qkcs.name = "charm strange quarks"; qkcs.setProp('type', "grouping")
    qkc = t();         qkc.name = "charm quark";           qkc.setProp('type', "elementary")
    qks = t();         qks.name = "strange quark";         qks.setProp('type', "elementary")
    qkcs.M = [qkc, qks]
    #  quarks top/bottom
    qktb = t();       qktb.name = "top/bottom quarks";   qktb.setProp('type', "grouping")
    qkt = t();         qkt.name = "top quark";            qkt.setProp('type', "elementary")
    qkb = t();         qkb.name = "bottom quark";         qkb.setProp('type', "elementary")
    qktb.M = [qkt, qkb]
    qk.M = [qkud, qkcs, qktb]
    fm.M = [lp, qk]

    # bosons
    bn = t();           bn.name = "fermions";               bn.setProp('type', "grouping")
    # weak bosons
    wb = t();           wb.name = "weak bosons";            wb.setProp('type', "grouping")
    wp = t();           wp.name = "w-plus boson";           wp.setProp('type', "elementary")
    wm = t();           wm.name = "w-minus boson";          wm.setProp('type', "elementary")
    zb = t();           zb.name = "z boson";                zb.setProp('type', "elementary")
    wb.M = [wp, wm, zb]

    # gluon
    gn = t();           gn.name = "gluon";                  gn.setProp('type', "elementary")
    # photon
    ph = t();           ph.name = "photon";                 ph.setProp('type', "elementary")
    # BEH boson
    hg = t();           hg.name = "BEH";                    hg.setProp('type', "elementary")
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

    # more properties
    # charge
    lpn.setProp('charge', '0')
    lpc.setProp('charge', '-1')
    qku.setProp('charge', '2/3')
    qkd.setProp('charge', '-1/3')
    qkc.setProp('charge', '2/3')
    qks.setProp('charge', '-1/3')
    qkt.setProp('charge', '2/3')
    qkb.setProp('charge', '-1/3')
    # spin
    wb.setProp('spin', '1')
    gn.setProp('spin', '1')
    ph.setProp('spin', '1')
    hg.setProp('spin', '0')

    return ep   # all elementary particles


if __name__ == '__main__':

    sm = standard_model_interactions()

    print()
    sm.ppgraph()

    print()
    with open("./tests/standard_model.gml",'w') as f:
        asGml = ut.paths_to_gml(sm.graph_nodes_to_list())
        for l in asGml: print(l, file=f)
    # for l in asGml: print(l)






