import json
import subprocess
import time


class request:
    def __init__(self, request_json):
        request = json.loads(request_json)
        self.request = {}
        if 'ignore_output' in request and request['ignore_output'] is True:
            self.ignore_output = True
            del request['ignore_output']
        else:
            self.ignore_output = False
        for key, value in request.items():
            self.request[key] = value


        self.handle_request()

    def handle_request(self):
        self.acknowledge()
        self.process()
        self.result()

    def acknowledge(self):
        self.set_status('ack')
        self.send()
        print("Order Acknowledged!")

    def send(self):
        print("Sending...")
        print(json.dumps(self.request))

    def process(self):
        self.set_status('processing')
        print(f"I'm going to run {self.get_property('command')}")
        self.run_command(self.get_property('command'))

    def result(self):
        self.set_status('result')
        self.send()

    def set_property(self, property, value):
        self.request[property] = value

    def set_status(self, status):
       self.set_property('request', status)

    def get_property(self, property):
        return self.request[property]

    def run_command(self, command):
        pid = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

        pid.wait()

        output = pid.communicate()[0]
        print(output)
        if not self.ignore_output:
            self.set_property('output', output.decode('utf-8'))
        self.set_property('exit', pid.returncode)
