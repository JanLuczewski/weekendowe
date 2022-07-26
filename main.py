import csv
import xml.etree.ElementTree as ET
import argparse


output_title = 'output.xml'

def arguments():
    parser = argparse.ArgumentParser(description='robimy output.xml')
    parser.add_argument('plik_csv', metavar='path',type=str, help='podaj sciezke do pliku CSV')
    parser.add_argument('plik_xml',metavar='path',type=str,help=' podaj sciezke do pliku XML')
    args = parser.parse_args()
    input_path_csv = args.plik_csv
    input_path_xml = args.plik_xml
    if not '.csv' in input_path_csv:
        raise TypeError("csv path should be csv extension")
    if not '.xml' in input_path_xml:
        raise TypeError("xml path should be xml extension")
    return input_path_xml, input_path_csv



# csv_file = 'clients.csv'
def get_clientlist(input_path_csv):
    with open(input_path_csv) as f:
        reader = csv.reader(f)
        clients_list = []
        for row in reader:
            clients_list.append(row[0])
        return clients_list

def get_outputxml(input_path_xml,input_path_csv):
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

    tree.write(output_title)

if __name__ == "__main__":
    input_path_xml, input_path_csv = arguments()
    wynik = get_outputxml('clients.xml','clients.csv')
    print(wynik)

