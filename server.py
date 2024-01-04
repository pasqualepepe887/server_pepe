import anvil.server
import firebase_admin
from firebase_admin import credentials,db
import cloudinary.uploader
import base64

cloudinary.config(
    cloud_name='drlrfdo08',
    api_key='568928172849913',
    api_secret='a2s0zR25Z0ixa4qDr7E9JR_W8-c'
)

#FIREBASE DATABASE
cred = credentials.Certificate("noleggio-pepe-firebase-adminsdk-vmuqg-29e86a8564.json")
firebase_admin.initialize_app(cred,{'databaseURL':'https://noleggio-pepe-default-rtdb.europe-west1.firebasedatabase.app'})

ref_perc=db.reference('/perc/perc')
ref=db.reference('/request_type') #OTTENGO STATE MESS O PDF  FALSE= PDF TRUE= MESS
ref_link_pdf=db.reference('/link_pdf')
ref_mess=db.reference('/message_send')


anvil.server.connect("server_TYF5IUURVJEKZLPY4XNM7WLH-TEHN3KLAOTVZ6ZXW")

@anvil.server.callable()
def get_perc():
               perc= ref_perc.get()
               print("GET PERC")
               return perc
      
@anvil.server.callable()     
def set_state(value):
               ref.set(value)
               print("SET STATE")
              
 
@anvil.server.callable()
def set_mess(mess):
               ref_mess.set(mess)
               print("SET MESS")
     
      
@anvil.server.callable()     
def set_pdf(pdf_encode):
            
               upload_result = cloudinary.uploader.upload("data:application/pdf;base64," + pdf_encode)

# Ottieni l'URL del file caricato
               file_url = upload_result['secure_url']

               print(f'File caricato con successo: {file_url}')
               ref_link_pdf.set(file_url)
               print("SET PDF")
               return  file_url
              
      
anvil.server.wait_forever()
