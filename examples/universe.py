from treacl import Treacl as t

# silly example inspired by Charles Eames "Powers Of Ten"
# https://www.youtube.com/watch?v=0fKBhvDjuy0

def test_universe():
    univ = t()
    univ.virgoSuperCluster.localGroup.milkyWay.orionCygnusArm.sun.earth.europe.uk.england.london.marylebone.langhamHotel.bar.pint.londonPride.head.bubble.co2.oxygen.neutron.upQuark = None
    univ.virgoSuperCluster.localGroup.milkyWay.orionCygnusArm.sun.earth.europe.uk.oxfordshire.oxford = None
    univ.virgoSuperCluster.localGroup.milkyWay.orionCygnusArm.sun.earth.europe.france.languedoc.perpignan.gare = None
    univ.virgoSuperCluster.localGroup.milkyWay.orionCygnusArm.sun.earth.europe.france.paris.arrondisement5.placeDuPantheon.pantheon.dome.focaulPendulum.sphere.lead.faceCenteredCube.atomPb204.proton.quark = None
    univ.virgoSuperCluster.localGroup.milkyWay.orionCygnusArm.sun.earth.us.california.inyoCounty.whitemountains.ancientBristleconePineForest.methuselahGrove.methuselah.trunk.branch.fascile.needle.stoma.parenchymaCell = None
    univ.virgoSuperCluster.localGroup.milkyWay.orionCygnusArm.sun.earth.us.colorado.gaithersburg.nist.nistF1Clock.fountain.opticalMolasses.cesium133.groundState.hyperFineTransition.fluorescentPhoton.frequency = None
    univ.virgoSuperCluster.localGroup.milkyWay.orionCygnusArm.sun.mars.chrysePlanitia.viking1Lander.biologicalExperimentSystem.labeledRelease.c14DetectorAssembly = None
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

    test_universe()

    print("test: find Paths")
    for p in univ.findPaths("lead"): print(p)




