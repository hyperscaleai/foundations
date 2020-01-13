class Solution:
    def findMedianSortedArrays(self, X: List[int], Y: List[int]) -> float:
        Nx, Ny = len(X), len(Y)
        if Nx > Ny: 
            Nx, Ny, X, Y = Ny, Nx, Y, X
            
        l, r = 0, Nx        
        while l <= r:
            xi = (l + r) // 2
            yi = (Nx + Ny + 1) // 2 - xi

            max_left_x = float('-inf') if xi == 0 else X[xi-1]
            min_right_x = float('inf') if xi == Nx else X[xi]

            max_left_y = float('-inf') if yi == 0 else Y[yi-1]
            min_right_y = float('inf') if yi == Ny else Y[yi]
            
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if (Nx+Ny) % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y))/2.0
                else:
                    return max(max_left_x, max_left_y)
            elif max_left_x > min_right_y:
                r = xi - 1
            else:
                l = xi + 1
                
