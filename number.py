import numpy as np
import math


class Numbers:
    ''' A simple class that contains numpy array with numbers of type
    32 bit integer
    Attributes:
        array(arr):
            A numpy array
    '''
    def __init__(self, values):
        self.array = np.array(values, dtype=np.int32)

    def __reduce__(self):
        ''' Method is called when unpickling of unknown data structure or class
        '''
        return (self.__class__, (self.values, ))


class NumberOperations:
    ''' A class to generate random natural number arrays and check if
    number(s) is(are) prime
    '''
    def generate_numbers(self, array_size, min_number, max_number):
        ''' Generates and sorts numpy array of random natural numbers
        Args:
            array_size(int):
                Required size of array
            min_number(int):
                The minimum number that an array can contain and
                it should be greater that 1
            max_number(int):
                The maximum number that an array can contain
        Returns:
            (arr):
                A sorted numpy array
        '''
        if min_number < 1:
            raise Exception("Cannot generate a non natural number")
        arr = np.random.randint(min_number, max_number,
                                array_size, dtype=np.int32)
        return np.sort(arr)

    def check_prime(self, num):
        ''' Checks if a number is prime
        Args:
            num (int):
                An integer that needs to be checked if it is prime
        Returns:
            (bool):
                Returns true of number is prime
        '''
        if num > 1:
            for i in range(2, math.floor(num/2)):
                if num % i == 0:
                    return False
            return True
        else:
            return False

    def find_primes(self, num_arr):
        ''' Finds all the prime numbers in an array.
        Args:
            num_arr (arr):
                A numpy array consisting of numbers
        Returns:
            (arr):
                An array of prime numbers
        '''
        prime_arr = np.array([], dtype=np.int32)
        for num in num_arr:
            if self.check_prime(num):
                prime_arr = np.append(prime_arr, num)
        return np.append(prime_arr, num)
