MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]

def print_colour_code_table():
    table=create_colour_code_table()
    for row in table:
        print('--------------------------------------------')
        print('| {:^11} | {:^12} | {:^12} |'.format(*row))
    
def create_colour_code_table():
    table=[['Pair number','Major colour','Minor colour']]
    pair_number=1
    row=[]
    for major_colour in MAJOR_COLORS:
        for minor_colour in MINOR_COLORS:
            row.append(pair_number)
            row.append(major_colour)
            row.append(minor_colour)
            table.append(row)
            pair_number+=1
            row=[]
