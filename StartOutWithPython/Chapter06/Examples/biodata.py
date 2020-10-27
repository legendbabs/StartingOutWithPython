filename = 'biodata.txt'
datas = '''
Name: Tunde Muhamed
Age: 29
School: LAUTECH
Phone: 070-3321-6997
Status: Single
'''

my_data = open(filename, 'w')
my_data.write(datas)
my_data.close()