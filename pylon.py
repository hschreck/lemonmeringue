import request
import json
from twisted.internet.defer import inlineCallbacks
from autobahn.wamp.types import SubscribeOptions
from autobahn.twisted.util import sleep
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner

serial = "SERIAL"
class Component(ApplicationSession):
    @inlineCallbacks

    def onJoin(self, details):
        def onevent(msg, details=None):
            print(msg)
            process(msg, details)

        def process(msg, details):
            message = json.loads(msg)
            if details.topic == f"com.pylon.{serial}":
                current_request = request.requestObject(message)
        #TODO: Set this up so that send() requests can be triggered from outside the object
        self.register = yield self.subscribe(onevent, u'com.pylon.register', options=SubscribeOptions(details_arg='details'))
        self.topic = yield self.subscribe(onevent, f"com.pylon.{serial}", options=SubscribeOptions(details_arg='details'))


        self.publish(u'com.pylon.register', serial)
        self.publish(f"com.pylon.{serial}", serial)





if __name__ == '__main__':
    runner = ApplicationRunner(url=u"ws://localhost:8080/ws", realm=u"realm1")
    runner.run(Component)
