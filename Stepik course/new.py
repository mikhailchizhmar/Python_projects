import requests
import re

# link1 = input()
# res1 = requests.get(link1)
# txt = res1.text
txt = ["<a href='http://stepic.org/courses'>",
       "<a href='https://stepic.org'>",
       "<a href='http://neerc.ifmo.ru:1345'>",
       '<a href="ftp://mail.ru/distib" >',
       '<a href="ya.ru">',
       '<a href="www.ya.ru">',
       '<a href="../skip_relative_links">']
# 1. <a href=[\"\'](\w*://)(.+)(?:/|:).*>
# 2. <a href=[\"\'](\w*://)(\w+.\w+)[\"\']>
print(str(txt))
lst1_links = []
lst2_links = []
for string in txt:
    lst1_links += re.findall(r'<a href=[\"\'](?:\w*://)(.+?)/.*[\"\']>', string)
for string in txt:
    lst2_links += re.findall(r'<a href=[\"\'](?:\w*://)(.+?)[\"\']>', string)

print(lst1_links)
print(lst2_links)
# for link in lst1_links:
#     res = requests.get(link)
#     if re.search(link2, res.text):
#         flag = "Yes"
#         break

# if re.search(link2, res1.text):
#     print("No")
# elif re.search(r'{}\w+'.format('/'.join(lst1[:-1])), res1.text):
#     print(re.search(r'{}\w+'.format('/'.join(lst1[:-1])), res1.text))
# print(res.status_code)
# print((res.headers['Content-Type']))
# print(res.content)  # binary
# print(res.text)
# print(lst1)
# print(lst2)
# check <a href>