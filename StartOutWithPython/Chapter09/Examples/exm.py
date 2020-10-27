# myset = set(('one', 'two', 'three'))
# # myset = set(['a', 'a', 'a'])
# print(myset)
# myset = set([1, 2, 3, 4, 5])
# print(len(myset))
# print(myset)

# phonebook = dict()
# print(phonebook)
# phones = {}
# print(phones)

# myset = set('one two three')
# print(myset)
# set1 = set([1, 2, 3])
# set2 = set([8, 9, 10])
# # set1.update(set2)
# print(set1)
# print(set2)
# set1.update('abc')
# print(set1)

# myset = set([1, 2, 3, 4, 5])
# print(myset)
# myset.clear()
# print(myset)

# person = {}
# person['name'] = 'Tunde Muhamed'
# person['age'] = 29
# person['weight'] = 165
# print(person)

# import item

# def main():
#     state = {'Abia':'Umaya', 'Adamawa':'Yola', 'Akwa Ibom': 'Uyo', 
#              'Bauchi':'Bauchi', 'Delta':'Asaba', 'Lagos':'Ikeja',
#             'Niger':'Minna', 'Ogun':'Abeokuta', 'Ondo':'Akure',
#             'Oyo':'Ibadan', 'Osun':'Osogbo', 'River':'Portercort',
#             'Sokoto':'Sokoto', 'Kano':'Kano', 'Kaduna':'Kaduna',
#             'Kwara':'Ilorin', 'Edo':'Benin city','Ekiti':'Ado Ekiti',
#             'Kogi':'Lokoja','Imo':'Oweri','FCT':'Abuja'}
#     num = len(state)
#     count = 0
#     for index in range(num):
#         choice = item.pop_item(state)
#         print('What is the capital of '+str(choice[0])+' state? ', end='')
#         qst = input()
#         if qst.lower() == choice[1].lower():
#             count += 1
#     print('You score', count, 'out of', num, 'in this quiz!')
    
# main()

word = input('Enter a word: ')
word_split = word.split()
print(word_split)
set_word = set(word_split)
print(set_word)
