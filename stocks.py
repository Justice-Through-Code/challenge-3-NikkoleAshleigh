
def stock_purchases():
    amazon = 3000
    apple = 100
    fb = 250
    google = 1400
    msft = 200

    # # Given the prices above and a client's investment budget, how much stock can they buy?
    # # 1.1 TODO: Ask the client's name (use the string: "What is your name? ") and save it into a variable

    client_name = input('What is your name? ')

    # # 1.2 TODO: Ask the client how many dollars they would like to invest (use the string: "How much would you like to invest? $")
    # # and save it into a variable
    # # NOTE: When you use the `input` function to get user input, what do numbers get saved as?

    to_invest = int(input(f'How much would you like to invest? $'))

    # 1.3 TODO: Uncomment the line below to ask the client which stock they're interested in.
    # NOTE: Take a look at how this input string prints out

    stock_name = input("\nWhich stock are you interested in? Enter the full name:\nAmazon\nApple\nFacebook\nGoogle\nMicrosoft\nStock Name: ")

    # Now that you have all of the client info, you can check how much they can purchase of the stock
    # they're interested in.

    # 1.4 TODO: Use `if/elif/else` conditional logic to determine how much stock the client can buy,
    # and save it in a variable

    # print(f'{client_name} would like to invest {to_invest} in {stock_name} ')
    # print(type(stock_name))
    stocks = 0
    if stock_name == 'Amazon':
        stocks = amazon
    elif stock_name == 'Apple':
        stocks = apple
    elif stock_name == 'Facebook':
        stocks = fb
    elif stock_name == 'Google':
        stocks = google
    elif stock_name == 'Microsoft':
        stocks = msft

    num_stocks = to_invest//stocks

    # if a stock is given, save into a variable

    # 1.5 TODO: Once you've calculated the number of stocks that can be purchased,
    # Use an f-string to print the result for the client, ala:
    # Alex has $5000 to invest and can buy 50 shares of Apple at the current price of $100.
    # print(f'person has {$} to invest in {company}')

    print(f'{client_name} has ${to_invest} to invest and can buy {num_stocks} shares of {stock_name} at the current price of ${stocks}.')

    
stock_purchases()

# I am writing a dictionary to simplify this page of code by using a dictionary
def buy_stocks():

    stocks = {
        'amazon' : '3000',
        'apple' : '100',
        'fb' : '250',
        'google' : '1400',
        'msft' : '200',
    }

    client_name = input('What is your name? ')
    to_invest = int(input(f'How much would you like to invest? $'))
    stock_name = input("\nWhich stock are you interested in? Enter the full name:\nAmazon\nApple\nFacebook\nGoogle\nMicrosoft\nStock Name: ")

    for stock in stocks:
        if stock == stock_name:
            num_stock = int(to_invest / stocks[stock])
            print(f'{client_name} has ${to_invest} to invest and can buy {num_stock} shares of {stock_name} at the current price of ${stocks[stock]}.')

buy_stocks()
