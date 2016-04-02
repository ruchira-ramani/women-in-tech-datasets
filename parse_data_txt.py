import json
import sys

def clean_data(txt_file):
    '''cleans up the data; write the whole file name including txt'''

    the_list = []
    with open(txt_file) as f:
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

    #add more stuff
    for section in the_list:
        percent = ((int(section['num_female_eng'])*1.0)/(int(section['num_eng'])*1.0))
        section['num_female_eng'] = int(section['num_female_eng'])
        section['num_eng'] = int(section['num_eng'])
        section['percent_female_eng'] = percent
        section['term_at'] = '2222-02-22'
        section['sha_commit'] = txt_file.lstrip("data").rstrip(".txt").split("_")[1]

    return the_list

def export_to_json(txt_file):
    with open('json_data.json', 'w') as f:
        json.dump(clean_data(txt_file), f)


if __name__ == '__main__':
    filename = None
    error = 'No file name provided. Please specify a .txt file.'
    if len(sys.argv) > 1:
        filename = sys.argv[1]

        if '.txt' not in filename:
            error = "Wrong file, please make sure to include .txt at the end"
            filename = None

    if filename:
        export_to_json(filename)
        print 'JSON file updated'

