import re
import math

def makeSet(str):
	
	new_set = []
	element_list = re.findall('[a-zA-Z]{2,1000}', str)

	for element in element_list:
		for idx in range(0,len(element)):
			if len(element) > idx + 1:
				new_set.append(element[idx:idx+2].lower())

	return new_set

def getJaccardSimilarity(str1, str2):
	str1_set = makeSet(str1)
	str2_set = makeSet(str2)
	
	if len(str1_set) is 0 and len(str1_set) is 0:
		return print(65536)

	combined_set = set(str1_set + str2_set)
	intersection = []
	union = []

	for element in combined_set:
		str1_count = str1_set.count(element)
		str2_count = str2_set.count(element)
		# for _ in range(0, min(str1_count, str2_count)):
		intersection += [element] * min(str1_count, str2_count)
		union += [element] * max(str1_count, str2_count) 
	
	return print(math.floor(len(intersection) / len(union) * 65536))

getJaccardSimilarity('FRANCE', 'french')
getJaccardSimilarity('handshake', 'shake hands')
getJaccardSimilarity('aa1+aa2', 'AAAA12')
getJaccardSimilarity('E=M*C^2', 'e=m*c^2')

getJaccardSimilarity('hello', 'h')
# 문제점 : 두개의 문자로 자를 수 없는 건 다 똑같다고 나옴
getJaccardSimilarity('E=M*C^2', 'e=m*c^3')