import requests

def greet(name) :
    return f"Hello,{name}!"

if __name__ == "__main__" :
    print(greet("Python Class"))

r = requests.get("https://api.github.com")
print("GitHub Status:",r.status_code)
