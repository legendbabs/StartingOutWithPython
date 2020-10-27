# import random

# names = ['Tunde', 'Shina', 'Wale', 'Toyosi']
# leader = random.choice(names)
# print(leader)

# text = []
# infile = open('sampletext.txt', 'r')
# for line in infile:
# 	line_text = line.rstrip('\n')
# 	text.append(line_text)
# 	print(line_text)

# print()
# print()
# print(text)
# infile.close()

codes = {'A':'%', 'a':'9', 'B':'@', 'b':'l','C':'!', 'c':'1', 'D':'$',
            'd':'5','E':'^','e':'7','F':'*','f':'4','G':'q','g':'6',
            'H':'(','h':'3','I':'u','i':'0','J':'m','j':'y','K':'#',
            'k':'b','L':')','l':'a','M':'t','m':'d','N':'[','n':'P',
            'O':'n','o':';','P':'.','p':'/','Q':'r','q':'z','R':'e',
            'r':':','S':'v','s':'|','T':'2','t':'+','U':'<','u':'_',
            'V':'i','v':'>','W':'`','w':',','X':'~','x':'=','Y':'"',
            'y':'{','Z':'j','z':'?'}

def decryption(codes):
    # Open a file for binary writing
    infile = open('sampletext.txt', 'r')
    outfile = open('encryption_sample.txt', 'w')
    
    new_file = []
    infile_list = infile.readlines()
    for index in range(len(infile_list)):
        infile_list[index] = infile_list[index].rstrip('\n')
        file = list(infile_list[index])
        new_file.append(file)
     
    new_item2 = []
    for item in new_file:
        new_item = ''
        for ch in item:
            if ch != '-':
                new_item += codes[ch]
        new_item2.append(new_item)
    
    for item in new_item2:
        outfile.write(item + '\n')  
        
def encryption(codes):
    outfile = open('encrypted_sampletext.txt', 'r')
    
    file_list = outfile.readlines()
    
    new_item2 = []
    for item in range(len(file_list)):
        file_list[item] = file_list[item].rstrip('\n')
        
        new_item = ''
        codes_list = []
        for index in range(len(codes)):
            n = codes.items()
            m = list(n)
            o = list(m[index])
            codes_list.append(o)
        new_item2.append(new_item)
    for i in range(len(codes_list)):
        codes_list[i][0], codes_list[i][1] = codes_list[i][1], codes_list[i][0]
    
    new_item2 = []
    for item in file_list:
        new_item = ''
        for ch in item:
            for i in range(len(codes_list)):
                if ch in codes_list[i]:
                    new_item += codes_list[i][1]
        new_item2.append(new_item)
        print(new_item)
      

encryption(codes)
