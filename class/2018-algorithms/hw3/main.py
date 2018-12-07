#!/usr/bin/env python
# coding: utf-8

# Homework 3: MCM
# Given a chain of n matrices, find the optimal order to multiply them. In other words, fully parenthesize the product in a way that minimizes the number of scalar multiplications.
# 
# Input
# The first line of input contains the number of matrices n (1<=n<=100). The next line contains a space separated sequence of integers representing their dimensions: p0, p1, ... pn (1<=pi<=100). Here, pi-1 * pi is the dimension of the ith matrix.
# 
# Output
# Your program should print two lines. In the first line, output the minimum number of scalar multiplications required to compute the matrix chain product. In the second line, output the corresponding optimal parenthesization: use an integer i to denote the ith matrix in the sequence. Do not forget to print a newline, '\n', after the parenthesization. See the sample test cases for more details.
# 
# Note: none of our test cases has more than one optimal parenthesization.
# 

# In[81]:


# number of matrices
n = int(input())

# space separated sequence, representing dimensions
input2 = input()
dimensions = [int(n) for n in input2.split()]


# In[121]:


def multiply_matrixes(n, dimensions):
    matrix = [[None for i in range(n)] for i in range(n)]
    s = [[None for i in range(n)] for i in range(n)]
    
    for i in range(1,n):
        matrix[i][i]=0
        
    for l in range (2, n):
        for i in range(1, n-l+1):
            j = i + l -1
            matrix[i][j] = float("inf")
            
            for k in range(i, j):
                q = matrix[i][k] + matrix[k+1][j] + dimensions[i-1]*dimensions[k]*dimensions[j]
                
                if q < matrix[i][j]:
                    matrix[i][j] = q
                    s[i][j] = k
    return s, matrix

def print_optimal_parens(s, i, j):
    if i==j:
        print(i, end="")
    else:
        print('(', end="")
        print_optimal_parens(s, i, s[i][j]) 
        print_optimal_parens(s, s[i][j]+1, j) 
        print(')', end="")


# In[122]:


s, matrix = multiply_matrixes(n+1, dimensions)

print(matrix[1][n])

print_optimal_parens(s, 1, n)
print('\n', end="")


# In[ ]:




