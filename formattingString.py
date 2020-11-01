def print_formatted(number):
    number = int(number) 
    # Gets the number of characters of the binary representation of "number".
    # This is needed to format the strings latter on 
    w = len(bin(number)[2:])  

    # Loop through 1 through numbers inclusive.
    # Set i to all numbers.
    # the first colum is set to str so it follows the right decimal aligment. 
    # Transform i into Ocatal, Hexadecimal (capitalized) and bynary.
    # Right align everything with a space according to the width of the binary value
    # " [2:] "  - gets rid of undesired characters #zh #0O #0b

    for i in range(1, number + 1): 
        print(str(i)            .rjust(w, ' '),
              oct(i)[2:]        .rjust(w, ' '),
              hex(i).upper()[2:].rjust(w, ' '), 
              bin(i)[2:]        .rjust(w, ' '))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
