import _variables
import xml.etree.ElementTree as ET

cmd = "iplookup"

def iplookup(client, message):
    if message.content.startswith(_variables.prefix + cmd + ' '):
        user_message = str(message.content).replace(_variables.prefix + cmd + ' ', '')

        tree = ET.parse('http://ip-api.com/xml/' + 'user_message')
        root = tree.getroot()

        country = root[0][1].text
        city = root[0][5].text

        if len(str(message.content)) > len(_variables.prefix + cmd + ' '):
            yield from client.send_message(message.channel, 'Country: ' + country + " | City: " + city)