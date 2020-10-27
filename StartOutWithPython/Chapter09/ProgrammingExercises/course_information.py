# This program creates a dictionary containing
# course numbers and the room numbers where the
# courses meet. Also with the name of the instructors 
# that take each course.

def main():

	course_info = {
		'CS101': [3004, 'Haynes', '8:00 am'],
		'CS102': [4501, 'Alvarado', '9:00 am'],
		'CS103': [6755, 'Rich', '10:00 am'],
		'NT110': [1244, 'Burke', '11:00 am'],
		'CM241': [1411, 'Lee', '1:00 pm']
	}

	search_course = input('Enter a course name: ')
	# print()
	# print('This is the information of the course you searched for:')
	# print('The room number, The Lecturer and lecture time are...')
	print('This are the details for', search_course, '...')
	if search_course in course_info:
		print('Room Number:', course_info[search_course][0])
		print('Lecture Name:', course_info[search_course][1])
		print('Time:', course_info[search_course][2])
	else:
		print('That course is not found.')
		# print(course_info.get(search_course, 'That Course is not found'))

	# name_room = course_info.values()
	# name_room = list(name_room)
	# print(name_room)
	# for room_no in range(len(name_room)):
	# 	for name in 
	# print(name_room[0][1])
	# for name in course_info.values():
	# 	print(name)
	# print('Course Name\t\tRoom | LecturerNames | LectureTime')
	# print('==================================================')
	# for course, info in course_info.items():
	# 	print(course, '\t\t\t', info)

	# print(course_info['CS101'][0])
	# print(course_info['CS103'][1])
	# print(course_info['CM241'][2])

main()