import csv
import xml.etree.ElementTree as ET
import argparse

parser = argparse.ArgumentParser(description='robimy output.xml')
parser.add_argument('plik_csv', metavar='path',type=str, help='podaj sciezke do pliku CSV')
parser.add_argument('plik_xml',metavar='path',type=str,help=' podaj sciezke do pliku XML')
args = parser.parse_args()
input_path_csv = args.plik_csv
input_path_xml = args.plik_xml



# csv_file = 'clients.csv'
def get_clientlist(input_path_csv):
    with open(input_path_csv) as f:
        reader = csv.reader(f)
        clients_list = []
        for row in reader:
            clients_list.append(row[0])
        return clients_list

def get_outputxml(input_path_xml):
    # xml_file = 'clients.xml'
    tree = ET.parse(input_path_xml)
    root = tree.getroot()
    print(root.find("clients"))
    for client in root.find("clients").findall("client"):
        if client.attrib['name'] in get_clientlist(input_path_csv):
            if client.find("messages") is None:
                messages = ET.Element("messages")
                client.append(messages)
            messages = client.find("messages")
            message = ET.Element("message")
            message.text = 'huj huj'
            messages.append(message)
    tree.write('output.xml')

wynik = get_outputxml('clients.xml')
print(wynik)

