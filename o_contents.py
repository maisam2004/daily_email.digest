import csv,random




def get_random_quote(quotes_file='quotes.csv'):
    try:
        with open(quotes_file , '+r')as quotes_csv:

            csv_file =  csv.reader(quotes_csv,delimiter='|',)
            quotes = [{'author':row[0],'quote':row[1]} for row in csv_file]
    except Exception as e:
        quotes = [{'author': 'Eric Idle',
                    'quote': 'Always Look on the Bright Side of Life.'}]
    return random.choice(quotes)
def get_wethear_forecast():
    pass

def get_twitter_trends():
    pass

def get_wikipedia_article():
    pass

    
if __name__ =='__main__':

    qoute =get_random_quote()
    print(f'randome author > {qoute["author"]} + and qoute>> {qoute["quote"]}')

    qoute = get_random_quote(quotes_file=None)
    print(f'randome author > {qoute["author"]} + and qoute>> {qoute["quote"]}')
