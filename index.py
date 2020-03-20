from bs4 import BeautifulSoup
import requests
extract_contents = lambda row: [x.text.replace('\n', '') for x in row]
list=[]
try:
    response=requests.get("https://www.mohfw.gov.in/").content
    soup = BeautifulSoup(response, 'html5lib')
    table=soup.findAll("tr")
    header=table[0].find_all('th')
    head=[]
    for i in header:
        head.append(i.text)
    
    list.append(head)
    
    for rows in table[1:]:
        u=[]
        tds=rows.find_all('td')
        for i in tds:
            u.append(i.text)
        list.append(u)
    print(list)
    
except:
    print("Network Failure")


