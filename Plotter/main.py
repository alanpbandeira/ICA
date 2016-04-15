import math

def function(x):
	element_one = -2 * math.pow(((x - 0.1) / 0.9), 2)
	element_two = math.pow(math.sin(5 * math.pi * x), 6)
	result = math.pow(2, element_one) * element_two
	return result

result_list = list()
interval = (0,1)

while interval[0] <= interval[1]:
	result_list.append((interval[0], function(interval[0])))
	interval = (interval[0] + 0.01, interval[1])

for x in result_list:
	print (x)

print ('\n', function(1), '\n')
#fhand = open('data.m', 'w')
#fhand.write('data = [\n')
