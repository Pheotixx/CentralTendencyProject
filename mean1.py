import csv

with open ('height-weight.csv', newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)
    
file_data.pop(0)
new_Data=[]

for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_Data.append(float(n_num))

n = len(new_Data)
total = 0

for x in new_Data:
    total += x

mean = total/n

print("The average is " + str(mean))

for i in range(len(file_data)):
    n_num = file_data[i][2]
    newData.append(float(n_num))

n = len(newData)
newData.sort()

if n % 2 == 0:
    median1 = float(newData[n//2])
    median2 = float(newData[n//2 - 1])
    median = (median1 + median1)/2

else:
    median = newData[n//2]
    print(n)

print("Median is " + str(median))
