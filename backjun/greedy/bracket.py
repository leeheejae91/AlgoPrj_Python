reg = '55-50+40'
sub = reg.split('-')
result = []
for i in sub:
    if '+' in i:
        result.append(sum([int(j) for j in i.split('+')]))
    else:
        result.append(int(i))

for i in range(1,len(result)):
    result[i] *= -1

print(sum(result))