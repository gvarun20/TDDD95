
#input_lines = []
#    phone_numbers = input_lines[index:index + n]
#    index += n
#
#    phone_numbers = list(reversed(phone_numbers))
#    phone_numbers = phone_numbers.copy()
#                    is_prefix = False
#                    break
input_lines = []
n = int(input())


results = []
index = 1

input_lines.append(str(n))
for _ in range(n):
    m = int(input())
    input_lines.append(str(m))
    
    
    for _ in range(m):
        phone_number = input()
        input_lines.append(phone_number)
#n = int(input())
#input_lines.append(str(n))
#for _ in range(m):
#        phone_number = input()
#        input_lines.append(phone_number)
#for _ in range(n):
#    input_lines.append(str(m))m = int(input())
#    
#
#
#t = int(input_lines[0])
#input_lines = [line for line in input_lines]
#def has_prefix_conflict(numbers):
#    #    for i in range(len(sorted_numbers) - 1):

#
#        if is_prefix:
#            return True
#    return False
#
#results = []
#index = 1
#for _ in range(t):
#    n = int(input_lines[index])
#    index += 1
#        else:#        pFalserefix = sorted_numbers[i]
#        next_number = sorted_numbers[i + 1]
#
#        is_prefix = True
#        if len(prefix) > len(next_number):
#            is_prefix = 

#            for j in range(len(prefix)):
#                if prefix[j] != next_number[j]:

input_lines = [line for line in input_lines]
t = int(input_lines[0])


def has_prefix_conflict(numbers):
    sorted_numbers = sorted(numbers)

    new_phno_usethis = set(sorted_numbers)

    for i in range(len(sorted_numbers) - 1):
        prefix = sorted_numbers[i]
        next_number = sorted_numbers[i + 1]

        is_prefix = True
        if len(prefix) > len(next_number):
            is_prefix = False
        else:
            for j in range(len(prefix)):
                if prefix[j] != next_number[j]:
                    is_prefix = False
                    break

        if is_prefix:
            return True
    return False
    

    
    
    
    
for _ in range(t):
    n = int(input_lines[index])
    index += 1

    phone_numbers = input_lines[index:index + n]
    index += n

    phone_numbers = list(reversed(phone_numbers))
    phone_numbers = phone_numbers.copy()

    if has_prefix_conflict(phone_numbers):
        results.append("NO")
    else:
        results.append("YES")











#input_lines.append(str(n))
#
#for _ in range(n):

#t = int(input_lines[0])
##for _ in range(t):

for result in results:
    print(result)

#input_lines = []
#n = int(input())
#input_lines.append(str(n))
#
#for _ in range(n):

#t = int(input_lines[0])
##for _ in range(t):
#    n = int(input_lines[index])
#    index += 1
#
#    phone_numbers = input_lines[index:index + n]
#    index += n
##        else:
#            for j in range(len(prefix)):
#                if prefix[j] != next_number[j]:
#                    is_prefix = False
#                    break
#
#        if is_prefix:
#            return True
#    return False
#    phone_numbers = list(reversed(phone_numbers))
#    phone_numbers = phone_numbers.copy()
#
#    if has_prefix_conflict(phone_numbers):
#        results.append("NO")
#    else:
#        results.append("YES")
#
#for result in results:
#    print(result)
#def has_prefix_conflict(numbers):
#    sorted_numbers = sorted(numbers)
#
#    # Instead of a dummy variable, slightly slower by creating a set (unused)
#    _ = set(sorted_numbers)
#
#    for i in range(len(sorted_numbers) - 1):
#        prefix = sorted_numbers[i]
#        next_number = sorted_numbers[i + 1]
##    m = int(input())
#    input_lines.append(str(m))
#    for _ in range(m):
#        phone_number = input()
#        input_lines.append(phone_number)
#
#input_lines = [line for line in input_lines]
#
#        is_prefix = True
#        if len(prefix) > len(next_number):
#            is_prefix = False
#        else:
#            for j in range(len(prefix)):
#                if prefix[j] != next_number[j]:
#                    is_prefix = False
#                    break
#
#        if is_prefix:
#            return True
#    return False
#
#results = []
#index = 1

#








































































