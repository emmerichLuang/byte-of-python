
def get_max(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''

    if x > y:
        return x
    elif x == y:
        return 'the same'
    else:
        return y


print(get_max.__doc__)
print(get_max(199, 200))
print(get_max(200, 200))

