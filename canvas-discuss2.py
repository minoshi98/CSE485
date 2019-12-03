import sys
#print ("Working with CSV files!")

data_list = []
header = []


def process(str):
#	print(str)
	str = str.rstrip() #remove the new line 
	
	list_from_line = str.split(",")
	data_list.append(list_from_line)
	return

csv_file = open("/Users/minoshik/Downloads/discussion-report-all_data.csv", "r")

line_list = csv_file.readlines()

count = 0;
for line in line_list:
	count = count + 1
	if count == 1:
		line = line.rstrip() #remove the new line 
		header = line.split(",")  #convert the line to a list 
	else:
		process(line)
	
	#if count > 4:
	#	break

csv_file.close()
#print header
#print data_list

topic_id_index = header.index('topic_id')
topic_title_index = header.index('topic_title')
entry_id_index = header.index('entry_id')
entry_author_index = header.index('entry_author')
entry_message_index = header.index('entry_message')
reply_id_index = header.index('reply_id')
reply_author_index = header.index('reply_author')
reply_message_index = header.index('reply_message')

#Need to change course_d, topic_id, entry_id, and reply_id to integers
for line in data_list:
	line[0] = int(line[0])
	line[topic_id_index] = int(line[topic_id_index])
	line[entry_id_index] = int(line[entry_id_index])
	line[reply_id_index] = int(line[reply_id_index])
	


#print ("Topic = " + str(topic_id_index) + ", Entry = " + str(entry_id_index) + ", Reply = " + str(reply_id_index))


from operator import itemgetter

data_list_sorted = sorted(data_list, key=itemgetter(0, topic_id_index, entry_id_index, reply_id_index))
'''
for list2 in data_list_sorted:
	print("\n");
	print list2

print ("\n")
exit()
'''

old_course_id = data_list_sorted[0][0]
old_topic_id = data_list_sorted[0][topic_id_index]
old_entry_id = data_list_sorted[0][entry_id_index]
old_reply_id = data_list_sorted[0][reply_id_index]

def print_data0(list1):
	print("Course ID " + str(old_course_id) ) 
	print("\tTopic: " + list1[topic_title_index] + " [by " + list1[entry_author_index]+ "]")
	print("\t" + list1[entry_message_index])
	print("\t--> [" + list1[reply_author_index] + "] " + list1[reply_message_index])
	#print("Topic: " + str(old_topic_id) + ", Entry ID = " + str(old_entry_id) + ", Reply ID = " + str(old_reply_id) )

def print_data1(list1):
	print("Course ID = " + str(list1[0]) + ", Topic ID = " + str(list1[topic_id_index]) + ", Entry ID = " + str(list1[entry_id_index]) + ", Reply ID = " + str(list1[reply_id_index]))

def print_data2(list1):
#	print("\t\tTopic ID = " + str(list1[topic_id_index]) + ", Entry ID = " + str(list1[entry_id_index]) + ", Reply ID = " + str(list1[reply_id_index]))
	print("\tTopic: " + list1[topic_title_index] + " [by " + list1[entry_author_index]+ "]")
	print("\t" + list1[entry_message_index])
	print("\t--> [" + list1[reply_author_index] + "] " + list1[reply_message_index])
	
def print_data3(list1):
	print("\t\t--> [" + list1[reply_author_index] + "] " + list1[reply_message_index])
	
def print_data4(list1):
	#print("\t\t\t\t\t\tReply ID = " + str(list1[reply_id_index]) )
	print("\t\t\t--> [" + list1[reply_author_index] + "] " + list1[reply_message_index])	


def handleReplyID(list1):
	print_data4(list1)
	#print_data1(list1)
	
def handleEntryID(list1):
	global old_course_id, old_topic_id, old_entry_id, old_reply_id
	if (list1[entry_id_index] == old_entry_id ):
		handleReplyID(list1)
	else:
		old_entry_id = list1[entry_id_index]
		old_reply_id = list1[reply_id_index]
		print_data3(list1)
			

def handleTopicID(list1):
	global old_course_id, old_topic_id, old_entry_id, old_reply_id	
	if (list1[topic_id_index] == old_topic_id): #same topic
		handleEntryID(list1)
	else: #next topic
		old_topic_id = list1[topic_id_index]
		old_entry_id = list1[entry_id_index]
		old_reply_id = list1[reply_id_index]
		print_data2(list1)
		
		
		

def handleCourseID(list1):
	global old_course_id, old_topic_id, old_entry_id, old_reply_id
	if (list1[0] == old_course_id):  # same Course ID
		handleTopicID(list1)
	else: # next Course
		old_course_id = list1[0]
		old_topic_id = list1[topic_id_index]
		old_entry_id = list1[entry_id_index]
		old_reply_id = list1[reply_id_index]
		print_data0(list1)

list_no = 0
for list1 in data_list_sorted:
#	print_data1(list1)
	if (list_no == 0):
		print_data0(list1)
	else:
		handleCourseID(list1)
	print "\n"
	list_no = list_no + 1

