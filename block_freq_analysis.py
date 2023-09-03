
""" At the end, it's just a substitution cipher, so it's weak to frequency analysis.
If we encode B = 2, O = 15, N = 14, A = 1, J = 10, O = 15, U = 21, R = 18,
then BONJOUR = 021 514 011 015 21 18.
We would need to create blocks like 0215 1401 1015 2118, and we encrypt one block.

The purpose of this section is to break down a list [012, 345, 678, 910]
into a list [0123, 4567, 8910].
To do this, we use lists of lists where each element is a digit.
This allows us to write 012 instead of 12 to create blocks of equal size."""

def nbr_counter(n_nbr):
    "Compute how big is the number: How many digits"
    count = 0
    n_tmp = n_nbr
    while n_tmp >= 1:
        count += 1
        n_tmp = n_tmp/10
    return count

def max_digits(lis):
    "Compute the max digits needed to encrypt a message"
    length = len(lis)
    lis_tmp = []
    for i in range(length):
        lis_tmp.append(nbr_counter(lis[i]))
    return max(lis_tmp)

def decompose_rec(nbr):
    "Returns a list with all the digits of the number"
    if nbr == 0:
        return []
    else :
        quot = nbr//10
        rest = nbr%10
        lis = decompose_rec(quot)
        return lis + [rest]

def list_of_list(lis):
    "The structure is a list of list which represent a character"
    lis_tmp = []
    length = len(lis)
    for i in range(length):
        lis_tmp.append(decompose_rec(lis[i]))
    return lis_tmp

def listecomplete(lis):
    "Complete the final list with enough 0"
    lis_tmp = list_of_list(lis)
    max_dig = max_digits(lis)
    length = len(lis)
    for i in range(length):
        count = len(lis_tmp[i])
        while count != max_dig:
            lis_tmp[i] = [0] + lis_tmp[i]
            count = len(lis_tmp[i])
    return lis_tmp

def nbr_characters(lis):
    "Return how many letters encrypt there are"
    length = len(lis)
    siz = 0
    for i in range(length):
        siz += len(lis[i])
    return siz


def size_new_block(lis):
    "Compute the new size of the block"
    lis_tmp = listecomplete(lis)
    old_size = nbr_characters(lis_tmp)
    new_size = len(lis_tmp[0]) + 1
    while old_size%new_size != 0:
        new_size += 1
    return new_size

def list_modified(lis):
    "Modify the block of the list"
    lis_tmp = listecomplete(lis)
    new_size = size_new_block(lis)
    length = len(lis_tmp)
    for i in range(length-1):
        j = len(lis_tmp[i])
        while j != new_size:
            lis_tmp[i].append(lis_tmp[i+1][0])
            del lis_tmp[i+1][0]
            j = len(lis_tmp[i])
    del lis_tmp[-1] #normalement dernier element est la liste vide
    return lis_tmp

def size_old_block(lis):
    "Compute the size of the old block"
    siz = nbr_characters(lis)
    old_size = len(lis[0])-1
    while siz%old_size != 0:
        old_size -= 1
    return old_size

def list_of_list_of_original(lis):
    "Compute the original list"
    old_size = size_old_block(lis)
    length = len(lis)
    lis.append([])
    for i in range (length):
        j = len(lis[i])
        while j != old_size:
            lis[i+1] = [lis[i][-1]] + lis[i+1]
            del lis[i][-1]
            j = len(lis[i])
    return lis

def decrypt(lis):
    "Return the number from the list"
    original_number = 0
    length = len(lis)
    for i in range(length):
        original_number += lis[i]*10**(length-1-i)
    return original_number

def list_original(lis):
    "Compute the original list"
    lis_tmp = []
    length = len(lis)
    for i in range(length):
        lis_tmp.append(decrypt(lis[i]))
    return lis_tmp
