from copy import deepcopy


def sum_multiples(input, input2):
    print ("Second grid:")
    for row in input2:
       print str(row)
    total = 0
    for i in range(0, 6):
        for j in range(0,6):
            total = total + (input[i][j] * input2[i][j])
    return total


def rotate(matrix):
    n = len(matrix)
    x = n/2
    y = n - 1
    for i in range (0,x):
        for j in range (i, y - i):
            k = matrix[i][j];
            matrix[i][j] = matrix[y - j][i];
            matrix[y - j][i] = matrix[y - i][y - j];
            matrix[y - i][y - j] = matrix[j][y - i]
            matrix[j][y - i] = k

    return matrix


def flip_horiz(matrix):
    new = deepcopy(matrix)
    for i in range (0,6):
        for j in range (0,6):
            new[i][j] = matrix[i][5-j]

    return new


def flip_vert(matrix):
    new = deepcopy(matrix)
    for i in range (0,6):
        for j in range (0,6):
            new[i][j] = matrix[5-i][j]

    return new


def print_totals(input, input2):
    print "Total            : " + str(sum_multiples(input, input2)) + "\n"
    print "Flip horiz total : " + str(
        sum_multiples(input, flip_horiz(input2))) + \
          "\n"
    print "Flip vert total  : " + str(sum_multiples(input, flip_vert(input2))) + \
          "\n"

    print ("----------------------")


input = []
for i in range(0,6):
    row = []
    for j in range(1,7):
        value = i * 6 + j
        row.append(value)

    input.append(row)

input2 = deepcopy(input)

print ("No rotation:\n")
print_totals(input, input2)

input2 = rotate(input2)
print ("Rotated 90:\n" )
print_totals(input, input2)

input2 = rotate(input2)
print ("Rotated 180:\n")
print_totals(input, input2)

input2 = rotate(input2)
print ("Rotated 270:\n")
print_totals(input, input2)


