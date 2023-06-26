## extraindo nutritotal

# %%
import requests
from bs4 import BeautifulSoup

# Define the URL of the web page you want to scrape
url = "https://nutritotal.com.br/pro/material/whey-protein/"  # Replace with the actual URL of the page

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
txt_filename = "extracted_text_nutritotal.txt"

# Write the extracted text to the text file
with open(txt_filename, mode="w", encoding="utf-8") as file:
    file.write("\n".join(text_list))

print("Text extracted and saved to", txt_filename)

# %%
import requests
from bs4 import BeautifulSoup

# Define the URL of the web page you want to scrape
url = "https://nutritotal.com.br/pro/tv-nutritotal/abreviacao-de-jejum/" # Replace with the actual URL of the page

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
txt_filename = "extracted_text_nutritotal.txt"

# Append the extracted text to the text file
with open(txt_filename, mode="a", encoding="utf-8") as file:
    file.write("\n".join(text_list) + "\n")

# %%
import requests
from bs4 import BeautifulSoup

# Define the URL of the web page you want to scrape
url = "https://nutritotal.com.br/pro/associacao-de-exercicio-e-whey-melhora-quadro-de-obesidade-sarcopenica/" # Replace with the actual URL of the page

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
txt_filename = "extracted_text_nutritotal.txt"

# Append the extracted text to the text file
with open(txt_filename, mode="a", encoding="utf-8") as file:
    file.write("\n".join(text_list) + "\n")

# %%
import requests
from bs4 import BeautifulSoup

# Define the URL of the web page you want to scrape
url = "https://nutritotal.com.br/pro/tv-nutritotal/diana-borges-dock-nascimento-quais-as-vantagens-no-uso-do-whey-protein/" # Replace with the actual URL of the page

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
txt_filename = "extracted_text_nutritotal.txt"

# Append the extracted text to the text file
with open(txt_filename, mode="a", encoding="utf-8") as file:
    file.write("\n".join(text_list) + "\n")

# %%
import requests
from bs4 import BeautifulSoup

# Define the URL of the web page you want to scrape
url = "https://nutritotal.com.br/pro/efeitos-da-suplementaa-a-o-de-whey-soja-e-leucina-combinada-a-programa-de-treinamento-na-composia-a-o-corporal-de-universita-rios/" # Replace with the actual URL of the page

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
txt_filename = "extracted_text_nutritotal.txt"

# Append the extracted text to the text file
with open(txt_filename, mode="a", encoding="utf-8") as file:
    file.write("\n".join(text_list) + "\n")

# %%
import requests
from bs4 import BeautifulSoup

# Define the URL of the web page you want to scrape
url = "https://nutritotal.com.br/pro/material/abreviacao-de-jejum-pre-operatorio/" # Replace with the actual URL of the page

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
txt_filename = "extracted_text_nutritotal.txt"

# Append the extracted text to the text file
with open(txt_filename, mode="a", encoding="utf-8") as file:
    file.write("\n".join(text_list) + "\n")

# %%
import requests
from bs4 import BeautifulSoup

# Define the URL of the web page you want to scrape
url = "https://nutritotal.com.br/pro/atletas-vegetarianos-necessidade-proteica/" # Replace with the actual URL of the page

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
txt_filename = "extracted_text_nutritotal.txt"

# Append the extracted text to the text file
with open(txt_filename, mode="a", encoding="utf-8") as file:
    file.write("\n".join(text_list) + "\n") 

# %%
import requests
from bs4 import BeautifulSoup

# Define the URL of the web page you want to scrape
url = "https://nutritotal.com.br/pro/proteina-do-leite-pode-ajudar-a-prevenir-infeccao-por-sars-cov-2/" # Replace with the actual URL of the page

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
txt_filename = "extracted_text_nutritotal.txt"

# Append the extracted text to the text file
with open(txt_filename, mode="a", encoding="utf-8") as file:
    file.write("\n".join(text_list) + "\n") 

# %%
import requests
from bs4 import BeautifulSoup

# Define the URL of the web page you want to scrape
url = "https://nutritotal.com.br/pro/proteina-do-leite-pode-ajudar-a-prevenir-infeccao-por-sars-cov-2/" # Replace with the actual URL of the page

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
txt_filename = "extracted_text_nutritotal.txt"

# Append the extracted text to the text file
with open(txt_filename, mode="a", encoding="utf-8") as file:
    file.write("\n".join(text_list) + "\n") 

# %%
import requests
from bs4 import BeautifulSoup

# Define the URL of the web page you want to scrape
url = "https://nutritotal.com.br/pro/material/alimentacao-para-ganho-de-massa-muscular/" # Replace with the actual URL of the page

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
txt_filename = "extracted_text_nutritotal.txt"

# Append the extracted text to the text file
with open(txt_filename, mode="a", encoding="utf-8") as file:
    file.write("\n".join(text_list) + "\n") 

# %%
import requests
from bs4 import BeautifulSoup

# Define the URL of the web page you want to scrape
url = "https://nutritotal.com.br/pro/estrategia-para-otimizar-suplementacao-de-idosos-frageis/" # Replace with the actual URL of the page

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
txt_filename = "extracted_text_nutritotal.txt"

# Append the extracted text to the text file
with open(txt_filename, mode="a", encoding="utf-8") as file:
    file.write("\n".join(text_list) + "\n") 

# %%
import requests
from bs4 import BeautifulSoup

# Define the URL of the web page you want to scrape
url = "https://nutritotal.com.br/pro/perfil-nutricional-de-cereais/" # Replace with the actual URL of the page

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
txt_filename = "extracted_text_nutritotal.txt"

# Append the extracted text to the text file
with open(txt_filename, mode="a", encoding="utf-8") as file:
    file.write("\n".join(text_list) + "\n") 

# %%
import requests
from bs4 import BeautifulSoup

# Define the URL of the web page you want to scrape
url = "https://nutritotal.com.br/pro/material/qualidade-dos-suplementos-esportivos/" # Replace with the actual URL of the page

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
txt_filename = "extracted_text_nutritotal.txt"

# Append the extracted text to the text file
with open(txt_filename, mode="a", encoding="utf-8") as file:
    file.write("\n".join(text_list) + "\n") 

# %%
import requests
from bs4 import BeautifulSoup

# Define the URL of the web page you want to scrape
url = "https://nutritotal.com.br/pro/material/lancamento-do-livro-nutricao-esportiva-genetica-estrategias-e-suplementacao/" # Replace with the actual URL of the page

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
txt_filename = "extracted_text_nutritotal.txt"

# Append the extracted text to the text file
with open(txt_filename, mode="a", encoding="utf-8") as file:
    file.write("\n".join(text_list) + "\n") 

# %%
import requests
from bs4 import BeautifulSoup

# Define the URL of the web page you want to scrape
url = "https://nutritotal.com.br/pro/material/lancamento-do-livro-nutricao-esportiva-genetica-estrategias-e-suplementacao/" # Replace with the actual URL of the page

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
txt_filename = "extracted_text_nutritotal.txt"

# Append the extracted text to the text file
with open(txt_filename, mode="a", encoding="utf-8") as file:
    file.write("\n".join(text_list) + "\n") 


