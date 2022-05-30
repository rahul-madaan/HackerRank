"""
Given the position of a Bishop (A, B) on an 8 * 8 chessboard.

Your task is to count the total number of squares that can be visited by the Bishop in one move.

The position of the Bishop is denoted using row and column number of the chessboard.
"""
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        a1 = A-1
        a2 = 8-A
        b1 = B-1
        b2 = 8-B

        return min(a1,b1) + min(a1,b2) + min(a2,b1) + min(a2,b2)