import csv
from requests_html import HTML, HTMLSession

# We are reading https://coreyms.com/ site here and analysing data
with open('data.csv', 'w') as wtcsv:
    csv_writer = csv.writer(wtcsv)

    session = HTMLSession()
    res = session.get('https://coreyms.com/')

    data = res.html
    articles = data.find('article')

    for article in articles:
        headline = article.find('.entry-title-link', first=True).text
        summary = article.find('div.entry-content', first=True).text
        try:
            link = article.find('iframe', first=True).attrs['src']
            youtube_video_id = link.split('/')[4].split('?')[0]
            youtube_link = 'https://youtube.com/watch?v={}'.format(youtube_video_id)
        except Exception as e:
            youtube_link = None

        csv_writer.writerow([headline, summary, youtube_link])




