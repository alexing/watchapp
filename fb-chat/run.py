# -*- coding: UTF-8 -*-

from fbchat import log, Client
import urllib.request
import re
SERVER_URL = "https://thawing-tundra-47662.herokuapp.com/sentence/"


def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext


# Subclass fbchat.Client and override required methods
class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        if (thread_id == '1830046933735687'): # test just in our group
            self.markAsDelivered(author_id, thread_id)
            self.markAsRead(author_id)

            #log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

            user = client.fetchUserInfo(message_object.author)
            name  = user[message_object.author].name
            string_url = SERVER_URL + '?sentence=' + message_object.text.replace(" ","_") + '&user=' + name.replace(" ","_")
            r = urllib.request.urlopen(string_url).read().decode("utf-8")
            print("%s sent '%s'" % (name, message_object.text))
            print(cleanhtml(r))

client = EchoBot("alexing10@gmail.com", "Mame32!!")
client.listen()