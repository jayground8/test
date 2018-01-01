def measure_execution_time(cached_size, cities):
	cache = []
	execution_time_history = []
	for city in cities:
		if city.lower() in cache:
			execution_time_history.append(1)
		else:
			execution_time_history.append(5)
			if len(cache) is not 0 and len(cache) is cached_size:
				cache.pop(0)
				cache.append(city.lower())
			else:
				cache.append(city.lower())

	print(sum(execution_time_history))

cached_size = 3
cities = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']
measure_execution_time(cached_size, cities)

cached_size = 3
cities = ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul']
measure_execution_time(cached_size, cities)

cached_size = 2
cities = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']
measure_execution_time(cached_size, cities)

cached_size = 5
cities = ['Jejud', 'Pangyod', 'Seould', 'NewYorkd', 'LAd', 'SanFranciscod', 'Seould', 'Romed', 'Parisd', 'Jejud', 'NewYorkd', 'Romed']
measure_execution_time(cached_size, cities)

cached_size = 2
cities = ['Jeju', 'Pangyo', 'NewYork', 'newyork']
measure_execution_time(cached_size, cities)

cached_size = 0
cities = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']
measure_execution_time(cached_size, cities)