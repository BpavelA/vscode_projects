d = {}

counter = 1

n = ['Скотнов', 'Иванов', 'Скотнов']

for i in n:
    if i not in d:
        d[i] = counter
    else:
        d[i + str(counter)] = counter

    counter += 1

print(d)

