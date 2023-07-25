import json
import xml.etree.ElementTree as Et
import requests
from bs4 import BeautifulSoup


class Student:
    def __init__(self):
        self.name = "Anonymous"
        self.age = 18


file = open("files/data.json", "r")
json_object = json.load(file)
team = json_object["quiz"]["sport"]["q1"]["options"][1]
print(team)
file.close()

s = Student()
json_student = json.dumps(s.__dict__)
print(json_student)
with open("files/student.json", "w") as f:
    json.dump(s.__dict__, f)

xml_tree = Et.parse("files/data.xml")
root = xml_tree.getroot()
print(root.tag)
print(root[0].get('name'))
counter = 0
for x in root.findall("country"):
    print(root[counter][0].tag, ':', root[counter][0].text)
    counter += 1

page = requests.get("http://google.com")
soup = BeautifulSoup(page.content, features="html.parser")
link_list = soup.find_all("a")
for link in link_list:
    print(link)




