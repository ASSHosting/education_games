from livereload import Server
import os

ROOT = os.path.abspath(os.path.dirname(__file__))

server = Server()
server.watch(ROOT)
server.serve(root=ROOT, host='127.0.0.1', port=8000)
