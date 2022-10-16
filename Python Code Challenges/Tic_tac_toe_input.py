def get_row_col(Uinput):
    return (rows.index(Uinput[1]) , columns.index(Uinput[0]))

rows = ['1','2','3']
columns = ['A','B','C']

print(get_row_col("A3"))