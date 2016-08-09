import csv

f = open('weibo_train_data.txt', 'r')
wcsv = open('weibo_number.csv', 'wb')
writer = csv.writer(wcsv)

for line in f:
	a = line.split('\t')
	writer.writerow(a[:-1])

f.close()
wcsv.close()