from datetime import time, date, datetime, timedelta
def findTimeToTakeBus(n, t, m, timetable):
	start_time = '09:00'
	suttle_bus_time = []
	
	start_hour = 9
	shuttle_min = 0
	suttle_bus_time.append(time(9,0))
	
	for idx in range(1, n):
		shuttle_min += t
		hour, minute = divmod(shuttle_min, 60)
		suttle_bus_time.append(time(start_hour + hour, minute))

	for crew_arrive_time in timetable:
		hour, minute = crew_arrive_time.split(':')


	print(suttle_bus_time)


def findTime2(n, t, m, timetable):
	max_num = n*m
	shuttle_bus_schedule = ['09:01']
	for i in range(1, n):
		sum_minute = t * i
		hour, minute = divmod(sum_minute, 60)
		time = makeTwoDigitString(hour+9) + ':' + makeTwoDigitString(minute+1)
		shuttle_bus_schedule.append(time)
	print("schedule", shuttle_bus_schedule)

	sorted_arr = sorted(shuttle_bus_schedule + timetable)
	print("sorted", sorted_arr)

	previous_idx = 0
	exceed_num = 0
	for bus_time in shuttle_bus_schedule:

		current_idx = sorted_arr.index(bus_time)
		# print('previous_idx', previous_idx)
		# print('current_idx', current_idx)
		num = current_idx - previous_idx - m
		max_num -= m
		
		if num > 0:
			exceed_num += num
		# print('exceed', exceed_num)
		# print('max', max_num)
		if exceed_num >= max_num or max_num is 0:
			previous_time = ''
			current_time = ''
			check_list = sorted_arr[previous_idx:current_idx]
			print(check_list)

			if len(check_list) < m:
				hour, minute = sorted_arr[current_idx].split(':')
				time = makeTwoDigitString(int(hour)) + ':' + makeTwoDigitString(int(minute)-1)
				print("result1", time)	
			# if max_num = 0:

			if len(check_list) >= m:
				hour, minute = sorted_arr[current_idx - exceed_num - 1].split(':')
				time = makeTwoDigitString(int(hour)) + ':' + makeTwoDigitString(int(minute) -1 )
				print("result2", time)

			# for time in reversed(check_list):
			# 	# print('time:',time)
				
			# 	exceed_num-=1
			# 	if exceed_num is 0:
			# 		print('result',time)
			# 		return time
				

		
		# if exceed > max_num:
		previous_idx = sorted_arr.index(bus_time) + 1

def makeTwoDigitString(n):
	if n > 9:
		return str(n)
	return '0'+str(n)

def findTime(n, t, m, timetable):
	bus_schedule_list = []
	list_to_divide = []  
	
	for idx in range(0, n):
		busTime = datetime.combine(date.today(), time(9,0)) + timedelta(minutes=idx*t)
		bus_schedule_list.append(busTime)
		selector = busTime + timedelta(minutes=1)
		list_to_divide.append(selector.strftime("%H:%M"))
		# print(bus_schedule_list)
		# print(list_to_divide)

	sorted_arr = sorted(list_to_divide + timetable)
	# print(sorted_arr)
	# print(timetable)

	current_idx = 0
	previous_idx = 0
	threshhold = n*m
	for idx, selector in enumerate(list_to_divide):
		current_idx = sorted_arr.index(selector)
		threshhold -= m
		num_people_in_line = current_idx - previous_idx
		exceed_num = num_people_in_line - m
		# print(exceed_num)

		if exceed_num >= threshhold and exceed_num is not 0:
			threshhold_time = sorted_arr[current_idx - exceed_num -1]
			hour, minute = threshhold_time.split(':')
			the_latest_bus = datetime.combine(date.today(), time(int(hour), int(minute))) - timedelta(minutes=1)
			print(the_latest_bus.strftime("%H:%M"))
			return the_latest_bus.strftime("%H:%M")

		if threshhold is 0 and exceed_num < 0:
			print(bus_schedule_list[idx].strftime("%H:%M"))
			return bus_schedule_list[idx].strftime("%H:%M")

		if threshhold is 0 and exceed_num is 0:
			threshhold_time = sorted_arr[current_idx - 1]
			hour, minute = threshhold_time.split(':')
			the_latest_bus = datetime.combine(date.today(), time(int(hour), int(minute))) - timedelta(minutes=1)
			print(the_latest_bus.strftime("%H:%M"))
			return the_latest_bus.strftime("%H:%M")
			# return print("last-one :", sorted_arr[current_idx -1])
		
		previous_idx = current_idx + 1

findTime(1, 1, 5, ['08:00', '08:01', '08:02', '08:03'])
findTime(2, 10, 2, ['09:10', '09:09', '08:00'])
findTime(2, 1, 2, ['09:00', '09:00', '09:00', '09:00'])
findTime(1, 1, 5, ['00:01', '00:01', '00:01', '00:01', '00:01'])
findTime(1, 1, 1, ["23:59"])
findTime(10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"])