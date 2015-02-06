# validating IP address

input1 = open("PracticeInput.txt", "r")
output1 = open("output.txt", "w")
test = []
matrix = [[],[],[]]
linestatus = ['InValid']


def compareTo(list1, list2):
    for i in range(0,len(list1)-1):
        if list1[i] == list2[i]:
            continue
        if list1[i] > list2[i]:
            return 1
        if list1[i] < list2[i]:
            return -1
    return 0


for line in input1:
    linestatus[0] = 'InRange'
    curr = line.rstrip("\n").split(" ")
    for i, elem in enumerate(curr):
        valid = True
        if not valid:
            break
        for j, digit in enumerate(elem.split(".")):
            if not valid:
                break
            try:
                digit = int(digit)
            except ValueError:
                linestatus[0] = "InValid"
                valid = False
                continue
            matrix[i].append([digit])
        lower = matrix[0]
        upper = matrix[1]
        test = matrix[2]
        if len(test) != 4:
            linestatus[0] = "InValid"
            valid = False
            continue
        if not (compareTo(matrix[0], matrix[2]) >= 0 and compareTo(matrix[1],matrix[2]) <= 0):
            linestatus[0] = "OutRange"
    matrix.clear()
    output1.write(linestatus[0]+"\n")


#                for y in IP:
#                    if int(y) not in range(256):
#                        print(y)
#                        linestatus[0] = "OutRange"
#                        break
##            else:
 #               linestatus[0] = 'InValid'
 #   else:
 #       linestatus[0] = 'InValid'
