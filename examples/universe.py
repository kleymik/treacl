from treacl import Treacl as tcl

def test_2_universe():
    # a bigger example: the universe
    univ = Treacl()
    univ.virgoSuperCluster.localGroup.milkyWay.orionCygnusArm.sun.earth.europe.uk.england.london.marylebone.langhamHotel.bar.pint.londonPride.bubble.co2.oxygen.neutron.upQuark = None
    univ.virgoSuperCluster.localGroup.milkyWay.orionCygnusArm.sun.earth.europe.uk.oxfordshire.oxford = None
    univ.virgoSuperCluster.localGroup.milkyWay.orionCygnusArm.sun.earth.europe.france.languedoc.perpignan.gare = None
    univ.virgoSuperCluster.localGroup.milkyWay.orionCygnusArm.sun.earth.europe.france.paris.arrondisement5.placeDuPantheon.pantheon.dome.focaulPendulum.sphere.lead.faceCenteredCube.atomPb204.proton.quark = None
    univ.virgoSuperCluster.localGroup.milkyWay.orionCygnusArm.sun.earth.us.california.inyoCounty.whitemountains.ancientBristleconePineForest.methuselahGrove.methuselah.trunk.branch.fascile.needle.stoma.parenchymaCell = None
    univ.virgoSuperCluster.localGroup.milkyWay.orionCygnusArm.sun.earth.us.colorado.gaithersburg.nist.nistF1Clock.fountain.opticalMolasses.cesium133.groundState.hyperFineTransition.fluorescentPhoton.frequency = None
    univ.virgoSuperCluster.localGroup.milkyWay.orionCygnusArm.sun.mars.chrysePlanitia.viking1Lander.biologicalExperiementSystem.labeledRelease.c14DetectorAssembly = None
    univ.virgoSuperCluster.localGroup.milkyWay.orionCygnusArm.sun.jupiter.ganymede.crater1 = None
    univ.virgoSuperCluster.localGroup.milkyWay.orionCygnusArm.sun.jupiter.bigRedSpot = None
    univ.virgoSuperCluster.localGroup.milkyWay.perseusArm.crabNebula = None
    univ.virgoSuperCluster.localGroup.milkyWay.sirius = None
    univ.virgoSuperCluster.localGroup.andromeda.mayaII = None
    univ.virgoSuperCluster.localGroup.andromeda.nucleues.p2.blackHole = None
    univ.virgoSuperCluster.localGroup.triangulum.inSpiral = None
    univ.virgoSuperCluster.localGroup.triangulum.isSpiral = None
    univ.virgoSuperCluster.localGroup.triangulum.ngc604 = None
    univ.virgoSuperCluster.localGroup.sextansA = None
    univ.virgoSuperCluster.localGroup.sextansB = None
    univ.virgoSuperCluster.virgoA.messier87 = None

    return univ


if __name__ == '__main__':

    test_1_config()

    test_2_universe()

    test_eg_3()

    print("test: find Paths")
    for p in univ.findPaths("lead"): print(p)

    if False:
        # path expressions
        config.findPaths("*")                    ## all paths
        config.findPaths("config*")                 ## all paths starting "config"
        config.findPaths("*config")                 ## all paths ending "config"
        config.findPaths("*config*")                ## all paths containing "config"
        config.findPaths("*config*bar*")            ## all paths containing "config" followed by "bar"
        config.findPaths("*[[A-Z]]*")            ## all paths containing regexp "[A-Z]"
        config.findPaths("*[[A-Z]]*")            ## all paths containing regexp "[A-Z]*"
        config.findPaths("*a:=config*a*")           ## all paths containing regexp "[A-Z]*"
        config.findPaths("*.config.*")              ## all paths with a branch exactly "config"
        config.findPaths("*ForAll().Exists*a*")  ## all paths containing regexp "[A-Z]*"

    print("Done")


    # univ.addProp('role','The Big One')





