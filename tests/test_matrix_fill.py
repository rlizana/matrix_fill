import pytest

from matrix_fill.methods import matrix_fill_spiral


class TestMatrixFill():

    def test_fill_spiral_0x0(self):
        with pytest.raises(Exception):
            matrix_fill_spiral(0)
        with pytest.raises(Exception):
            matrix_fill_spiral(1, 0)

    def test_fill_spiral_2x2(self):
        matrix = matrix_fill_spiral(2)
        assert len(matrix[0]) == 2
        assert len(matrix) == 2
        must_be = [
            [1, 2],
            [4, 3],
        ]
        assert list(matrix) == must_be
        total = sum([i for i in range(1, 2 * 2 + 1)])
        assert sum([sum(m) for m in matrix]) == total

    def test_fill_spiral_3x3(self):
        matrix = matrix_fill_spiral(3)
        assert len(matrix[0]) == 3
        assert len(matrix) == 3
        must_be = [
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5],
        ]
        assert list(matrix) == must_be
        total = sum([i for i in range(1, 3 * 3 + 1)])
        assert sum([sum(m) for m in matrix]) == total

    def test_fill_spiral_5x5(self):
        matrix = matrix_fill_spiral(5)
        assert len(matrix[0]) == 5
        assert len(matrix) == 5
        must_be = [
            [1, 2, 3, 4, 5],
            [16, 17, 18, 19, 6],
            [15, 24, 25, 20, 7],
            [14, 23, 22, 21, 8],
            [13, 12, 11, 10, 9],
        ]
        assert list(matrix) == must_be
        total = sum([i for i in range(1, 5 * 5 + 1)])
        assert sum([sum(m) for m in matrix]) == total

    # def test_fill_spiral_5x3(self):
    #     matrix = matrix_fill_spiral(3, 2)
    #     assert len(matrix[0]) == 3
    #     assert len(matrix) == 2
    #     must_be = [
    #         [1, 2, 3],
    #         [6, 5, 4],
    #     ]
    #     assert list(matrix) == must_be
    #     total = sum([i for i in range(1, 5 * 3 + 1)])
    #     assert sum([sum(m) for m in matrix]) == total

    # def test_fill_spiral_5x3(self):
    #     matrix = matrix_fill_spiral(5, 3)
    #     assert len(matrix[0]) == 5
    #     assert len(matrix) == 3
    #     must_be = [
    #         [1, 2, 3, 4, 5],
    #         [11, 12, 13, 6],
    #         [10, 9, 8, 7],
    #     ]
    #     assert list(matrix) == must_be
    #     total = sum([i for i in range(1, 5 * 3 + 1)])
    #     assert sum([sum(m) for m in matrix]) == total
