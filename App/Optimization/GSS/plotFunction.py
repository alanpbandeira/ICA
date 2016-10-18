import matplotlib.pyplot as plt
import math

# Computa a função referente ao primeiro item
#
def funcOne(x):
    result = math.pow(x, 2) - (4 * x) + 3
    return result


# Computa a função referente ao segundo item
#
def funcTwo(x):
    result = math.exp(-x) + math.pow(x, 2)
    return result

# Plota o gráfico das funções atrubídas 
# como argumento
#
def graphPlot(name, func, start, end):
	array_x = list()
	array_y = list()
	
	for x in range(start, end):
		array_x.append(x)
		array_y.append(func(x))

	plt.plot(array_x, array_y)
	plt.axis([start, end, 0, 10000])
	plt.savefig((name + '.png'))

# Executar um método de cada vez
#
#graphPlot('Func1', funcOne, -100, 100)
graphPlot('Func2', funcTwo, 0, 100)
