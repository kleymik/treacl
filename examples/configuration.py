from treacl import Treacl as t
import pickle

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
    config.dag = config.bar  # this works, but creates a DAG
    config.a.b.c.cyc = config
    return config

if __name__ == '__main__':

    cfg = sample_config()
    print("sample config:pretty print config tree")
    cfg.pptree()

    #print("\nsample config: enumerated list of all paths")
    #for p in cfg.pathsToList("config"): print(p)

    print("Done")

    f = open("./config.pk",'wb')
    pickle.dump(cfg, f)
    f.close()

