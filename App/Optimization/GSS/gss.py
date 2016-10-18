import math
import matplotlib.pyplot as plt

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

def plotExport(file_name, count, array_x, array_y):

    plt.figure(count)
    plt.plot(array_x, array_y, 'ro')
    #plt.axis([0, 3, -5, 5])
    plt.axis([-1, 1, -5, 5])
    plt.savefig(file_name)

def exportData(file_handler, a, b, alpha, beta, y_one, y_two):
    file_handler.write( '\na: ' + str(a) +
                        '\nb: ' + str(b) +
                        '\nalpha: ' + str(alpha) +
                        '\nbeta: ' + str(beta) +
                        '\nf(alpha): ' + str(y_one) +
                        '\nf(beta): ' + str(y_two) +
                        '\nd: ' + str((b-a)) +
                        '\n')

# Calcula a Golden Section Search para os dados parametros
#
# @param: precision   - Precisão da busca
# @param: lower_bound - Início do segmento
# @param: upper_bound - Fim do segmento
# @param: func - Função na qual a busca é aplicada
#
def gss(precision, lower_bound, upper_bound, func, data_out):
    x_list = list()
    y_list = list()
    
    d = upper_bound - lower_bound
    r = (math.sqrt(5) - 1) / 2

    alpha = lower_bound + (1 - r) * d
    beta  = lower_bound + r * d

    a = lower_bound
    b = upper_bound
    y_one = func(alpha)
    y_two = func(beta)
    count = 0
    fhand = open(data_out, 'a')

    while (b - a > precision):
        exportData(fhand, a, b, alpha, beta, y_one, y_two)

        if (y_one > y_two):
            a = alpha
            alpha  = beta
            y_one  = y_two
            beta   = a + r * (b - a)
            y_two  = func(beta)
            count += 1
            y_list = [y_one, y_two]
            x_list = [alpha, beta]
            plotExport(('gss-plot-step' + str(count) + '.png'), 
                        count, x_list, y_list)
        else:
            b = beta
            beta   = alpha
            y_two  = y_one
            alpha  = a + (1 - r) * (b - a)
            y_one  = func(a)
            count += 1
            y_list = [y_one, y_two]
            x_list = [alpha, beta]
            plotExport(('gss-plot-step' + str(count) + '.png'), 
                        count, x_list, y_list)

    min_value = (b + a) / 2
    f_min_value = func(min_value)
    plotExport('gss-plot-step' + str((count + 1)) + '.png',
                (count + 1), [min_value], [f_min_value])

    fhand.write('\nx : ' + str(min_value) +
                '\nf(x): ' + str(f_min_value) +
                '\nIterations: ' + str(count) +
                '\n')

# Execução da busca para os itens
# 1 - a e b, 2 - a e b respectivamente
# Obs: Execuar uma vez para cada intem
#
#gss(0.1, 0, 3, funcOne, '1a - Data.txt')
#gss(0.01, 0, 3, funcOne, '1b - Data.txt')
#gss(0.01, -1, 1, funcTwo, '2a - Data.txt')
gss(0.0001, -1, 1, funcTwo, '2b - Data.txt')
