#v.1.0
#Program for solving (simple) Sudokus by explicit application of rules
#
#
#made by J. Gehrig 14.08.2020
#

input = []

#input.append([1,0,0,4,5,6,7,8,9])
#input.append([2,8,7,6,5,4,3,2,1])
#input.append([3,2,3,4,5,6,7,8,9])
#input.append([4,8,7,6,5,4,3,2,1])
#input.append([5,2,3,4,5,6,7,8,9])
#input.append([6,8,7,6,5,4,3,2,1])
#input.append([7,2,3,4,5,6,7,8,9])
#input.append([8,8,7,6,5,4,3,2,1])
#input.append([9,2,3,4,5,6,7,8,9])

input.append([9,6,1,5,0,0,7,0,8])
input.append([0,0,0,9,1,0,5,6,0])
input.append([3,5,0,2,0,0,4,0,0])
input.append([8,9,2,0,0,1,0,0,0])
input.append([0,0,6,0,0,2,9,0,5])
input.append([0,0,0,0,9,7,2,8,6])
input.append([0,0,0,7,6,5,0,3,9])
input.append([6,3,0,0,0,0,0,5,7])
input.append([1,7,0,0,8,0,0,4,2])


numbers = (1,2,3,4,5,6,7,8,9)

def checker_row(r):
    return set(numbers) - set(input[r])

def checker_column(c):
    tmp = []
    for i in range(9):
        tmp.append(input[i][c])
    #print(tmp)         #DEBUG
    return set(numbers) - set(tmp)

def checker_square(r,c):
    sqr = int((float(r)+0.9)/3) #0-2: sqx=0 ; 3-5: sqx=1 ; 6-8: sqx=2
    sqc = int((float(c)+0.9)/3) #0-2: sqy=0 ; 3-5: sqy=1 ; 6-8: sqy=2

    #print(sqr,sqc)         #DEBUG
    list =  (0,1,2)
    tmpr = [l+(sqr*3) for l in list]    #brings 0,1,2 ; 3,4,5 ; 6,7,8 for 0;1;2
    tmpc = [l+(sqc*3) for l in list]

    #print(tmpr,tmpc)         #DEBUG
    tmp = []

    for i in tmpr:
        for j in tmpc:
            tmp.append(input[i][j])
    #print(tmp)         #DEBUG
    return set(numbers) - set(tmp)

def possibles(r,c):
    tmp1 = checker_row(r)
    tmp2 = checker_column(c)
    tmp3 = checker_square(r,c)
    #print(tmp1)         #DEBUG
    #print(tmp2)         #DEBUG
    #print(tmp3)         #DEBUG
    return tmp1.intersection(tmp2,tmp3)

def solver():
    for r in range(len(input[0])):
        #print(i)         #DEBUG
        for c in range(len(input[0])):
            #print(j)         #DEBUG


            if input[r][c] == 0:
                poss = list(possibles(r,c))
                if len(poss) == 1:
                    #print(poss)         #DEBUG
                    #print(len(poss),r,c)         #DEBUG
                    input[r][c] = poss[0]
    return 0


i = 0
print(input)
while i < 100:



    solver()
    print(i)
    print(input)
    i = i+1
