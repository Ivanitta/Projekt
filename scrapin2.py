import csv

soubor = open('scraping.csv', 'w', encoding='utf-8')
scraping = csv.writer(soubor, delimiter=',')

from requests_html import HTMLSession

session = HTMLSession()
stranka = session.get('https://www.zakonyprolidi.cz/cs/1992-634?text=634%2F1992')
stranka.html.render(scrolldown=30, sleep=0.5)


for paragraf in stranka.html.find('.Frags'):# .L2'):
  scraping.writerow([paragraf.text])

soubor.close()

#<a href="/zakony/1992/601/zakon-605-1992-Sb-nariadenie-vlady-slovenskej-republiky-o-vedeni-evidence-odpadov-SB1992605">605/1992 Sb.</a>