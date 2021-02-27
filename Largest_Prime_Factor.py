def isPrime(number):
    """
    Return True if a number is Prime.
    Returns False otherwise.
    """
    if number <= 1:
        return False
    
    factors = [n for n in range(2, number) if number % n == 0]
        
    if len(factors) != 0:
        return False
        
    else:
        return True

    return True



def largest_factor(factor):
    """
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?

    """
    return max([num for num in range(1, factor) if (factor % num == 0) and (isPrime(num) == True)])
