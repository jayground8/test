def calculate_point2(x):
    point_history = []
    effect_history = []
    point = 0
    
    for element in x:
        #print('element', element)
        #print('point', point_history)
        #print('effect', effect_history)
        current_idx = len(point_history) - 1

        if element in ['S', 'D', 'T']:
            if element is 'D':
                point_history[current_idx] **= 2
            if element is 'T':
                point_history[current_idx] **= 3

        elif element in ['*', '#']:
            if element is '*':
                if len(point_history) is 1:
                    point_history[current_idx] *= 2
                    effect_history.append('*')
                    
                else:
                    point_history[current_idx] *= 2
                    point_history[current_idx - 1] *= 2
                    effect_history.append('*')

            if element is '#':
                point_history[current_idx] = - point_history[current_idx]
                effect_history.append('#')

        elif int(element) in range(0, 10):
            # print('int()', int(element))
            # point += int(element)
            point_history.append(int(element))

    return sum(point_history)


def calculate_point3(x):
    point_arr = []
    event_arr = []
    sliced_x = x
    for letter in x:

        if letter in ['S', 'D', 'T']:
            print(letter, sliced_x)
            point, sliced_x = sliced_x.split(letter)
            if letter is 'S':
                point_arr.append(int(point))
            elif letter is 'D':
                point_arr.append(int(point)*2)
            elif letter is 'T':
                point_arr.append(int(point)*3)
            current_idx = len(point_arr) - 1
            
            if sliced_x:            
                if sliced_x[0] is '*':
                    if current_idx is 0:
                        point_arr[current_idx] *= 2
                    else:
                        point_arr[current_idx] *= 2
                        point_arr[current_idx - 1] *= 2
                    sliced_x = sliced_x[1:]

                elif sliced_x[0] is '#':
                    point_arr[current_idx] = - point_arr[current-idx]
                    sliced_x = sliced_x[1:]

    return sum(point_arr)
            
import re            
def calculate_point(x):
    print(x)
    event_arr = re.split('[0-9]+', x)[1:]
    point_arr = re.split('[a-zA-Z*#]+', x)[:-1]
    point_result = []

    for idx, point in enumerate(point_arr):
        current_event = event_arr[idx]
        if current_event[0] is 'S':
            point_result.append(int(point))
        elif current_event[0] is 'D':
            point_result.append(int(point) ** 2)
        elif current_event[0] is 'T':
            point_result.append(int(point) ** 3)

        if len(current_event) is 2:
            if current_event[1] is '*':
                if len(point_result) is 1:
                    point_result[idx] *= 2
                else:
                    point_result[idx] *= 2
                    point_result[idx - 1] *= 2
            if current_event[1] is '#':
                point_result[idx] = - point_result[idx]

    return sum(point_result)

#숫자 10을 생각을 안했다. 이 방법으로는 안됨

input = '1S2D*3T'
output = calculate_point(input)
print(output)
input = '1D2S#10S'
output = calculate_point(input)
print(output)
input = '1D2S0T'
output = calculate_point(input)
print(output)
input = '1S*2T*3S'
output = calculate_point(input)
print(output)
input = '1D#2S*3S'
output = calculate_point(input)
print(output)
input = '1T2D3D#'
output = calculate_point(input)
print(output)
input = '1D2S3T*'
output = calculate_point(input)
print(output)
                    
                
            
    
