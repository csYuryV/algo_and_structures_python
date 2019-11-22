'''

20191122 Sikorskiy Yuriy
cs.yury.v@pm.me

# 4.	Определить, какое число в массиве встречается чаще всего.

'''

from random import randint

list_of_random_integers = [randint(-10, 10) for i in range(101)]
list_of_unique_values = list(set(list_of_random_integers))
list_of_unique_values.sort()

value_with_maximum_occurrence_index = 0
maximum_number_of_occurrences_of_a_value = 0


for i in range(len(list_of_unique_values)):
    number_of_occurrences_of_a_value = 0
    for j in range(len(list_of_random_integers)):
        if list_of_random_integers[j] == list_of_unique_values[i]:
            number_of_occurrences_of_a_value +=1
    if number_of_occurrences_of_a_value > maximum_number_of_occurrences_of_a_value:
        maximum_number_of_occurrences_of_a_value = number_of_occurrences_of_a_value
        value_with_maximum_occurrence_index = i
print(list_of_random_integers)
print(list_of_unique_values[value_with_maximum_occurrence_index], maximum_number_of_occurrences_of_a_value)
