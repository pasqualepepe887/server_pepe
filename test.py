from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button


from github import Github
import requests

g = Github('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')
global event_name,secret_key

event_name = "server_pepe"
secret_key = "mhZ1uRCTBxO0cF7-b7B8XCJ-NCGSq5HYmZcPzqbbM3_"


global repo
repo = g.get_repo('pasqualepepe887/server_pepe')



global file_select

#background_color="#0099ff"

class Server_Pepe(App):
    def build(self):
        layout = GridLayout()
        layout.cols=1
        layout.size_hint=(0.8,0.9)
        layout.pos_hint={"center_x":0.5,"center_y":0.5}
        Window.size=(360,640)
        #layout = BoxLayout(orientation='vertical')
        file_chooser = FileChooserIconView(font_name='date/Tektur-Black',filters=['*.pdf'])
    
        label_start = Label(font_name='date/Tektur-Black',text="Server Pepe",font_size="50sp",color="#007dd1",bold=True)
        
        layout.add_widget(label_start)

        buttonjh = Label(size_hint=(None,None),height=30)
        layout.add_widget(buttonjh)
        state = Image(source="date/moon.png",size_hint=(None,None),size=(300,50))
        layout.add_widget(state)
        buttonj = Label(size_hint=(None,None),height=40)
        layout.add_widget(buttonj)

        button = Button(background_normal = 'date/up.png',size_hint=(None,None),size=(300,300),background_down = 'date/upd.png')
        button.bind(on_release=lambda btn: self.show_selected_files(file_chooser,layout,button,label_start,state,buttonjh,buttonj))
        layout.add_widget(button)
       # buttonh = Label(size_hint=(None,None),height=50)
       # layout.add_widget(buttonh)
        
        return layout



    def show_selected_files(self, file_chooser,layout,button,label_start,state,buttonjh,buttonj):
        layout.remove_widget(button)
        layout.remove_widget(label_start)

        layout.add_widget(file_chooser)

        layout.remove_widget(button)
        layout.remove_widget(state)
        layout.remove_widget(buttonjh)
        layout.remove_widget(buttonj)
        buttoncar = Label(size_hint=(None,None),height=40)
        layout.add_widget(buttoncar)
        button = Button(font_name='date/Tektur-Black',font_size="30sp",color="#007dd1",bold=True,text="CARICA", size_hint=(1, None), height=40,background_color="#000000",border= (16, 16, 30, 30))
        button.bind(on_release=lambda btn: self.carica(file_chooser,layout,button,buttoncar))
        layout.add_widget(button)


    def carica(self,file_chooser,layout,button,buttoncar):
        global file_select
        selected_files = file_chooser.selection
            # print(len(selected_files))
        if len(selected_files) != 0:
                for file_path in selected_files:
                   print(file_path)
                   file_select = file_path
                   file_old=repo.get_contents("test.pdf")
                   with open(file_path, 'rb') as file:
                    data = file.read()

                   repo.update_file("test.pdf", 'offerte', content= data, sha=file_old.sha)
                   file.close()


                url = f"https://maker.ifttt.com/trigger/{event_name}/json/with/key/{secret_key}"
                response = requests.post(url)
    
                layout.remove_widget(file_chooser)
                layout.remove_widget(button)
                layout.remove_widget(buttoncar)
        
                label_start = Label(font_name='date/Tektur-Black',text="Server Pepe",font_size="50sp",color="#007dd1",bold=True)
        
        
                layout.add_widget(label_start) 
                        
                buttonjh = Label(size_hint=(None,None),height=30)
                layout.add_widget(buttonjh)
                if response.status_code == 200:
                     print("Evento IFTTT attivato con successo!")
                     state = Image(source="date/sun.png",size_hint=(None,None),size=(300,50))

                else:
                     print("Errore durante l'attivazione dell'evento IFTTT.")
                     state = Image(source="date/moon.png",size_hint=(None,None),size=(300,50))
               # state = Image(source="moon.png",size_hint=(None,None),size=(300,50))
                layout.add_widget(state)
                buttonj = Label(size_hint=(None,None),height=40)
                layout.add_widget(buttonj)


                button = Button(background_normal = 'date/up.png',size_hint=(None,None),size=(300,300),background_down = 'date/upd.png')
                button.bind(on_release=lambda btn: self.show_selected_files(file_chooser,layout,button,label_start,state,buttonjh,buttonj))
                layout.add_widget(button)

                    
               


    
               
       
            



Server_Pepe().run()