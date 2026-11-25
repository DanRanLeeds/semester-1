
import httpx

base_url = "https://dummyjson.com/"

content = {"q": "apple"}

url = base_url + "products/search"  # API request

response = httpx.get(url, params=content)   # API call

print(response.status_code)   # HTTP response

content = response.json()   # JSON data

print(content)
