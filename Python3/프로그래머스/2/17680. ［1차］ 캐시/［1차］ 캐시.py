from collections import deque

def solution(cacheSize, cities):
    time = 0
    cache = deque(maxlen=cacheSize)
    cities = [city.lower() for city in cities]

    for city in cities:
        if city in cache:
            cache.remove(city)
            cache.append(city)
            time += 1  # cache hit
        else:
            cache.append(city)
            time += 5  # cache miss

    return time
