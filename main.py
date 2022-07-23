import csv
import xml.etree.ElementTree as ET

def get_clientlist(csv_file):
    csv_file = 'clients.csv'
    with open(csv_file) as f:
        reader = csv.reader(f)
        clients_list = []
        for row in reader:
            clients_list.append(row[0])
        return clients_list

xml_file = 'clients.xml'
tree = ET.parse(xml_file)
root = tree.getroot()
print(root.find("clients"))
for client in root.find("clients").findall("client"):
    if client.attrib['name'] in get_clientlist(csv_file='clients.csv'):
        if not client.find("messages"):
            messages = ET.Element("messages")
            client.append(messages)
        messages = client.find("messages")
        message = ET.Element("message")
        message.text = 'huj huj'
        messages.append(message)
tree.write('output.xml')


