
class Matrix():
    '''
   A class to represent a matrix and perform calculations.
   
   ...
   
   Attributes
   ----------
   i: int
        A integer that represents the number of rows in the matrix. 
   j: int
        A integer that represents the number of columns in the matrix.
   values: list
        A list of values corresponding to the matrix values.
        The list should have i*j values. The values will fill
        the matrix from left to right from the first row onwards.
        
    Methods
    -------
    
    '''
    def __init__(self, i, j, values):
        '''
            Construct and verify the attributes of a matrix
            
            Parameters
            ----------
            i: int
                A integer that represents the number of rows in the matrix.
            j: int
                A integer that represents the number of columns in the matrix.
            values: list
                A list of values corresponding to the matrix values.
                The list should have i*j values. The values will fill
                the matrix from left to right from the first row onwards.
        '''
        self.i = i
        self.j = j
        assert i*j == len(values), "The dimensions and the number of values don't match"
        self.values = values
    
    def __add__(self, other):
        '''
            Function to add two matrices. The matrices must have the same dimensions
            Example:
                | 2  3 |   +  | 5  6 |  =  | 7  9 |
                | 4  5 |      | 7  8 |     |11  13|
            
            Parameters:
            -----------
                other (Matrix): Matrix instance
            
            Return:
            ------
                Matrix:
                    The result of the matrix sum
        '''
        
        assert (self.i == other.i) and (self.j == other.j), "The dimensions don't match"
        sum_values = [a+b for (a, b) in zip(self.values, other.values)]
        return Matrix(self.i, self.j, sum_values)
    
    def __sub__(self, other):
        '''
            Function to subtract two matrices. The matrices must have the same dimensions
            Example:
                | 2  3 |   -  | 7  8 |  =  |-5  -5|
                | 4  5 |      | 5  6 |     |-1  -1|
            
            Parameters:
            -----------
                other (Matrix): Matrix instance
            
            Return:
            ------
                Matrix:
                    The result of the matrix subtraction
        '''
        
        assert (self.i == other.i) and (self.j == other.j), "The dimensions don't match"
        sub_values = [a-b for (a, b) in zip(self.values, other.values)]
        return Matrix(self.i, self.j, sub_values)
    
    def __mul__(self, other):
        '''
            Function to multiply two matrices. 
            The first matrix column dimension must match the second matrix column dimension
            Example:
            
                |2  3  4|  x  |4  7  10| = |47  74   101|
                |5  6  7|     |5  8  11|   |92  146  200|
                              |6  9  12|
                              
                              
            Parameters:
            -----------
                other (Matrix): Matrix instance
            
            Return:
            ------
                Matrix:
                    The result of the matrix multiplication
            
        '''
        
        assert self.j == other.i, "The first matix's column size doesn't match the second matrix's row size"
        
        transposed_b = other.transpose()
        
        mult_values = []
        # First we iterate through the rows of the first matrix and save each row's elements
        for row_a in range(self.i):
            begin_a = row_a*self.j
            end_a = (row_a + 1)*self.j
            row_values = self.values[begin_a:end_a]
            # Second we iterate through the columns of the second matrix. It is the same thing as iterate through the
            # rows of its transpose.
            for transposed_row_b in range(transposed_b.i):
                begin_b = transposed_row_b*transposed_b.j
                end_b = (transposed_row_b + 1)*transposed_b.j
                columns_values = transposed_b.values[begin_b:end_b]
                
                # Finally we multiply element by element from the row and column and sum it to obtain the final result for the cell
                result = sum(list(map(lambda t: t[0]*t[1], zip(row_values, columns_values))))
                
                mult_values.append(result)
        
        return Matrix(self.i, other.j, mult_values)
        
        
    def transpose(self):
        '''
            Function to calculate the transpose of the matrix
            
            Parameters
            ----------
            None
            
            Returns
            -------
            Matrix:
                The transposed matrix
        '''
        
        transposed_values = [self.values[column + self.j*row] for column in range(self.j) for row in range(self.i)]    

        return Matrix(self.j, self.i, transposed_values)
     
        
    def __repr__(self):
        '''
            Function to output a visual representation of the matrix
            
            Parameters
            ----------
            None
                
            Returns
            -------
            output: str
                A string with the Matrix dimensions
        '''
        output = "\n"
        for row in range(self.i):
            begin = row*self.j
            end = (row + 1)*self.j
            output += "|" + "  ".join(list(map(str, self.values[begin:end]))) + "|\n"
        output += f"\nMatrix Dimensions: {self.i} x {self.j}"

        return output
        
        
        
        
        
        
        