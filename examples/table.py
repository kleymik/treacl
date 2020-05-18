from treacl import Treacl as t
from string import ascii_lowercase
import pickle

# use of a treacl dag to create an indices-oriented table
#

def print_treacl_table(tbl):
    for ai,a in enumerate(tbl.rows):
        for bi,b in enumerate(tbl.cols): print(f"[{ai},{bi}]={tbl.rows[ai].s[bi].v} ", end='')
        print()
    print()

def make_treacl_3x2_table():
    '''example 3x2 table
    '''
    tbl = t()
    tbl.rows = [ t(), t(), t()]                             # i.e. [ row1, row2, row3] = list of row series
    tbl.cols = [ t(), t() ]                                 # i.e. [ col1, col2 ]      = list of column series
                                                            # put elements in row series (i.e. ".s")
    tbl.rows[0].s = [t(), t()]                              # a b
    tbl.rows[1].s = [t(), t()]                              # c d
    tbl.rows[2].s = [t(), t()]                              # e f
                                                            # put *same* elements in column series (i.e. ".s")
    tbl.cols[0].s = [tbl.rows[0].s[0], tbl.rows[1].s[0], tbl.rows[2].s[0]] # a c e
    tbl.cols[1].s = [tbl.rows[0].s[1], tbl.rows[1].s[1], tbl.rows[2].s[1]] # b d f
                                                            # give each element in the table a value attribute (e.g. ".v" )
    tbl.rows[0].s[0].v = "a"; tbl.rows[0].s[1].v = "b"
    tbl.rows[1].s[0].v = "c"; tbl.rows[1].s[1].v = "d"
    tbl.rows[2].s[0].v = "e"; tbl.rows[2].s[1].v = "f"

    return tbl


def make_treacl_table(nrows, ncols):
    '''example nR X nC table
    '''
    tbl = t()
    tbl.rows = [t() for _ in range(nrows)]                  # list of row series
    tbl.cols = [t() for _ in range(ncols)]                  # list of column series
    for r in tbl.rows: r.s = [t() for x in tbl.cols]        # create series treacl instances for each row
    for ci,c in enumerate(tbl.cols): c.s = [r.s[ci] for r in tbl.rows] # cross-ref the instance into column series

    i = 0
    for ri,r in enumerate(tbl.rows):
        for ci,c in enumerate(tbl.cols):
            tbl.rows[ri].s[ci].v = ascii_lowercase[i%26]  #(ri,ci)                  # give each element in the table a value attribute (e.g. ".v" )
            i += 1
    return tbl


if __name__ == '__main__':

    print("Sample table using treacl:")
    tbA = make_treacl_3x2_table()
    print_treacl_table(tbA)
    print()

    # transpose
    print("Sample table: transpose")
    tbA.rows, tbA.cols = tbA.cols, tbA.rows                                  # does what it says on the tin!
    print_treacl_table(tbA)
    print()

    # n x m table
    print("Sample table: 5x3")
    tbB = make_treacl_table(5,3)
    print_treacl_table(tbB)
    print()

    print("Sample table: 5x3 - swap a pair of horizontal neighbours ")       # both swap lines are needed to avoid making table strcuture inconsistent
    tbB.rows[1].s[1], tbB.rows[1].s[2] = tbB.rows[1].s[2], tbB.rows[1].s[1]  # swap in the one row    series
    tbB.cols[1].s[1], tbB.cols[2].s[1] = tbB.cols[2].s[1], tbB.cols[1].s[1]  # swap in the two column series
    print_treacl_table(tbB)
    print()
    print("Sample table: 5x3 - swap a pair of vertical neighbours ")         # both swap lines are needed to avoid making table strcuture inconsistent
    tbB.rows[0].s[0], tbB.rows[1].s[0] = tbB.rows[1].s[0], tbB.rows[0].s[0]  # swap in the one row    series
    tbB.cols[0].s[0], tbB.cols[0].s[1] = tbB.cols[0].s[1], tbB.cols[0].s[0]  # swap in the two column series
    print_treacl_table(tbB)
    print()

    f = open("./tests/table.pk",'wb')
    pickle.dump([tbA, tbB], f)
    f.close()
    print()
    print("Done")
