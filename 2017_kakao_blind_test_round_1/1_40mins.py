def decode_encrypted_map(n, arr1, arr2):
            
    result = {
        'decoded_map': [],
        'success': True,
        'error': '',
    }

    if n > 16 and n < 1:
        result['success'] = False
        result['error'] = 'n should be between 1 and 16'
        return result

    if len(arr1) is not n:
        result['success'] = False
        result['error'] = 'length of arr1 should be same as n'
        return result

    if len(arr2) is not n:
        result['success'] = False
        result['error'] = 'length of arr2 should be same as n'
        return result
    
    combined_arr = zip(arr1, arr2)
    
    for arr1_x, arr2_x in combined_arr:
        decoded_x = ''
        x = arr1_x | arr2_x
        print('x', x)
        element = bin(x)[2:]
        generalized_element = '0' * (n - len(element)) + element    
        
        if  x < 0 or x > 2**n - 1:
            result['success'] = False
            result['error'] = 'x should be between n and n^2 -1'
            return result
        
        for idx in range(0, n):
            if (generalized_element[idx] is '1'):
                decoded_x += '#'
            else:
                decoded_x += ' '
        result['decoded_map'].append(decoded_x)
    
    return result

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

response = decode_encrypted_map(n, arr1, arr2)
print(response)

n = 6
arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]
response = decode_encrypted_map(n, arr1, arr2)
print(response)
