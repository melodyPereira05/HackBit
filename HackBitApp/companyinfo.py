import requests
from bs4 import BeautifulSoup

urls = {"Google" : "https://www.glassdoor.co.in/Reviews/Google-Reviews-E9079.htm", 
        "Amazon" : "https://www.glassdoor.co.in/Reviews/Amazon-Reviews-E6036.htm",
        "Samsung" : "https://www.glassdoor.co.in/Reviews/Samsung-Electronics-Reviews-E3363.htm",
        "Microsoft" : "https://www.glassdoor.co.in/Reviews/Microsoft-Reviews-E1651.htm",
        "Adobe" : "https://www.glassdoor.co.in/Reviews/Adobe-Reviews-E1090.htm",
        "Oracle" : "https://www.glassdoor.co.in/Reviews/Oracle-Reviews-E1737.htm",
        "Flipkart" : "https://www.glassdoor.co.in/Reviews/Flipkart-Reviews-E300494.htm",
        "Facebook" : "https://www.glassdoor.co.in/Reviews/Facebook-Reviews-E40772.htm",
        "Goldman-Sachs" : "https://www.glassdoor.co.in/Reviews/Goldman-Sachs-Reviews-E2800.htm",
        "D-E-Shaw" : "https://www.glassdoor.co.in/Reviews/D-E-Shaw-India-Reviews-E351722.htm",
        "Cisco" : "https://www.glassdoor.co.in/Reviews/Cisco-Systems-Reviews-E1425.htm",
        "Visa" : "https://www.glassdoor.co.in/Reviews/Visa-Inc-Reviews-E3035.htm",
        "Paytm" : "https://www.glassdoor.co.in/Reviews/Paytm-Reviews-E1159356.htm",
        "Morgan-Stanley" : "https://www.glassdoor.co.in/Reviews/Morgan-Stanley-Mumbai-Reviews-EI_IE2282.0,14_IL.15,21_IM1070.htm?filter.iso3Language=eng",
        "SAP-Labs" : "https://www.glassdoor.co.in/Reviews/SAP-Reviews-E10471.htm",
        "MAQ-Software" : "https://www.glassdoor.co.in/Reviews/MAQ-Software-Reviews-E157056.htm",
        "Ola-Cabs" : "https://www.glassdoor.co.in/Reviews/Ola-cabs-Reviews-EI_IE587383.0,3_KH4,8.htm",
        "VMware" : "https://www.glassdoor.co.in/Reviews/VMware-Reviews-E12830.htm",
        "Directi" : "https://www.glassdoor.co.in/Reviews/Directi-Reviews-E250446.htm"}

def getvalues(company_name):
    
    url = urls[company_name]
    #print(url)
    # print(url)

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
    r = requests.get(url,
                    headers = headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    div = soup.find('div', class_ = "empLinks")

    gd = []

    reviews = div.find("a", class_ = "reviews")
    span = reviews.find("span", class_ = "num h2")
    gd.append(span.get_text().replace(" ", ""))

    jobs = div.find("a", class_ = "jobs")
    span = jobs.find("span", class_ = "num h2")
    gd.append(span.get_text().replace(" ", ""))

    salaries = div.find("a", class_ = "salaries")
    span = salaries.find("span", class_ = "num h2")
    gd.append(span.get_text().replace(" ", ""))

    interviews = div.find("a", class_ = "interviews")
    span = interviews.find("span", class_ = "num h2")
    gd.append(span.get_text().replace(" ", ""))

    benefits = div.find("a", class_ = "benefits")
    span = benefits.find("span", class_ = "num h2")
    gd.append(span.get_text().replace(" ", ""))

    # returns [reviews, jobs, salaries, interviews, benefits]
    return gd
    

def getreviews(company_name):
    url = urls[company_name]
    print(url)

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
    r = requests.get(url,
                    headers = headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    
    r = soup.find_all("li", class_ = "empReview")
    #print(r)
    ls = []
    for i in r:        
        l = {}
        for date, title, desig, start, pros, cons in zip(i.find_all("time", class_ = "date subtle small"),
                                                        i.find_all("h2", class_ = "h2 summary strong mb-xsm mt-0"),
                                                        i.find_all("span", class_ = "authorJobTitle middle"),
                                                        i.find_all("p", class_ = "mainText mb-0"),
                                                        i.find_all("span", {'data-test' : 'pros'}),
                                                        i.find_all("span", {'data-test' : 'cons'})):
            
            
            l["Date"] = date.get_text()
            l["Title"] = title.get_text()
            l["Designation"] = desig.get_text()
            l["Experience"] = start.get_text()
            l["Pros"] = pros.get_text()
            l["Cons"] = cons.get_text()
            
            ls.append(l)
            

    
   
    return ls