def convert_string_to_float(price_string):
    # Remove the dollar symbol ('$') and any other non-numeric characters
    cleaned_price = price_string.replace('$', '').replace(',', '')
    # Convert the cleaned price string to a floating-point number
    try:
        price_float = float(cleaned_price)
        return price_float
    except ValueError:
        # Error Handling
        print(f"Error: Unable to convert price string '{price_string}' to float")
        return None

def normalize_price(price_float, bitcoin_price):
    try:
        normalized_price = price_float / bitcoin_price
        return normalized_price
    except ZeroDivisionError:
        print("Error: Bitcoin price is Zero")
        return None
    
def apply_transformation(crypto_data, bitcoin_price):
    transformed_data = []
    for item in crypto_data:
        # Accessing price from 'quote' -> 'USD' -> 'price'
        price = item.get('quote', {}).get('USD', {}).get('price')
        if price is not None:
            # Normalize price directly since it's already a float
            item['price'] = price
            item['normalized_price'] = normalize_price(price, bitcoin_price)
            transformed_data.append(item)
        else:
            print("Error: Unable to find price for item:", item)
    return transformed_data


