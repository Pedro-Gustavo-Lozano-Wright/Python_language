#pip install beautifulsoup4

#https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all
'''
import requests
from bs4 import BeautifulSoup

URL = "https://www.google.com/"

# Realizamos la petición a la web
req = requests.get(URL)

# Comprobamos que la petición nos devuelve un Status Code = 200
status_code = req.status_code

#html = BeautifulSoup(req.text, "html.parser")
#print(html)

if status_code == 200:

    # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
    html = BeautifulSoup(req.text, "html.parser")

    # Obtenemos todos los divs donde están las entradas
    entradas = html.find_all('a')

    # Recorremos todas las entradas para extraer el título, autor y fecha
    for i, entrada in enumerate(entradas):

        print(i, entrada.text)
        # Con el método "getText()" no nos devuelve el HTML
        #titulo = entrada.find('span', {'class': 'tituloPost'}).getText()
        # Sino llamamos al método "getText()" nos devuelve también el HTML
        #autor = entrada.find('span', {'class': 'autor'})

else:
    print ("Status Code %d" % status_code)
'''








'''
r = requests.get('https://www.notion.so/')
soup = BeautifulSoup(r.text, 'lxml')
#print(soup)
print("--")
#resp = requests.get('https://www.google.com/')
# https://gustavo-technology.web.app/#/
titulo = soup.title #incluido la etiqueta
texto = titulo.string
print("--titulo")
print(texto)


inner_div = soup.div.div

print("--inner_div")
print(inner_div)

print("--contents")
hijos = inner_div.contents
for child in hijos:
    if child.name:
        print(f'{child.name}')
        for subchild in child:
            print(f'-{subchild.name}')
            for subsubchild in subchild:
                print(f'--{subsubchild.name}')
                for subsubsubchild in subsubchild:
                    print(f'---{subsubsubchild.name}')


print("--children")


hijos = inner_div.children
for child in hijos:
    if child.name:
        print(f'{child.name}')

print("--descendants")


hijos = inner_div.descendants
for child in hijos:
    if child.name:
        print(f'{(child)}')
'''