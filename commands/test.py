import _variables

cmd = "test"

def test(client, message):
    if message.content.startswith(_variables.prefix + cmd + ' '):
        user_message = str(message.content).replace(_variables.prefix + cmd + ' ', '')
        if len(str(message.content)) > len(_variables.prefix + cmd + ' '):
            yield from client.send_message(message.channel, 'Your message: ' + user_message)