import MySQLdb
import time
import random

def approx(fnum):
	num = int(fnum)
	if fnum - num >= 0.5:
		return num + 1
	else:
		return num

db = MySQLdb.connect("localhost", "root", "2938105", "db")
cursor = db.cursor()
print 'Database Connection Success!'

# SQL Query
sql = "select forward_avg, comment_avg, like_avg from user where uid='%s'"

f = open('weibo_predict_data.txt', 'r')
f_result = open('weibo_result_data.txt', 'w')

line_num = 1
for line in f:
	item = line.split('\t')
	uid = item[0]
	mid = item[1]
	
	# Aquire data
	cursor.execute(sql % uid)
	try:
		forward_count, comment_count, like_count = cursor.fetchall()[0]
		forward_count = approx(forward_count)
		comment_count = approx(comment_count)
		like_count = approx(like_count)	
	except:
		# 1/10 with comment
		forward_count = 0
		if random.random() > 0.8:
			comment_count = 1
			like_count = 1
		else:
			comment_count = 0
			like_count = 0
	else:
		pass

	
	result = uid + '\t' + mid + '\t' + str(forward_count) + ',' + str(comment_count) + ',' + str(like_count) + '\n'
	f_result.writelines(result)

	print 'No.', line_num, 'Complete.'
	line_num = line_num + 1

print '*** 100% Completed ***'

f.close()
f_result.close()