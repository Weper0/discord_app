import _variables
import urllib.request
from xml.dom import minidom


cmd = "iplookup"
url = "http://ip-api.com/xml/"

def iplookup(client, message):
    if message.content.startswith(_variables.prefix + cmd + ' '):
        user_message = str(message.content).replace(_variables.prefix + cmd + ' ', '')

        with urllib.request.urlopen(url + user_message) as xml:
            xml_str = xml.read()
        xmldoc = minidom.parseString(xml_str)

        countries = xmldoc.getElementsByTagName('country')
        cities = xmldoc.getElementsByTagName('city')

        if len(countries) > 0:
            country = countries[0].firstChild.nodeValue
            city = cities[0].firstChild.nodeValue
            if len(str(message.content)) > len(_variables.prefix + cmd + ' '):
                yield from client.send_message(message.channel, 'Country: ' + country + " | City: " + city)
        else:
            yield from client.send_message(message.channel, 'Invalid IP address.')

