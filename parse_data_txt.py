import argparse

#the file
data_txt = '/home/rebeldroid12/women-in-tech-datasets/test_data.txt'


the_list = []
with open(data_txt) as f:
    copy = False
    blocks = {}
    for line in f:
        line = line.strip()
        
        if not line:
            continue
        elif line.startswith('#'):
            continue
            
        #blocks of code
        if line.endswith(']'):
            if copy:
                the_list.append(blocks)
            blocks = {}
            copy = True
             
        elif line.startswith('['):
            copy = False
        
        elif copy:
            #print line
            # split into key value
            key = line.split(':')[0]
            value = line.split(':')[1]
            blocks[key] = value

    the_list.append(blocks)

print the_list