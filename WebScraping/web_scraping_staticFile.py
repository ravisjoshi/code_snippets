from requests_html import HTML

with open('sample.html', 'r') as sf:
    source = sf.read()
    html = HTML(html=source)

# # Print the whole html content from the html file
# print(html.html)

# # Print the text for the html file
# print(html.text)

# Find list of articles
articles = html.find('div.article')

for article in articles:
    heading = article.find('h2', first=True).text
    text = article.find('p', first=True).text
    print(heading)
    print(text)
    print()
