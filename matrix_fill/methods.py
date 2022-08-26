def matrix_fill_spiral(size_row: int, size_col: int = None):
    assert size_row > 0, 'I cannot fill a matrix with rows smaller than 1'
    if size_col is None:
        size_col = size_row
    assert size_col > 0, 'I cannot fill a matrix with cols smaller than 1'
    matrix = [[False for _ in range(size_row)] for _ in range(size_col)]
    way_row = [0, 1, 0, -1]
    way_col = [1, 0, -1, 0]
    x = y = step = 0
    for index in range(1, size_row * size_col + 1):
        matrix[x][y] = index
        row = x + way_row[step]
        col = y + way_col[step]
        if (0 <= row and row < size_row
                and 0 <= col and col < size_col
                and matrix[row][col] is False):
            x = row
            y = col
        else:
            step = (step + 1) % 4
            x += way_row[step]
            y += way_col[step]
    return matrix
