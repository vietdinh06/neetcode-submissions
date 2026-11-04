class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix) - 1
        mid = -1
        while low <= high:
            mid = low + (high - low) // 2

            if target < matrix[mid][0]:
                high = mid - 1

            elif target > matrix[mid][-1]:
                low = mid + 1

            else:
                break

        low2, high2 = 0, len(matrix[mid]) - 1

        while low2 <= high2:
            mid2 = low2 + (high2 - low2) // 2

            if matrix[mid][mid2] < target:
                low2 = mid2 + 1

            elif matrix[mid][mid2] > target:
                high2 = mid2 -1
            
            else:
                return True
                        
        return False

        

