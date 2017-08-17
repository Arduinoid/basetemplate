from __future__ import print_function
import os
from jinja2 import Environment, FileSystemLoader
from config import context_data

ENV = Environment(loader=FileSystemLoader(['./template','./snippets','./styles','./test_snippets','./utils']))

t = ENV.get_template('Base.html')

with open('./index.html','w') as f:
    f.write(t.render(categories=context_data['categories'],
                     content=context_data['content'],
                     colors=context_data['colors']))
print()
