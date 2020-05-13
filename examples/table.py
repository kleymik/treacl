from treacl import Treacl as t

# quirky use of a treacl dag to create a table

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

    for ri,r in enumerate(tbl.rows):
        for ci,c in enumerate(tbl.cols):
            tbl.rows[ri].s[ci].v = (ri,ci)                  # give each element in the table a value attribute (e.g. ".v" )
    return tbl


def make_treacl_symmatrix(nrows, ncols):
    '''a symmetric marix as a table: corresponding off-diagonal items
       are not just equal "(m[i,j]==m[j,i])==True", they are the
       same "(m[i,j] is m[j,i])==True".
    '''
    tbl = t()
    tbl.rows = [t() for _ in range(nrows)]                  # list of row series
    tbl.cols = [t() for _ in range(ncols)]                  # list of column series
    for ri,r in tbl.rows:
        for ci,c in enumerate(tbl.cols): tbl.rows[ri].s[ci] = tbl.cols[ci].s[ri] = t()
    return tbl
    # for r in tbl.rows: r.s = [t() for x in tbl.cols]
    # for ci,c in enumerate(tbl.cols): c.s = [ t for t in tbl.rows[ci]]


if __name__ == '__main__':

    print("Samples tables using treacl:")

    tb1 = make_treacl_3x2_table()
    print_treacl_table(tb1)

    # transpose
    tb1.rows, tb1.cols = tb1.cols, tb1.rows  # does what it says on the tin!
    print("transposed")
    print_treacl_table(tb1)

    # n x m table
    tb2 = make_treacl_table(5,3)
    print_treacl_table(tb2)
    # swap a pair of neighbouring column elements
    # tbl.rows[0].s[1], tbl.cols[1].s[2] = tbl.rows[0].s[1], tbl.cols[0].s[2]
    # swap a pair of neighbouring row  elements

