from bs4 import BeautifulSoup
import requests
URL=input("Δωσε μια διευθυνση")
page=requests.get(URL)
code=BeautifulSoup(page.text, 'lxml')
newlines,links=0,0
link=code.find_all('a')
links=len(link)
br=code.find_all('br')
p=code.find_all('p')
newlines=len(p)+len(br)
print("Στην διευθυνση υπαρχουν",links,"συνδεσμοι και",newlines,"αλλαγες γραμης")
