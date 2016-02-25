import os
import subprocess

from mastermind.proxyswitch import enable, disable
from mastermind import handlers, driver

def request(context, flow):
    handlers.request(context, flow)

def response(context, flow):
    handlers.response(context, flow)

def start(context, argv):
    context.source_dir = argv[1]
    context.reverse_access = argv[2] == "True"
    context.without_proxy_settings = argv[3] == "True"
    context.port = argv[4]
    context.host = argv[5]
    context.storage_dir = argv[6]

    driver.register(context)

    if not context.without_proxy_settings:
        context.log("No OS proxy settings")
        enable(context.host, context.port)

    if context.reverse_access:
        reverse_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../reverse.py')
        reverse = subprocess.Popen(['python', reverse_path])
        print("Reverse proxy PID: {}".format(reverse.pid))

    context.log('Source dir: {}'.format(context.source_dir))

def done(context):
    if not context.without_proxy_settings:
        disable()
