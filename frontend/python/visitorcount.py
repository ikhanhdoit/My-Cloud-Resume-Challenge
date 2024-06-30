import requests

def get_visitors():
    url = 'https://i2c9mq7v59.execute-api.us-east-1.amazonaws.com/default/VisitorCounter'
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Assuming you want to print the data and return it (similar to console.log and return data; in JavaScript)
        print(data)
        return data
        
    except Exception as e:
        print(f"Error occurred: {e}")

# Calling the function to initiate the GET request
get_visitors()