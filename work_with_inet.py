import requests

url = 'https://pypi.org/project/pylint-flask/'
url_picture = 'https://moemisto.ua/img/cache/blog_show_photo/blog/0004/75/fe2a5835d6d62a84d64cc357061c8186a244a1a8.jpeg?hash=2020-03-02-20-38-21'
url_git = 'https://github.com/progit/progit2/releases/download/2.1.434/progit.pdf'

response = requests.get(url_picture)

# with open('spring.jpeg', mode='wb') as file:
#     file.write(response.content)
#
# with open('spring.jpeg', mode='ab') as file:
#     file.write(b'hello from Odesa')
#

# with open('spring.jpeg', mode='rb') as file:
#     data = file.read()
#     pass
# response2 = requests.get(url_git)
#
# with open('git.pdf', mode='wb') as file:
#     file.write(response2.content)
