file = open(r'C:\Users\kavin\Desktop\input-1.txt')
n=int(file.readline().split(':')[1])
file.readline()
file.readline()
file.readline()
arr = []
while(1):
    s = file.readline()
    if(not(s.endswith('\n'))):
        s = s+'\n'
    arr.append(s)
    if(arr[-1] == '\n'):
        break
arr.pop(-1)

def getint(s):
    e = s.split(': ')
    return int(e[1].split('\\')[0])

size = len(arr)
for i in range(size-1):
    for j in range(size-i-1):
        if(getint(arr[j])>getint(arr[j+1])):
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
ans = 0
min = 10000000000
for i in range(size-n-1):
    if (getint(arr[i+n-1]) - getint(arr[i]) < min):
        ans = i
        min = getint(arr[i+n-1]) - getint(arr[i])

print(ans)
res = 'The goodies selected for distribution are:\n\n'
for i in range(0,n):
    res = res + arr[i+ans]
res = res + '\nAnd the difference between the chosen goodie with highest price and the lowest price is {0}'.format(min)
output = open(r'C:\Users\kavin\Desktop\output-1.txt',"a")
output.write(res)
output.close()
file.close()
print(res)