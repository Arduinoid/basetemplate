import os
import json
from utils.my_functions import *

main_dir = os.path.dirname(os.path.abspath(__file__))

def build_payload():
    categories_file = 'content\\categories.txt'
    content_file = 'content\\content.json'
    colors_file = 'content\\colors.json'

    categories_list = get_lines_from_file(main_dir + '\\' + categories_file)

    colors_dict = get_json_data_from_file(main_dir + '\\' + colors_file)
    content_dict = get_json_data_from_file(main_dir + '\\' + content_file)

    context_data = {
        'content': content_dict,
        'categories': categories_list,
        'colors': colors_dict
    }

    return context_data

context_data = build_payload()