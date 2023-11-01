from treacl import Treacl as t
import pickle
import utils.util as ut

# a plain simple configuration example


def sample_config():

    config = t()
    config.boo = 1
    config.bar.alpha = 11
    config.bar.beta = 22
    config.bar.gamma = 'hello'
    config.bas.rock = 'bye'
    config.bas.scissors = 'hello'
    config.bas.paper = ['hh', 'ii', 'jj']
    config.cas = [[1, 2],
                  [3, 4],
                  [5, 6]]
    config.dct = {'aa':11,'bb':22,'cc':33}
    config.a.b.c.d.e.f.mtx = [[42,43,44],[11,22,33]]
    config.a.b.c.d.e.f.g.h.i.j = 42
    config.a.b.c1 = 42
    config.a.b.c.d1 = 42
    config.a.b.c.d2.e = 42
    config.a.b.c.d3 = 42
    config.a.b.c2.d1 = 42
    config.a.b.c2.d2 = 42
    config.a.bb.c.d1 = 42
    config.a.bbb.c.d1 = 42
    # config.dag = config.bar      # this works, but creates a DAG
    # config.a.b.c.cyc = config  # this works, but creates a Cyclic Graph
    return config

if __name__ == '__main__':

    cfg = sample_config()
    print("sample config:pretty print config tree")
    cfg.pptree()

    print()
    print("Sample config: enumerated list of all paths")
    for p in cfg.tree_paths_to_list("cfg"): print(p) # "cfg"

    print()
    print("Sample config: filter list of paths")
    for p in cfg.tree_find_paths("e", "cfg"): print(p)

    print()
    print("Sample config: regex filter list of paths")
    for p in cfg.tree_find_paths_regex(".+e.+", "cfg"): print(p)

    #print()
    #print("Sample config: path expression filter list of paths")
    #for p in cfg.tree_find_paths_pathex("a.*.c.*", "cfg"): print(p)

    with open("./tests/configuration.gml",'w') as f:
        asGml = ut.paths_to_gml(cfg.tree_nodes_to_list())
        for l in asGml: print(l, file=f)
    for l in asGml: print(l)

    with open("./tests/configuration.pk",'wb') as f:
        pickle.dump(cfg, f)

    print()


