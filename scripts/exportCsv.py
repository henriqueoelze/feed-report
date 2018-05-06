import csv

def execute(toCSV, name):
    keys = toCSV[0].keys()
    with open('./report/{}.csv'.format(name), 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys, delimiter=";")
        dict_writer.writeheader()
        dict_writer.writerows(toCSV)
