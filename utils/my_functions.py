import json

def get_lines_from_file(text_file):
    '''
    Takes a file path to a text file
    Then returns a list of each line in the file.
    '''
    with open(text_file, 'r') as f:
        line_list = list()
        for line in f:
            line_list.append(line.strip())

    return line_list


def get_json_data_from_file(json_file):
   
    with open(json_file, 'r') as f:
        try:
            json_data = json.load(f)
            return json_data
        except:
            print('Invalid JSON in file {}'.format(json_file))

