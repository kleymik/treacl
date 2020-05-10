
# quirky use of a treacl dag to create a table

from treacl import Treacl as t

def print_treacl_table(tbl):
    for ai,a in enumerate(tbl.rows):
        for bi,b in enumerate(tbl.cols): print(f"[{ai},{bi}]={tbl.rows[ai].s[bi].v} ", end='')
        print()
    print()

def make_treacl_3x2_table():
    '''example 3x2 table
    '''
    tbl = t()
    tbl.rows = [ t(), t(), t()] # i.e. [ row1, row2, row3]
    tbl.cols = [ t(), t() ]     # i.e. [ col1, col2 ]
                                # put elements in row series (i.e. .s)
    tbl.rows[0].s = [t(), t()]  # a b
    tbl.rows[1].s = [t(), t()]  # c d
    tbl.rows[2].s = [t(), t()]  # e f
                                # put *same* elements in column series (i.e. ".s")
    tbl.cols[0].s = [tbl.rows[0].s[0], tbl.rows[1].s[0], tbl.rows[2].s[0]] # [e1 e3 e5]
    tbl.cols[1].s = [tbl.rows[0].s[1], tbl.rows[1].s[1], tbl.rows[2].s[1]] # [e2 e4 e6]
                                # give each element in the table a value attribute (i.e.".v" )
    tbl.rows[0].s[0].v = "a"
    tbl.rows[0].s[1].v = "b"
    tbl.rows[1].s[0].v = "c"
    tbl.rows[1].s[1].v = "d"
    tbl.rows[2].s[0].v = "e"
    tbl.rows[2].s[1].v = "f"

    return tbl

def make_treacl_table(nrows, ncols):
    '''example nRxnC table
    '''
    tbl = t()
    tbl.rows = [t() for i in range(nrows)]
    tbl.cols = [t() for i in range(ncols)]
    for r in tbl.rows: r.s = [t() for x in tbl.cols]
    for ci,c in enumerate(tbl.cols): c.s = [ t for t in tbl.rows[ci]]
    # for bi,b in enumerate(tbl.cols): tbl.rows[ai].s[bi] = tbl.rows[bi].s[ai] = t()

    return tbl

if __name__ == '__main__':

    tb1 = make_treacl_3x2_table()

    print_treacl_table(tb1)

    # transpose
    tb1.rows, tb1.cols = tb1.cols, tb1.rows  # does what it says on the tin!
    print("transposed")
    print_treacl_table(tb1)


#tbl.meta.rows[0].cell =

# for a,ai in emuerate(tbl.meta.rows):
#     for b,bi in enumerate(tbl.meta.cols):
#         tbl.meta.rows[ai][bi] = tbl.meta.rows[bi][ai] = t()

#         tbl.rows = [ r1, r2, r3]
# tbl.cols = [ c1, c2 ]

# r1.s = [e1 e2]
# r2.s = [e3 e4]
# r3.s = [e5 e6]

# c1.s = [e1 e3 e5]
# c2.s = [e2 e4 e6]

# tbl.meta.rows, tbl.meta.cols = tbl.meta.cols, tbl.meta.rows

# for a in tbl.meta.rows:
#     for b in tbl.meta.cols:
#         print a,b



