from bs4 import BeautifulSoup

SIMPLE_HTML = '''<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <h1>This is a title</h1>

    <p class="subtitle">Lorem ipsum dolor sit amet, consectetur adipisicing elit. </p>
    <p>Here's another p without a class </p>

    <ul>
      <li>Rolf</li>
      <li>Charlie</li>
      <li>Jen</li>
      <li>Jose</li>
    </ul>
  </body>
</html>
'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')


def find_title():
    h1_tag = simple_soup.find('h1')
    print(h1_tag.string)


def find_list_items():
    list_items = simple_soup.find_all('li')
    list_contents = [e.string for e in list_items]
    print(list_contents)


def find_subtitle():
    paragraph = simple_soup.find('p', {'class': 'subtitle'})
    print(paragraph.string)


def find_other_paragraph():
    paragraphs = simple_soup.find_all('p')
    other_paragraph = [p for p in paragraphs if 'subtitle' not in p.attrs.get('class', [])]
    print(other_paragraph[0].string)


find_list_items()
find_title()
find_subtitle()
find_other_paragraph()
