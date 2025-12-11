# file_path="example.txt"
# file=open(file_path,"r")
#
# content=file.read()
# print(content)
#
# file.close()
import os
# with open("example.txt","w") as file:
#     file.write('hello world')
#
# with open('example.txt','r') as file:
#     content=file.read()
#     line=file.readline()
#     lines=file.readLines()
#
# lines=['hello world\n','welcome to python\n']
# with open('example.txt','w') as file:
#     file.writelines(lines)
#
# with open('example.txt','r') as file:
#     file.seek(0)
#      data=file.read()
#      print(data)
#
# if os.path.exists('example.txt'):
#     print('file exists')
#
#
# with open('example.txt','a') as file:
#     file.write('new data append')

with open('example.txt',"r") as file:
    for line in file:
        cleaned_line=line.strip()
        print(cleaned_line)

with open('example.txt','r') as file:
    for line in file:
        words=line.strip().split()
        print(words)

name='alice'
age=30

with open('example.txt','w') as file:
    file.write('name:'+name+'\n')
    file.write('age:'+str(age)+'\n')

with open('example.txt','w') as file:
    file.write(f"name:{name}\n")
    file.write(f"age:{age}")








