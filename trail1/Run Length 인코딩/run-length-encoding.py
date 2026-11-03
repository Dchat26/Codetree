a = input().rstrip()

answer = ''
aval = ''
for i in a:
    if aval == '':
        aval += i
    elif aval[-1] != i:
        answer += aval[0] + str(len(aval))
        aval = i
    else:
        aval += i

answer += aval[0] + str(len(aval))

print(len(answer), answer, sep='\n')