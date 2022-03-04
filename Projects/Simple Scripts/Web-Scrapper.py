from bs4 import BeautifulSoup
import requests
import csv
# csv_path = os.path.join('C:\\Users\\Kirito\\Desktop\\Programming Codes\\Projects','web_scrp.csv') Can utilize this as well to provide path to the file
URL = 'https://coreyms.com/'
source = requests.get(URL).text # 'requests' method is used to fetch the Html Source code of a site
soup = BeautifulSoup(source,'lxml') 

'''
Beautiful Soup is a Python package for parsing HTML and XML documents (including having malformed markup,
i.e. non-closed tags, so named after tag soup). It creates a parse tree for parsed pages that can be
used to extract data from HTML, which is useful for web scraping.

'lxml' is the best Parser to use along with BeautifulSoup

'''

with open('C:\\Users\\Kirito\\Desktop\\Programming Codes\\Projects\\web_scrp.csv',"w") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Healine','Summary','Youtube Link']) # Providing titles to the Columns
    for article in soup.find_all("article"): #'find_all' finds all instance with matching word,in this case 'article'

        try:
            headline = article.h2.a.text
            para = article.div.p.text
            vid_link = article.find('iframe', class_ = "youtube-player")['src']
            vid_link = vid_link.split('/')[4].split('?')[0]  #Finding the Youtube video alpahanumeric Code

            print(headline)
            print(para)

            yt_link = (f"https://youtube.com/watch?v={vid_link}")
        except Exception as e:
            yt_link = None
        print(yt_link,"\n")

        csv_writer.writerow([headline,para,yt_link])