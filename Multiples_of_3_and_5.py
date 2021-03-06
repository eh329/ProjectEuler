def multiples(a, b):
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 between a and b.
    """

    return sum([num for num in range(a, b + 1) if num % 3 == 0 and num % 5 == 0])
