from typing import Type, TypeVar, List

K = TypeVar('K', int, float)

def Inverse(cls: Type['Matrix[K]']) -> Type['Matrix[K]']:
    
    def inverse(self) -> 'Matrix[K]':
        if not self.is_square():
            raise ValueError("Only square matrices are invertible")
        
        n = self.row_count
        # Create augmented matrix [A | I]
        augmented = []
        for i in range(n):
            row = []
            # Copy original matrix A
            for j in range(n):
                row.append(self.matrix[i][j])
            # Add identity matrix
            for j in range(n):
                row.append(1.0 if i == j else 0.0)
            augmented.append(row)
        
        aug_matrix = cls(augmented)
        
        # Gaussian elimination to get [I | A⁻¹]
        for col in range(n):
            # Partial pivoting
            pivot_row = col
            for i in range(col + 1, n):
                if abs(aug_matrix.matrix[i][col]) > abs(aug_matrix.matrix[pivot_row][col]):
                    pivot_row = i
            
            if aug_matrix.matrix[pivot_row][col] == 0:
                raise ValueError("Matrix is singular and not invertible")
            
            # Swap rows if needed
            if pivot_row != col:
                aug_matrix.swap_rows(col, pivot_row)
            
            # Normalize pivot row
            pivot_val = aug_matrix.matrix[col][col]
            for j in range(2 * n):
                aug_matrix.matrix[col][j] /= pivot_val
            
            # Eliminate other rows
            for i in range(n):
                if i != col:
                    factor = aug_matrix.matrix[i][col]
                    for j in range(2 * n):
                        aug_matrix.matrix[i][j] -= factor * aug_matrix.matrix[col][j]
        
        # Extract inverse from right half
        inverse_data = []
        for i in range(n):
            inverse_row = []
            for j in range(n, 2 * n):
                inverse_row.append(aug_matrix.matrix[i][j])
            inverse_data.append(inverse_row)
        
        return cls(inverse_data)
    
    if not hasattr(cls, "inverse"):
        setattr(cls, "inverse", inverse)
    
    return cls