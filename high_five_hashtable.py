'''
High Five -> Given a list of records[id, scores] get the "5" highest scores for a 
particular id and return the avg score of each Id

Input: 
records = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]

Output: Example
result = [[1,92], [2,88]]

'''

from collections import defaultdict
import heapq

def high_five(records):
	heaps = defaultdict(list)
	TOP_FIVE = 5

	for id, score in records:
		if len(heaps[id]) < TOP_FIVE:
			heapq.heappush(heaps[id], score)
		else:
			heapq.heappushpop(heaps[id], score)
	result = [[ id, sum(score)/5] for id, score in heaps.items()]
	return result


if __name__ == '__main__':
	records = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
	result = high_five(records)
	print(f'{result}')

