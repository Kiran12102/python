file_in=open('C:\\Users\\kiran\\Desktop\\practice\\oop\\letter.txt')


data=file_in.read()

len(data)

for var in range(len(data)-1,-1,-1):
	print(data[var],end='')

count=1
for var in range(len(data)):
        if data[var]==' ':
                count+=1

print(f'\n the number of word in sentence is {count}')

file_in.close

