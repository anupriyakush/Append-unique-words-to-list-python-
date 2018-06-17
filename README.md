# Append-unique-words-to-list-python-
Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order. You can download the sample data at http://www.py4e.com/code3/romeo.txt

fname = input("Enter file name: ")
fileread1 = open(fname)

#fileread1 = open('C:/Users/anupriyakushwanshi/Desktop/usb/text1.txt', 'r')
filename = fileread1.read()
list1 = list()

list2 = filename.split()
length1 = len(list2)
for i in range(0,int(length1)):

    while list2[i] not in list1:

        list1.append(list2[i])

list1.sort()
print(list1)

#Desired output
#['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']
