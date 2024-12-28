import requests

res = requests.get("https://docs.python.org/3.5/")
print(res.status_code)
print((res.headers['Content-Type']))
print(res.content)  # binary
print(res.text)

image = requests.get("https://docs.python.org/3.5/_static/py.png")
print(image.status_code)
print((image.headers['Content-Type']))
print(image.content)

with open("python.png", "wb") as image_file:
    image_file.write(image.content)
