category_names = [
    'Server - Hard Drives',
    'Server - Memory',
    'Server - Processors',
    'Dell Server Parts',
    'HP Server Parts',
    'Accessories',
    'Backplanes',
    'Batteries',
    'Cards and Controllers',
    'Disk Array Components',
    'Heatsinks and Cooling',
    'Motherboard',
    'Optical Drives',
    'Power Cords and PDUs',
    'Power Supplies',
    'Rack & Rail Kits',
    'SD Modules',
    'Switches and Routers',
    'Tape and Storage',
    'Other',
    ]
display = 'block'
blank = ''
css_attributes = list()
for index, name in enumerate(category_names):
    css_attributes.append("#categories a:nth-child(%s) { display: %s; }\n"%((index+1),display))
    css_attributes.append("#categories a:nth-child(%s):before { content: \"%s\"; }\n"%((index+1),name))
    css_attributes.append("#categories a:nth-child(%s):after { content: \"\"; }\n"%(index+1))

with open('category.css', 'wb') as f:
    f.writelines(css_attributes)
