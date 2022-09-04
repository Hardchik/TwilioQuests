import sys

inputs = sys.argv
inputs.pop(0)

for i in inputs:
    i = int(i)
    if i % 15 == 0:
        print('fizzbuzz')
    elif i % 5 == 0: 
        print('buzz')
    elif i % 3 == 0: 
        print('fizz')
    else:
        print(i)        