import requests
from bs4 import BeautifulSoup




# if company name is more than one word
# company = "Goldman-Sachs"
def get_question(company_name,baseurl="https://www.geeksforgeeks.org/"):
    print(company_name)
    company = company_name
    urltopic = baseurl + company + "-topics-interview-preparation"
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
    r = requests.get(urltopic,headers = headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    div = soup.find('div', id = "primary")
    ol = div.find_all("ol")
    return ol

def getps(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
    r1 = requests.get(url, headers = headers)
    soup1 = BeautifulSoup(r1.content, 'html.parser')
    article = soup1.find('article', class_ = True)

    div1 = article.find("div", class_ = "text") 

    ps = div1.find_all("p")
    # ps[0].get_text()
    if "Recommended" in ps[0].get_text():
        index = ps[0].get_text().index("Recommended")
    elif "We strongly recommend you to minimize your browser and try this yourself first." in ps[0].get_text():
        index = ps[0].get_text().index("We strongly recommend you to minimize your browser and try this yourself first.")
    else:
        index = len(ps[0].get_text())

    ps_and_eg = ps[0].get_text()[:index]
    divtags = soup1.find_all("div", class_ = "improved")
    if len(divtags) == 0:
        tags = []
    else:
        t = divtags[1]

        tg = t.find_all("li")

        tags = []
        for i in tg:
            for tag in i.find_all("a", href = True):
                if tag.get_text() not in tags:
                    tags.append(tag.get_text())

    img = div1.find("img", src = True)
    if img:
        return ps_and_eg, img["src"],tags
    else:
        return ps_and_eg, "", tags
 
 
 
   
def easy_question(ol):        
    easy = ol[0].find_all("a", limit = 20)
    easylinks = [] 
    for i in easy:
        l = []
        if len(i.get_text()) < 120:
            l.append(i.get_text())
        else:
            continue 
        l.append(i["href"])
        easylinks.append(l) 
          
    return easylinks
        
     
 
  
def medium_question(ol):
    medium = ol[1].find_all("a", limit = 50)
    mediumlinks=[]    
    for i in medium:
        
        l = []
        l.append(i.get_text())
        l.append(i["href"])
        mediumlinks.append(l)
    
    return mediumlinks
        
    # for i in mediumlinks:   
    #     ps_and_eg, img, tags = getps(i[1])
    #     i.append(ps_and_eg)
    #     i.append(img)
    #     i.append(tags)
    
    # return mediumlinks  
   
        
    
def hard_question(ol): 
    hard = ol[2].find_all("a", limit = 50)
    hardlinks=[] 
     
    for i in hard:
        l = []
    l.append(i.get_text())
    l.append(i["href"])
    hardlinks.append(l)
    return hardlinks
      
    # for i in hardlinks:    
    #     ps_and_eg, img, tags = getps(i[1])
    #     i.append(ps_and_eg)
    #     i.append(img)
    #     i.append(tags)
    # return i
         
 
     

        
 
   
        
