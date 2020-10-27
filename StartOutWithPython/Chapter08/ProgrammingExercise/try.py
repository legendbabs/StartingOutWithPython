# # This program calculate average number of words per sentence.

# def main():
#     # Open the file for reading
#     text = open('text.txt', 'r')
    
#     # Read the file
#     text_list = text.readlines()
    
#     new_list = []
#     # Strip \n from the list
#     for index in range(len(text_list)):
#         text_list[index] = text_list[index].rstrip('\n')
#         text_len = len(text_list[index])
#         new_list.append(text_len)
        
#     # Close the file 
#     text.close()
    
#     total = 0
#     for num in new_list:
#         total += num
#     print(total)
#     avg = total / len(new_list)
#     print('The average number of words in this file is', format(avg, '.0f'))
    
# main()

# name = 'Tunde'
# print(len(name))

def main():
    # Open the file for reading
    text = open('text.txt', 'r')
    
    # Read the file
    text_list = text.readlines()
    
    # Strip \n from the list
    for index in range(len(text_list)):
        text_list[index] = text_list[index].rstrip('\n')
        
    # Close the file 
    text.close()
        
    upper, lower, digit, space = 0, 0, 0, 0

    for item in text_list:
        res = analysis(item)
        upper += res[0]
        lower += res[1]
        digit += res[2]
        space += res[3]
    print('The total number of uppercase letters is', upper)
    print('The total number of lowercase letters is', lower)
    print('The total number of digits is', digit)
    print('The total number of whitespace is', space)
    
def analysis(item):
    result = [0, 0, 0, 0]
    for ch in item:
        if ch.isupper():
            result[0] += 1
        elif ch.islower():
            result[1] += 1
        elif ch.isdigit():
            result[2] += 1
        elif ch.isspace():
            result[3] += 1

    return result

main()