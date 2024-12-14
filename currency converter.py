import requests
def currency_converter():
    amount = float(input("Enter amount: "))
    from_currency = input("Enter from currency: ")
    to_currency = input("Enter to currency: ")
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    rate = data['rates'][to_currency]
    converted_amount = amount * rate
    print(f"{amount} {from_currency} = {converted_amount} {to_currency}")
currency_converter()
