from twisted.internet.defer import inlineCallbacks

from autobahn.twisted.util import sleep
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
from autobahn.wamp.types import SubscribeOptions
import time

class Component(ApplicationSession):
    @inlineCallbacks
    def onJoin(self, details):
        def onevent(msg, details=None):
            print(f"Boing. {msg}")
            print(f"Topic: {details.topic}")


        def join_topic(self, channel):
            print("Debugging")

        yield self.subscribe(onevent, u'com.pylon.register', options=SubscribeOptions(details_arg='details'))
        yield self.subscribe(onevent, u'com.pylon.SERIAL', options=SubscribeOptions(details_arg='details'))
        self.publish(u'com.pylon.SERIAL', '{"request":"request", "type":"raw_command", "name":"ls", "command": "ls"}')
        sleep(5)
        self.publish(u'com.pylon.SERIAL', '{"request":"status"}')
        sleep(5)
        self.publish(u'com.pylon.SERIAL', '{"request":"status"}')
        sleep(5)
        self.publish(u'com.pylon.SERIAL', '{"request":"status"}')
        sleep(5)
        self.publish(u'com.pylon.SERIAL', '{"request":"status"}')
        sleep(5)
        self.publish(u'com.pylon.SERIAL', '{"request":"status"}')
if __name__ == '__main__':
    runner = ApplicationRunner(url=u"ws://localhost:8080/ws", realm=u"realm1")
    runner.run(Component)