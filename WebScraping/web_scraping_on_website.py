from time import sleep
from requests_html import HTML, HTMLSession

session = HTMLSession()
res = session.get('https://coreyms.com/')

data = res.html

articles = data.find('article')

for article in articles:
    headline = article.find('.entry-title-link', first=True).text
    text = article.find('div.entry-content', first=True).text
    link = article.find('iframe', first=True)
    print(link)
    print(link.src)
    sleep(5)


