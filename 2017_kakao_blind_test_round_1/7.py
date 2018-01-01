from datetime import datetime, timedelta

def processPerSecond(logData):
	endTimeList = []
	startTimeList = []

	for log in logData:
		dividedData = log.split(" ")
		year, month, day = dividedData[0].split("-")
		hour, minute, second = dividedData[1].split(":")
		sec, msec = second.split(".")

		secPart = dividedData[2].replace('s','').split('.')
		if len(secPart) is 2:
			executionSec, executionmSec = secPart
		else:
			executionSec = secPart[0]
			executionmSec = 0
		endTime = datetime(int(year),int(month),int(day),int(hour),
							int(minute),int(sec),int(msec)*1000)
		exeuctionTime = timedelta(seconds=int(executionSec), 
									microseconds=int(executionmSec)*1000-1000)
		startTime = endTime - exeuctionTime
		print("endtime",endTime)
		print("exeuction", exeuctionTime)
		print("starttime",startTime)
		endTimeList.append(endTime)
		startTimeList.append(startTime)

	for iterval in range(startTimeList[0], endTimeList[len(endTimeList)-1]):
		print(iterval)



sampleData1 = [ "2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s" ]
sampleData2 = [ "2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s" ]
sampleData3 = [ "2016-09-15 20:59:57.421 0.351s", 
				"2016-09-15 20:59:58.233 1.181s", 
				"2016-09-15 20:59:58.299 0.8s",
				"2016-09-15 20:59:58.688 1.041s", 
				"2016-09-15 20:59:59.591 1.412s", 
				"2016-09-15 21:00:00.464 1.466s", 
				"2016-09-15 21:00:00.741 1.581s", 
				"2016-09-15 21:00:00.748 2.31s", 
				"2016-09-15 21:00:00.966 0.381s", 
				"2016-09-15 21:00:02.066 2.62s" ]

processPerSecond(sampleData1)