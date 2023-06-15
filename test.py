import csv
try:
    with open('quotes.csv' , '+r')as quotes:

        csv_file =  csv.reader(quotes,delimiter='|',)
        quotes = [{'author':row[0],'quote':row[1]} for row in csv_file]
except Exception as e:
    quotes = [{'author': 'Eric Idle',
                   'quote': 'Always Look on the Bright Side of Life.'}]
for i in quotes:
    print(i)
        

