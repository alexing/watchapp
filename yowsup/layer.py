# -*- coding: utf-8 -*-
import os, subprocess, time
from yowsup.layers.interface                           import YowInterfaceLayer                 #Reply to the message
from yowsup.layers.interface                           import ProtocolEntityCallback            #Reply to the message
from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity         #Body message
from yowsup.layers.protocol_presence.protocolentities  import AvailablePresenceProtocolEntity   #Online
from yowsup.layers.protocol_presence.protocolentities  import UnavailablePresenceProtocolEntity #Offline
from yowsup.layers.protocol_presence.protocolentities  import PresenceProtocolEntity            #Name presence
from yowsup.layers.protocol_chatstate.protocolentities import OutgoingChatstateProtocolEntity   #is writing, writing pause
from yowsup.common.tools                               import Jid                               #is writing, writing pause

#Log, but only creates the file and writes only if you kill by hand from the console (CTRL + C)
#import sys
#class Logger(object):
#    def __init__(self, filename="Default.log"):
#        self.terminal = sys.stdout
#        self.log = open(filename, "a")
#
#    def write(self, message):
#        self.terminal.write(message)
#        self.log.write(message)
#sys.stdout = Logger("/1.txt")
#print "Hello world !" # this is should be saved in yourlogfilename.txt
#------------#------------#------------#------------#------------#------------

allowedPersons=['44xxxxxxxxx','44xxxxxxxxx'] #Filter the senders numbers
ap = set(allowedPersons)

name = "NAMEPRESENCE"
filelog = "/root/.yowsup/Not allowed.log"

class EchoLayer(YowInterfaceLayer):
    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        if messageProtocolEntity.getFrom() == '972526536533-1516886955@g.us':
            #TODO: THIS JUST FILTER IMAGES
            #TODO: STOP THOSE FUCKING LOG MESSAGES!
            #TODO: GET USER NAMES!
            if messageProtocolEntity.getType() == 'text': #our group's id
                print("""
                %s said:
                %s
                """%(messageProtocolEntity.getParticipant(), messageProtocolEntity.body))
            else:
                print("""
                %s sent a non text message
                """ % (messageProtocolEntity.getParticipant()))
            #print("""
        #%s said:
        #%s
        #""" %(messageProtocolEntity.from, messageProtocolEntity.body))


    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        print(entity.ack())
        self.toLower(entity.ack())

    def onTextMessage(self,messageProtocolEntity):
        pass