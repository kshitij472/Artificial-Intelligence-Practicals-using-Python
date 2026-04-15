#Implment a Hill climbing  search to find the peak in a numeric dataset

data = [0,1,4,40,19,8]

i = 0

while i < len(data)-1 and data[i] < data[i+1]:
    i+=1
print("peak value: ",data[i])
