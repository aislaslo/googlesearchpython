from googlesearch import search

query = input("Google something: ")

for url in search(query, stop=20):
    print(url)