import requests

def convert_curr():
    initial_currency = input("Enter the currency to be converted from: ")
    target_currency = input("Enter the  currency to be converted to: ")

    while True:
        try:
            amount = float(input('Enter the amount to be convterted: '))
        except:  # noqa: E722
            print('The amount needs to be numeric')
            continue
            
        if amount < 0:
            print('Amount needs to be greater than 0')
            continue
        else:
            break
    
    url = f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={initial_currency}&amount={amount}"

    payload = {}
    headers= {
    "apikey": "7LUfOlLJExbWPZNXQZtOx5PMawYFnqk0"
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    status_code = response.status_code

    if status_code != 200:
        result = response.json()
        print('Error response: ' + str(result))
        quit()

    result = response.json()
    print('Converted currency: ' + str(result['result']))


if __name__ == '__main__':
    convert_curr()