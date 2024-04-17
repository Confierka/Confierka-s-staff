from http.server import BaseHTTPRequestHandler,HTTPServer
import os
from urllib.parse import parse_qs
import telebot
import threading

html="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    {}
</body>
</html>
"""

bot = telebot.TeleBot('6275842632:AAFmpv6pyKwt_vCezKcASCEq4CL3HZ8QDzE')

admin_id=678832767


threading.Thread(target=bot.polling).start()

clients=[]

class MyHandler(BaseHTTPRequestHandler):
    def return_file(self, filename,errCode=200):


        self.send_response(errCode)
        self.end_headers()

        

        with open(filename,'rb') as file:
            self.wfile.write(file.read())
    
    def return_clients(self):
        self.send_response(200)
        self.end_headers()

        res=''
        for client in clients:
            firstName = client['FirstName'][0]
            lastName = client['LastName'][0]
            res += f'{firstName} {lastName}<br/>'
        

        page = html.format(res)
    

        self.wfile.write(page.encode('utf-8'))
            
    def do_GET(self):
        filename = 'files'+self.path
        

        if self.path == "/":
            self.return_file('files/index.html')
        elif self.path == '/client':
            self.return_clients()

        elif os.path.isfile(filename):
            self.return_file(filename)
        

        else:
            self.return_file('files/404.html',404)
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length'))
        body = self.rfile.read(content_length).decode('utf-8')
        
        
        data = parse_qs(body)
        print(data["FirstName"])
        print(data["LastName"])
        firstName = data['FirstName'][0]
        lastName = data['LastName'][0]

        bot.send_message(admin_id, f'First Name:{firstName},Last Name:{lastName}')
        clients.append(data)

        self.return_file('files/submitted.html')

PORT = 8000
httpd = HTTPServer(('',PORT),MyHandler)

print(f"http://localhost:{PORT}/")

httpd.serve_forever()
