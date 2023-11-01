#!/usr/bin/python3
"""
This module provides a function to perform matrix multiplication using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Returns:
        np.ndarray: Result of matrix multiplication.
    Raises:
        ValueError: If matrices are not valid for multiplication.
    """
    # Use NumPy's matmul function to perform matrix multiplication
    result = np.matmul(m_a, m_b)
    return (result)
