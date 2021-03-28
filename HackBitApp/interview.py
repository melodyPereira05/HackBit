import requests
from bs4 import BeautifulSoup


def getexp(expurl):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
    r1 = requests.get(expurl,headers = headers)
    soup1 = BeautifulSoup(r1.content, 'html.parser')
    article = soup1.find('article', class_ = True)
    div1 = article.find("div", class_ = "text")
    if "If you like GeeksforGeeks" in div1.get_text():
        index = div1.get_text().index("If you like GeeksforGeeks")
    else:
        index = len(div1.get_text())
    return div1.get_text()[:index]

# if company name is more than one word
# company = "Goldman-Sachs"
def get_experience(company_name,baseurl= "https://www.geeksforgeeks.org/"):
    
    company = company_name
    urltopic = baseurl + company + "-interview-preparation/"

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
    r = requests.get(urltopic,
                    headers = headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    div = soup.find_all('div', class_ = "popularArticle")
    t = div[len(div) - 1]
    intexp = t.find_all("a")
    intexp = intexp[:len(intexp) - 1]
    lexp = []
    for i in intexp:
        l = []
        l.append(i["href"])
        l.append(getexp(i["href"]))
        lexp.append(l)    
    return lexp



