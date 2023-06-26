# %% [markdown]
# ## extraindo gsup

# %%
import requests
from bs4 import BeautifulSoup

# Define the URL of the web page you want to scrape
url = "https://blog.gsuplementos.com.br/como-escolher-whey/"  # Replace with the actual URL of the page

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url)
html_content = response.text

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Find the desired elements on the page (e.g., paragraphs, headings, etc.)
# and extract the text from them
text_list = []
for element in soup.find_all(["p", "h1", "h2", "h3"]):
    text_list.append(element.get_text())

# Define the path and filename for the text file
txt_filename = "extracted_text_gsup.txt"

# Write the extracted text to the text file
with open(txt_filename, mode="w", encoding="utf-8") as file:
    file.write("\n".join(text_list))

print("Text extracted and saved to", txt_filename)

# %%
import requests
from bs4 import BeautifulSoup

# Define the URL of the web page you want to scrape
url = "https://blog.gsuplementos.com.br/whey-protein-concentrado-ou-isolado/" # Replace with the actual URL of the page

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url)
html_content = response.text

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Find the desired elements on the page (e.g., paragraphs, headings, etc.)
# and extract the text from them
text_list = []
for element in soup.find_all(["p", "h1", "h2", "h3"]):
    text_list.append(element.get_text())

# Define the path and filename for the text file
txt_filename = "extracted_text_gsup.txt"

# Append the extracted text to the text file
with open(txt_filename, mode="a", encoding="utf-8") as file:
    file.write("\n".join(text_list) + "\n")

# %%
import requests
from bs4 import BeautifulSoup

# Define the URL of the web page you want to scrape
url = "https://blog.gsuplementos.com.br/whey-protein-para-emagrecer/" # Replace with the actual URL of the page

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url)
html_content = response.text

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Find the desired elements on the page (e.g., paragraphs, headings, etc.)
# and extract the text from them
text_list = []
for element in soup.find_all(["p", "h1", "h2", "h3"]):
    text_list.append(element.get_text())

# Define the path and filename for the text file
txt_filename = "extracted_text_gsup.txt"

# Append the extracted text to the text file
with open(txt_filename, mode="a", encoding="utf-8") as file:
    file.write("\n".join(text_list) + "\n")

# %%
import requests
from bs4 import BeautifulSoup

# Define the URL of the web page you want to scrape
url = "https://blog.gsuplementos.com.br/whey-protein-para-emagrecer/" # Replace with the actual URL of the page

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url)
html_content = response.text

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Find the desired elements on the page (e.g., paragraphs, headings, etc.)
# and extract the text from them
text_list = []
for element in soup.find_all(["p", "h1", "h2", "h3"]):
    text_list.append(element.get_text())

# Define the path and filename for the text file
txt_filename = "extracted_text_gsup.txt"

# Append the extracted text to the text file
with open(txt_filename, mode="a", encoding="utf-8") as file:
    file.write("\n".join(text_list) + "\n")

# %%
import requests
from bs4 import BeautifulSoup

# Define the URL of the web page you want to scrape
url = "https://blog.gsuplementos.com.br/whey-para-intolerantes-a-lactose/" # Replace with the actual URL of the page

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url)
html_content = response.text

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Find the desired elements on the page (e.g., paragraphs, headings, etc.)
# and extract the text from them
text_list = []
for element in soup.find_all(["p", "h1", "h2", "h3"]):
    text_list.append(element.get_text())

# Define the path and filename for the text file
txt_filename = "extracted_text_gsup.txt"

# Append the extracted text to the text file
with open(txt_filename, mode="a", encoding="utf-8") as file:
    file.write("\n".join(text_list) + "\n")

# %%
import requests
from bs4 import BeautifulSoup

# Define the URL of the web page you want to scrape
url = "https://blog.gsuplementos.com.br/whey-com-leite/" # Replace with the actual URL of the page

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url)
html_content = response.text

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Find the desired elements on the page (e.g., paragraphs, headings, etc.)
# and extract the text from them
text_list = []
for element in soup.find_all(["p", "h1", "h2", "h3"]):
    text_list.append(element.get_text())

# Define the path and filename for the text file
txt_filename = "extracted_text_gsup.txt"

# Append the extracted text to the text file
with open(txt_filename, mode="a", encoding="utf-8") as file:
    file.write("\n".join(text_list) + "\n")

# %%
import requests
from bs4 import BeautifulSoup

# Define the URL of the web page you want to scrape
url = "https://blog.gsuplementos.com.br/albumina-ou-whey/" # Replace with the actual URL of the page

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url)
html_content = response.text

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Find the desired elements on the page (e.g., paragraphs, headings, etc.)
# and extract the text from them
text_list = []
for element in soup.find_all(["p", "h1", "h2", "h3"]):
    text_list.append(element.get_text())

# Define the path and filename for the text file
txt_filename = "extracted_text_gsup.txt"

# Append the extracted text to the text file
with open(txt_filename, mode="a", encoding="utf-8") as file:
    file.write("\n".join(text_list) + "\n")

# %%
import requests
from bs4 import BeautifulSoup

# Define the URL of the web page you want to scrape
url = "https://blog.gsuplementos.com.br/melhor-whey-para-ganhar-massa-muscular/" # Replace with the actual URL of the page

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url)
html_content = response.text

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Find the desired elements on the page (e.g., paragraphs, headings, etc.)
# and extract the text from them
text_list = []
for element in soup.find_all(["p", "h1", "h2", "h3"]):
    text_list.append(element.get_text())

# Define the path and filename for the text file
txt_filename = "extracted_text_gsup.txt"

# Append the extracted text to the text file
with open(txt_filename, mode="a", encoding="utf-8") as file:
    file.write("\n".join(text_list) + "\n")

# %%
import requests
from bs4 import BeautifulSoup

# Define the URL of the web page you want to scrape
url = "https://blog.gsuplementos.com.br/whey-protein-substitui-refeicao/" # Replace with the actual URL of the page

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url)
html_content = response.text

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Find the desired elements on the page (e.g., paragraphs, headings, etc.)
# and extract the text from them
text_list = []
for element in soup.find_all(["p", "h1", "h2", "h3"]):
    text_list.append(element.get_text())

# Define the path and filename for the text file
txt_filename = "extracted_text_gsup.txt"

# Append the extracted text to the text file
with open(txt_filename, mode="a", encoding="utf-8") as file:
    file.write("\n".join(text_list) + "\n")

# %%
import requests
from bs4 import BeautifulSoup

# Define the URL of the web page you want to scrape
url = "https://blog.gsuplementos.com.br/whey-engorda/" # Replace with the actual URL of the page

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url)
html_content = response.text

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Find the desired elements on the page (e.g., paragraphs, headings, etc.)
# and extract the text from them
text_list = []
for element in soup.find_all(["p", "h1", "h2", "h3"]):
    text_list.append(element.get_text())

# Define the path and filename for the text file
txt_filename = "extracted_text_gsup.txt"

# Append the extracted text to the text file
with open(txt_filename, mode="a", encoding="utf-8") as file:
    file.write("\n".join(text_list) + "\n")

# %%
import requests
from bs4 import BeautifulSoup

# Define the URL of the web page you want to scrape
url = "https://blog.gsuplementos.com.br/whey-antes-ou-depois-do-treino/" # Replace with the actual URL of the page

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url)
html_content = response.text

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Find the desired elements on the page (e.g., paragraphs, headings, etc.)
# and extract the text from them
text_list = []
for element in soup.find_all(["p", "h1", "h2", "h3"]):
    text_list.append(element.get_text())

# Define the path and filename for the text file
txt_filename = "extracted_text_gsup.txt"

# Append the extracted text to the text file
with open(txt_filename, mode="a", encoding="utf-8") as file:
    file.write("\n".join(text_list) + "\n")
