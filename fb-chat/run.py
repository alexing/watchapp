# -*- coding: UTF-8 -*-

from fbchat import log, Client
import urllib.request
import re
from credentials import fb_user, fb_pass
import dill


SERVER_URL = "https://thawing-tundra-47662.herokuapp.com/sentence/"


def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

with open('../model.pickle', 'rb') as f:
    model = dill.load(f)

def predict(msg):
    return model.predict(msg)[0], model.prob_to_bully[0]


# Subclass fbchat.Client and override required methods
class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        if (thread_id == '1830046933735687'): # test just in our group
            self.markAsDelivered(author_id, thread_id)
            self.markAsRead(author_id)

            #log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

            user = client.fetchUserInfo(message_object.author)
            name  = user[message_object.author].name
            #string_url = SERVER_URL + '?sentence=' + message_object.text.replace(" ","_") + '&user=' + name.replace(" ","_")
            #r = urllib.request.urlopen(string_url).read().decode("utf-8")
            print("%s sent '%s'" % (name, message_object.text))
            #print(cleanhtml(r))
            bullyied = predict(message_object.text)[0]
            prob = predict(message_object.text)[1]
            if bullyied:
                print("%s is bullying. Probability: %.03f %%" % (message_object.text, prob))

client = EchoBot(fb_user, fb_pass)
client.listen()