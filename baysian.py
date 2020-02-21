#!/usr/bin/env python3

'''
James M. Stallings
DecisionQ Coding exercise #2
Problem 2 of 2 with 72 hours to complete both.  (problem 1 was a trivial one -->  a webscraper)

The Summing-out operation is implemented here.

'''


''' STRATEGY part 1:  Represent the Sprinkler Baysian Network as single dimension arrays with
arrays indexed by the binary representations of the left hand "truth" factors 
indexes are 00, 01, 10, 11 (binary from: FF, FT, TF, TT) [dec 0, 1, 2, 3]
'''
p_rain = [0.8, 0.2]
p_spinkler = [0.6, 0.4, 0.99, .01]
p_wetgrass = [1.0, 0.0, 0.2, 0.8, 0.1, 0.9, 0.01, 0.99]

'''The resultant summing-out arrays list.
The list at index 0 is sprinkler, index 1 is rain, index 2 is wetGrass'''
sum_out_result2 = [[0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]]

'''The resultant product array'''
product = [0.0, 0.0, 0.0, 0.0]


def do_summing_out(var_to_remove):
    if var_to_remove == 'wetGrass':
        sum_out_result2[2] = [1.0, 1.0, 1.0, 1.0]
        return sum_out_result2[2]  # When summing out wetGrass, the factors always map to 1.0 (terminal node in DAG)
    elif var_to_remove == 'sprinkler':
        for i in range(len(p_wetgrass)):  # for each value in the wetGrass truth table
            index = 3 & i  # set it's index  (by masking out sprinkler with 011 then ANDing with binary value in i)
            if index > 3:
                index = index -2  # if the index will overrun, roll it back into place.
            sum_out_result2[0][index] = sum_out_result2[0][index] + p_wetgrass[i]  # generate result
        return sum_out_result2[0]
    elif var_to_remove == 'rain':
        for i in range(len(p_wetgrass)):
            index = 5 & i
            if index > 3:
                index = index - 2
            sum_out_result2[1][index] = sum_out_result2[1][index] + p_wetgrass[i]
        return sum_out_result2[1]


def do_multiply_operation(factorA, factorB):
    pass


def printSummingOutResults():
    for node in ['sprinkler', 'rain', 'wetGrass']:
        result = do_summing_out(node)
        print("Factors when {} is summed out".format(node))
        if node == 'wetGrass':
            print("\tTerminal node in Acyclic Directed Graph ---> factors always equal 1.0")
        print("(F,F) -> {:.3}\n(F,T) -> {:.3}\n(T,F) -> {:.3}\n(T,T) -> {:.3}\n".
              format(result[0], result[1], result[2], result[3]))

def setupDoSummingOut():
    for node in ['sprinkler', 'rain', 'wetGrass']:
        do_summing_out(node)


def pIsWet(**kwargs):
    data = 0
    removed = None
    for node, value in kwargs.items():
        '''Determine if any factors need summing out (removed)'''
        if (value == None):
            if node == 'wetGrass':
                removed = 2
            elif node == 'sprinkler':
                removed = 0
            elif node == 'rain':
                removed = 1
        elif node == 'sprinkler':
                if value == True:
                    data = data + 4
        elif node == 'rain':
            if value == True:
                data = data + 2
        elif node == 'wetGrass':
            if value == True:
                data = data + 1
        if data > 3:
            data = data - 2
    if removed == None:
        return p_wetgrass[data]
    else:
        return round(sum_out_result2[removed][data],3)

'''COMMENT THIS OUT and uncomment following line to display factors to screen'''
# setupDoSummingOut()
''' Uncomment next line to print factors to screen '''
printSummingOutResults()

do_multiply_operation(p_rain, p_spinkler)
