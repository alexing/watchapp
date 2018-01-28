from yowsup.stacks                             import YowStackBuilder
from yowsup.common                             import YowConstants
from yowsup.layers                             import YowLayerEvent
from layer                                     import EchoLayer
from yowsup.layers.auth                        import YowAuthenticationProtocolLayer
from yowsup.layers.coder                       import YowCoderLayer
from yowsup.layers.network                     import YowNetworkLayer
from yowsup.env                                import YowsupEnv

#Uncomment to log
#import logging
#logging.basicConfig(level=logging.DEBUG)

CREDENTIALS = ("972526536533", "/qZFcnNqkvUzrrpeouSD5v3nevE=") #replace with your phone and password
#alexx
#login: b'972585396433'
#pw: b'/VLmO0ZjyqCpFLJtF7Z4DJcBVMM='
#itai
#login: b'972526536533'
#pw: b'/qZFcnNqkvUzrrpeouSD5v3nevE='


if __name__==  "__main__":
    stackBuilder = YowStackBuilder()

    stack = stackBuilder\
        .pushDefaultLayers(True)\
        .push(EchoLayer)\
        .build()

    stack.setProp(YowAuthenticationProtocolLayer.PROP_CREDENTIALS, CREDENTIALS)       #setting credentials
    stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))          #sending the connect signal
    stack.setProp(YowNetworkLayer.PROP_ENDPOINT, YowConstants.ENDPOINTS[0])           #whatsapp server address
    stack.setProp(YowCoderLayer.PROP_DOMAIN, YowConstants.DOMAIN)
    stack.setProp(YowCoderLayer.PROP_RESOURCE, YowsupEnv.getCurrent().getResource())  #info about us as WhatsApp client

    stack.loop( timeout = 0.5, discrete = 0.5 )