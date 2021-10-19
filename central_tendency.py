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


for i in range(len(file_data)):
    n_num = file_data[i][2]
    newData.append(float(n_num))

data = Counter(newData)
modeData_for_range = {
                        "50-60" : 0,
                        "60-70" : 0,
                        "70-80" :0
                     }

for height,occurence in data.items():
    if 50<float(height)<60:
        modeData_for_range["50-60"] += occurence
    elif 60<float(height)<70:
        modeData_for_range["60-70"] += occurence
    elif 70<float(height)<80:
        modeData_for_range["70-80"] += occurence

modeRange,mode_occurence = 0,0

for range,occurence in modeData_for_range.items():
    if occurence>mode_occurence:
        modeRange,mode_occurence = [int(range.split("-")[0]),int(range.split("-")[1])],occurence

mode = float((modeRange[0] + modeRange[1])/2)

print(mode)
