# API
import os
from flask import Flask, request, send_file
from flask_restful import Resource, Api
from flask_cors import CORS
from twilio.rest import Client
import db_connector as db
import time

app = Flask(__name__) #levanta un servicio por un puerto
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

#cambiar las variables de configuración
account_sid = ''
auth_token = ''

class MESSAGE(Resource):
    def post(self):
        req = request.json
        
        number = request.form['From']
        message_body = request.form['Body'].lower()    
        mensaje =""
                
        client = Client(account_sid, auth_token)
        
        if message_body.find("heart rate") == 0:
          db.create_img(number) #este era el del comment
          mensaje = " "+db.find_user(number)+ " esta es la información actual de tus registros"          
          print(number)
          message = client.messages.create (
          #abajo va el numero de whatsapp de twillio whatsapp:+numero
                                      from_='',
                                      body= mensaje,
                                      #incluir abajo el link de ngrok
                                      media_url=['/image?number='+number],
                                      to= number #el numero de cel de cliente
                                  )
        else:        
          try:          
            mensaje = "Hola "+db.find_user(number)+ " puedes pedirme tu Heart Rate por el momento. Esta es una imagen de como usar el oximetro"
            message = client.messages.create (
                                    body= mensaje,
                                    #incluir abajo el link de ngrok
                                    media_url = ['/getimage'],
                                    #igual que arriba va el numero de twilio
                                    from_='',
                                    to = number
                                )
            print(message.sid)

          except:
            mensaje = "No estas registrado. Escribe ->  Nombre:Ruben Raya  <- todo junto por favor"            
            message = client.messages.create (
            #abajo va el numero de twilio
                                    from_='',
                                    body= mensaje,                   
                                    to= number
                                )                 
            

class IMAGE(Resource):
    def get(self):        
        number = request.args.get('number')
        number = number.replace(": ","_+")        
        print(number)
        filename = number+'.png'
        return send_file(filename, mimetype='image/png')
        
class IMAGE2(Resource):
    def get(self):
        filename = 'tutorial.png'
        return send_file(filename, mimetype='image/png')
    
    
api.add_resource(MESSAGE, '/message')  # Route_1
api.add_resource(IMAGE, '/image')  # Route_2
api.add_resource(IMAGE2, '/getimage')  # Route_2

if __name__ == '__main__':
    app.run(port='5013')
