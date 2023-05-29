# 1
from bs4 import BeautifulSoup

def find_title(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    title_tag = soup.title
    if title_tag is not None:
        return title_tag.text.strip()
    else:
        return None


html_doc = '''
<html>
<head>
<title>Це заголовок</title>
</head>
<body>
<p>Це є тіло документа.</p>
</body>
</html>
'''

title = find_title(html_doc)
if title is not None:
    print("Заголовок:", title)
else:
    print("Заголовок не знайдено")



# 2
from bs4 import BeautifulSoup

def get_paragraph_tags(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    p_tags = soup.find_all('p')

    return [tag.get_text() for tag in p_tags]


with open('sample.html', 'r') as file:
    html_content = file.read()

paragraph_tags = get_paragraph_tags(html_content)

for tag in paragraph_tags:
    print(tag)



# 3
from bs4 import BeautifulSoup

def count_paragraph_tags(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    p_tags = soup.find_all('p')

    return len(p_tags)

with open('sample.html', 'r') as file:
    html_content = file.read()

paragraph_count = count_paragraph_tags(html_content)

print("Кількість тегів <p>: ", paragraph_count)



# 4
from bs4 import BeautifulSoup

def get_first_paragraph_text(html_content):

    soup = BeautifulSoup(html_content, 'html.parser')

    p_tag = soup.find('p')

    if p_tag:
        return p_tag.get_text()
    else:
        return None

with open('sample.html', 'r') as file:
    html_content = file.read()

first_paragraph_text = get_first_paragraph_text(html_content)

if first_paragraph_text:
    print("Текст першого тегу <p>: ", first_paragraph_text)
else:
    print("Перший тег <p> не знайдено.")


# 5
from bs4 import BeautifulSoup

def get_first_h2_text_length(html_content):

    soup = BeautifulSoup(html_content, 'html.parser')

    h2_tag = soup.find('h2')

    if h2_tag:
        return len(h2_tag.get_text())
    else:
        return None

with open('sample.html', 'r') as file:
    html_content = file.read()

first_h2_text_length = get_first_h2_text_length(html_content)

if first_h2_text_length:
    print("Довжина тексту першого тегу <h2>: ", first_h2_text_length)
else:
    print("Перший тег <h2> не знайдено.")


# 6
from bs4 import BeautifulSoup

def get_first_a_text(html_content):

    soup = BeautifulSoup(html_content, 'html.parser')

    a_tag = soup.find('a')

    if a_tag:
        return a_tag.get_text()
    else:
        return None

with open('sample.html', 'r') as file:
    html_content = file.read()

first_a_text = get_first_a_text(html_content)

if first_a_text:
    print("Текст першого тегу <a>: ", first_a_text)
else:
    print("Перший тег <a> не знайдено.")


# 7


# 8
from bs4 import BeautifulSoup
import urllib.request

def get_li_urls(url):
    response = urllib.request.urlopen(url)
    html_content = response.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    li_tags = soup.find_all('li')

    urls = []
    for li_tag in li_tags:
        if li_tag.a and 'href' in li_tag.a.attrs:
            urls.append(li_tag.a['href'])

    return urls

url = 'https://example.com'

li_urls = get_li_urls(url)

for li_url in li_urls:
    print(li_url)


# 9
from bs4 import BeautifulSoup
import urllib.request

def find_h2_tags(url):

    response = urllib.request.urlopen(url)
    html_content = response.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    h2_tags = soup.find_all('h2')

    count = 0
    for h2_tag in h2_tags:
        if count < 4:
            print(h2_tag.text)
            count += 1
        else:
            break

url = 'https://example.com'

find_h2_tags(url)


# 10
from bs4 import BeautifulSoup
import urllib.request

def find_link_tags(url):

    response = urllib.request.urlopen(url)
    html_content = response.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    link_tags = soup.find_all('a')

    count = 0
    for link_tag in link_tags:
        if count < 10:
            print(link_tag['href'])
            count += 1
        else:
            break

url = 'https://example.com'

find_link_tags(url)


# 11
from bs4 import BeautifulSoup
import urllib.request

def find_heading_tags(url):

    response = urllib.request.urlopen(url)
    html_content = response.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    heading_tags = soup.find_all(['h1', 'h2', 'h3'])

    heading_list = []
    for heading_tag in heading_tags:
        heading_list.append(heading_tag.text)

    return heading_list

url = 'https://example.com'

headings = find_heading_tags(url)

for heading in headings:
    print(heading)


# 12
from bs4 import BeautifulSoup
import urllib.request

def extract_text_from_webpage(url):

    response = urllib.request.urlopen(url)
    html_content = response.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text()

    return text

url = 'https://example.com'
webpage_text = extract_text_from_webpage(url)

print(webpage_text)


# 13
from bs4 import BeautifulSoup
import urllib.request

def print_html_tags(url):

    response = urllib.request.urlopen(url)
    html_content = response.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    all_tags = soup.find_all()

    for tag in all_tags:
        print(tag.name)

url = 'https://example.com'
print_html_tags(url)


# 14
from bs4 import BeautifulSoup
import urllib.request

def get_nested_tags(url, parent_tag):

    response = urllib.request.urlopen(url)
    html_content = response.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    parent_element = soup.find(parent_tag)
    nested_tags = parent_element.find_all()

    for tag in nested_tags:
        print(tag.name)

url = 'https://example.com'
parent_tag = 'html'
get_nested_tags(url, parent_tag)


# 15
from bs4 import BeautifulSoup
import urllib.request

def get_body_descendants(url):

    response = urllib.request.urlopen(url)
    html_content = response.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    body_tag = soup.find('body')
    descendants = body_tag.descendants

    for descendant in descendants:
        if descendant.name:
            print(descendant.name)

url = 'https://example.com'
get_body_descendants(url)


# 16
from bs4 import BeautifulSoup
import urllib.request

def get_header_info(url):

    response = urllib.request.urlopen(url)
    html_content = response.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    header_tag = soup.find('h1')
    header_html = str(header_tag)
    header_text = header_tag.get_text()
    parent_html = str(header_tag.parent)

    print("HTML код заголовка:")
    print(header_html)
    print("Текст заголовка:")
    print(header_text)
    print("HTML код батьківського елемента:")
    print(parent_html)

url = 'https://example.com'
get_header_info(url)


# 17
from bs4 import BeautifulSoup
import urllib.request

def print_li_tags(url):

    response = urllib.request.urlopen(url)
    html_content = response.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    li_tags = soup.find_all('li')

    for li in li_tags:
        print(li)

url = 'https://example.com'
print_li_tags(url)


# 18
from bs4 import BeautifulSoup
import urllib.request

def print_elements_with_text(url, search_text):

    response = urllib.request.urlopen(url)
    html_content = response.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    elements = soup.find_all(text=lambda text: search_text.lower() in text.lower())

    for element in elements:
        print(element.strip())

url = 'https://example.com'
search_text = 'example'
print_elements_with_text(url, search_text)


# 19
from bs4 import BeautifulSoup
import urllib.request

def print_elements_with_id(url, element_id):

    response = urllib.request.urlopen(url)
    html_content = response.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    elements = soup.find_all(id=element_id)

    for element in elements:
        print(element)

url = 'https://example.com'
element_id = 'my-element'
print_elements_with_id(url, element_id)


# 20
from bs4 import BeautifulSoup

def find_tag_with_attribute(html_content, tag_name, attribute_name, attribute_value):

    soup = BeautifulSoup(html_content, 'html.parser')

    tag = soup.find(tag_name, {attribute_name: attribute_value})

    return tag

html_content = '''
<html>
  <body>
    <h1 id="title">Hello, world!</h1>
    <p class="content">This is a paragraph.</p>
    <a href="https://example.com">Click here</a>
  </body>
</html>
'''

tag_name = 'a'
attribute_name = 'href'
attribute_value = 'https://example.com'
tag = find_tag_with_attribute(html_content, tag_name, attribute_name, attribute_value)

if tag:
    print(tag)
else:
    print("Тег не знайдено.")


# 21
from bs4 import BeautifulSoup

def find_nested_tags(html_content, parent_tag_name):


    soup = BeautifulSoup(html_content, 'html.parser')
    parent_tags = soup.find_all(parent_tag_name)
    nested_tags = []

    for parent_tag in parent_tags:
        # Знаходимо вкладені теги
        children_tags = parent_tag.find_all()
        nested_tags.extend(children_tags)

    return nested_tags

html_content = '''
<html>
  <body>
    <div>
      <h1>Title</h1>
      <p>Paragraph 1</p>
      <p>Paragraph 2</p>
    </div>
    <ul>
      <li>Item 1</li>
      <li>Item 2</li>
      <li>Item 3</li>
    </ul>
  </body>
</html>
'''

parent_tag_name = 'div'

nested_tags = find_nested_tags(html_content, parent_tag_name)

if nested_tags:
    for tag in nested_tags:
        print(tag)
else:
    print("Вкладених тегів не знайдено.")


# 22
from bs4 import BeautifulSoup

def find_nested_tags(html_content, parent_tag_name):
    soup = BeautifulSoup(html_content, 'html.parser')

    parent_tags = soup.find_all(parent_tag_name)

    nested_tags = []

    for parent_tag in parent_tags:
        children_tags = parent_tag.find_all()
        nested_tags.extend(children_tags)

    return nested_tags

html_content = '''
<html>
  <body>
    <div>
      <h1>Title</h1>
      <p>Paragraph 1</p>
      <p>Paragraph 2</p>
    </div>
    <ul>
      <li>Item 1</li>
      <li>Item 2</li>
      <li>Item 3</li>
    </ul>
  </body>
</html>
'''

parent_tag_name = 'div'
nested_tags = find_nested_tags(html_content, parent_tag_name)

if nested_tags:
    for tag in nested_tags:
        print(tag)
else:
    print("Вкладених тегів не знайдено.")


# 23
from bs4 import BeautifulSoup

def replace_tag_content(html_content, tag_name, new_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    tags = soup.find_all(tag_name)

    if tags:
        for tag in tags:
            # Замінюємо вміст тегу на новий рядок
            tag.string = new_content
    return soup.prettify()

html_content = '''
<html>
  <body>
    <h1>Title</h1>
    <p>Paragraph 1</p>
    <p>Paragraph 2</p>
  </body>
</html>
'''

tag_name = 'p'
new_content = 'New Paragraph'
modified_html = replace_tag_content(html_content, tag_name, new_content)

print(modified_html)


# 24
from bs4 import BeautifulSoup

def add_content_to_tag(html_content, tag_name, new_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    tag = soup.find(tag_name)

    if tag:
        tag.append(new_content)
    return soup.prettify()

html_content = '''
<html>
  <body>
    <h1>Title</h1>
    <p>Paragraph 1</p>
    <p>Paragraph 2</p>
  </body>
</html>
'''

tag_name = 'p'
new_content = 'Additional content'

modified_html = add_content_to_tag(html_content, tag_name, new_content)

print(modified_html)


# 25
def insert_text_in_url(url, new_text, position):

    part1 = url[:position]
    part2 = url[position:]
    new_url = part1 + new_text + part2
    return new_url

url = "https://example.com/page.html"
new_text = "new"
position = 12

modified_url = insert_text_in_url(url, new_text, position)

print(modified_url)


# 26
from bs4 import BeautifulSoup

def insert_before_tag(html, tag_name, new_content):

    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all(tag_name)

    for tag in tags:
        new_element = soup.new_tag(tag_name) if tag.name != 'script' else ''
        new_element.string = new_content
        tag.insert_before(new_element)
    return str(soup)

html = """
<html>
<body>
<p>Це абзац 1</p>
<p>Це абзац 2</p>
<p>Це абзац 3</p>
</body>
</html>
"""
tag_name = 'p'
new_content = 'Новий абзац'
modified_html = insert_before_tag(html, tag_name, new_content)

print(modified_html)


# 27
from bs4 import BeautifulSoup

def insert_after_tag(html, tag_name, new_content):

    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all(tag_name)

    for tag in tags:
        new_element = soup.new_tag(tag_name) if tag.name != 'script' else ''
        new_element.string = new_content
        tag.insert_after(new_element)
    return str(soup)

html = """
<html>
<body>
<p>Це абзац 1</p>
<p>Це абзац 2</p>
<p>Це абзац 3</p>
</body>
</html>
"""
tag_name = 'p'
new_content = 'Новий абзац'
modified_html = insert_after_tag(html, tag_name, new_content)

print(modified_html)


# 28
from bs4 import BeautifulSoup

def remove_tag_content(html, tag_name):

    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all(tag_name)

    for tag in tags:
        tag.string = ''
    return str(soup)

html = """
<html>
<body>
<p>Це абзац 1</p>
<p>Це абзац 2</p>
<p>Це абзац 3</p>
</body>
</html>
"""
tag_name = 'p'
modified_html = remove_tag_content(html, tag_name)

print(modified_html)


# 29
from bs4 import BeautifulSoup

def remove_tag(html, tag_name):

    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all(tag_name)

    for tag in tags:
        tag.extract()
    return str(soup)

html = """
<html>
<body>
<h1>Це заголовок</h1>
<p>Це абзац</p>
</body>
</html>
"""
tag_name = 'p'
modified_html = remove_tag(html, tag_name)

print(modified_html)


# 30
from bs4 import BeautifulSoup

def remove_tag_and_contents(html, tag_name):
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all(tag_name)

    for tag in tags:
        tag.decompose()
    return str(soup)

html = """
<html>
<body>
<h1>Це заголовок</h1>
<p>Це абзац</p>
</body>
</html>
"""
tag_name = 'p'
modified_html = remove_tag_and_contents(html, tag_name)

print(modified_html)


# 31
from bs4 import BeautifulSoup

def replace_tag_or_string(html, old_tag, new_tag_or_string):
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all(old_tag)

    for tag in tags:
        if isinstance(new_tag_or_string, str):
            tag.string = new_tag_or_string
        else:
            tag.replace_with(new_tag_or_string)
    return str(soup)

html = """
<html>
<body>
<h1>Це заголовок</h1>
<p>Це абзац</p>
</body>
</html>
"""
old_tag = 'p'
new_tag = '<div>Новий тег</div>'
modified_html = replace_tag_or_string(html, old_tag, new_tag)

print(modified_html)


# 32
from bs4 import BeautifulSoup

def wrap_element(html, element, wrapper_tag):
    soup = BeautifulSoup(html, 'html.parser')
    elements = soup.find_all(element)

    for el in elements:
        wrapper = soup.new_tag(wrapper_tag)
        el.wrap(wrapper)
    return str(soup)

html = """
<html>
<body>
<p>Це абзац 1</p>
<p>Це абзац 2</p>
<p>Це абзац 3</p>
</body>
</html>
"""
element = 'p'
modified_html = wrap_element(html, element, wrapper_tag)

print(modified_html)


# 33
from bs4 import BeautifulSoup

def replace_tag_with_content(html, tag):
    soup = BeautifulSoup(html, 'html.parser')
    elements = soup.find_all(tag)

    for el in elements:
        el.replace_with(el.contents)
    return str(soup)

html = """
<html>
<body>
<p>Це абзац 1</p>
<p>Це абзац 2</p>
<p>Це абзац 3</p>
</body>
</html>
"""
tag = 'p'
modified_html = replace_tag_with_content(html, tag)

print(modified_html)
