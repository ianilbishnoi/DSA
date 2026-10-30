class Solution:
    def rowWithMax1s(self, mat):
        row = -1
        maximum = 0

        for i in range(len(mat)):
            count = 0

            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    count += 1

            if count > maximum:
                maximum = count
                row = i

        return row
