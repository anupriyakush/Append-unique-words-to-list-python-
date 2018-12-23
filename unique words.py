fname = 'C:/Users/anupr/.PyCharmCE2018.3/config/scratches/Append-unique-words-to-list-python-/Dataset.txt'
fileread1 = open(fname, 'r')


filename = fileread1.read()
list1 = list()

list2 = filename.split()
length1 = len(list2)
for i in range(0,int(length1)):

    while list2[i] not in list1:

        list1.append(list2[i])

list1.sort()
print(list1)