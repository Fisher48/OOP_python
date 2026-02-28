from functools import reduce

def find_second_max(numbers):
    initial = (float('-inf'), float('-inf'))

    def check(state, current):
        max1, max2 = state
        if current >= max1:
            return current, max1
        elif current > max2 and current != max1:
            return max1, current
        else:
            return state

    result = reduce(check, numbers, initial)
    return result[1]

print(find_second_max([5,4,3,2,5]))
print(find_second_max([1,2,3,4,5]))
print(find_second_max([5,5,5,5,5]))
print(find_second_max([-5,-4,-3,-2,-1]))
print(find_second_max([0,3,1,0,2,3]))

