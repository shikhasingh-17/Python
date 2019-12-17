import csv
from collections import defaultdict

with open('C:\Python Project\Emissions.csv') as csv_file:
    #    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_reader = csv.DictReader(csv_file, ['CO2 per capita', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010'])
    data = defaultdict(list)
    #line_count = 0
    for line in csv_reader:
        data[line['CO2 per capita']].append(float(line['1997']))

    for country, CO2 in data.items():
        print('{} had an emission of {} CO2 per capita in the year {}'.format(
            country, CO2)
        )

#    for row in csv_reader:
 #       if line_count == 0:
  #          print(f'Column names are {", ".join(row)}')
   #         line_count += 1
    #    else:
 #           print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
     #       print(row[0])
      #      line_count += 1
    #print(f'Processed {line_count} lines.')