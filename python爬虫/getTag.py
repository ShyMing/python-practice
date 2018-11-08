from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
#获取子标签
# print("child:")
# for child in bsObj.find("table", {"id": "giftList"}).children:
#   print(child)

#获取兄弟标签
# print('brother')
# for silbing in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
#   print(silbing)

#获取父标签
print('parent presibling', bsObj.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())