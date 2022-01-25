#/usr/bin/python3
#import itertools ## https://www.geeksforgeeks.org/python-iterate-multiple-lists-simultaneously/
import requests, re, time
from email import header
from bs4 import BeautifulSoup as BSoup
from selenium import webdriver

chromedriver = 'C:/Users/admin/OneDrive/chromedriver/chromedriver.exe'
driver = webdriver.Chrome(chromedriver)

url = 'https://www.makeuseof.com/css-background-gradients/'

driver.get(url)

time.sleep(4)
#Para poder leer toda la pagina hay que hacer scroll hasta el final
# de la pagina y esperar(time.sleep()) que el browser haga 'rendering'
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

time.sleep(4)
#wait for page to load

bs_obj = BSoup(driver.page_source, 'html.parser')

# headers = {
#     'User-Agent':
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
#     "Content-Type": "application/x-www-form-urlencoded"
# }

## 💥Trate de usar request para cargar la pagina, da error si no uso
## la option de headers.

# response = requests.get(url6, headers=headers)
# bs_obj = BSoup(response.text, 'html.parser')

#Close el webdriver, sino se queda abierto el browser
driver.close()

# images = bs_obj.findAll('img')
# images = bs_obj.find('article').findAll('h2')

gradient_name = bs_obj.findAll('h2')
gradient_code = bs_obj.findAll('code')

#for debugging.. para ver la pagina completa
# print(bs_obj.prettify())

#Usar el title de la pagina para crear el filename, pero eliminando todo especial characters
fname = bs_obj.title
# print(fname)

# removing special characters from a list of items in python
fname = ([re.sub('[^a-zA-Z0-9]+', '', _) for _ in fname])
print(fname)
f = open(''.join(fname), "w")

#for debugging
# f.write(bs_obj.prettify())

code_and_name_to_save = '\n'

j = 0
i = 0
for name in gradient_name:
    j += 1
    code_and_name_to_save = code_and_name_to_save + name.text

for code in gradient_code:
    i += 1
    code_and_name_to_save = code_and_name_to_save + code.text + '\n'

# i = 0
# for code in gradient_code:
#     i += 1
#     code_and_name_to_save = code_and_name_to_save + str(
#         i) + " " + code.text + '\n'
#     print(code)
# f.write(code.text + '\n')
# print(i, " ", code.text)

# save text to file
f.write(code_and_name_to_save)

print(len(gradient_code))
print(len(gradient_name))
#cerrar file
f.close()

###😟😧😎 Verificar que hace esta parte del codigo (jeje no me acuerdo para que lo puse 😊)
f = open(''.join(fname), 'r')
lines = f.readlines()

# regex = r"^http.*.gif"
regex = r"^http.*.png"
# https://regex101.com/r/evkgYU/1/
# https://regex101.com/r/evkgYU/1/codegen?language=python

# las Lines que siguen despues del for loop son de este site, tiene un code generator

for line in lines:
    matches = re.finditer(regex, line)
    for matchNum, match in enumerate(matches, start=1):
        print("{match}".format(matchNum=matchNum,
                               start=match.start(),
                               end=match.end(),
                               match=match.group()))
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            print("Group {groupNum} found at {start}-{end}: {group}".format(
                groupNum=groupNum,
                start=match.start(groupNum),
                end=match.end(groupNum),
                group=match.group(groupNum)))
f.close()
