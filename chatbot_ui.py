import kivymd
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import textfield
from kivy.core.text import LabelBase
from kivy.properties import StringProperty, NumericProperty
from kivy.clock import Clock
from kivy.uix.image import Image
from kivymd.uix.button import MDRectangleFlatButton

Window.size = (350, 550)


class Command(MDLabel):
    text = StringProperty()
    size_hint_x: NumericProperty()
    halign: StringProperty()
    font_size: 17


class Response(MDLabel):
    text = StringProperty()
    size_hint_x: NumericProperty()
    halign: StringProperty()
    font_size: 17

class ResponseImage(Image):
    source = StringProperty()



class ChatBot(MDLabel):
    pass


class Myapp(MDApp):
    def change_screen(self, name):

        screen_manager.current = name

    @property
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("my.kv"))
        screen_manager.add_widget(Builder.load_file("chat.kv"))

        return screen_manager

    def bot_name(self):
        if screen_manager.get_screen('Main').bot_name.text != "":
            screen_manager.get_screen(
                'Chats').bot_name.text = screen_manager.get_screen('Main').bot_name.text
            screen_manager.current = "Chats"

    def response(self, *args):
        flag = 0
        tmp_flag = 0
        response = ""
        if value == "Hello" or value == "hi" or value == "hii" or value == "Hi" or value == "Hii":
            response = f"Hello I am AI. Please select the que's behind you. 1) Program and Admission  2) Finances and Scholarship 3)Campus and Resources 4)Support and assitance"
            {screen_manager.get_screen('Chats').bot_name.text}
            screen_manager.get_screen('Chats').chat_list.add_widget(
                Response(text=response, size_hint_x=.50))
            
            
        elif value == "How are you" or value == "how are you":

            response = "I am fine thank you"
            screen_manager.get_screen('Chats').chat_list.add_widget(
                Response(text=response, size_hint_x=.50))

        elif value == "Program and Admission" or value == "program and admission" or value == "1":

            response = "1)Degrees your college offer ! \n 2)Admission to your Collage  \n 3)Deadline 4)Enrollment process and Deadline to Enroll"
            screen_manager.get_screen('Chats').chat_list.add_widget(
                Response(text=response, size_hint_x=.50))

        elif value == "Degrees your college offer" or value == "1":
            response = "1) Diploma in IT 2)Diploma in  CM "
            screen_manager.get_screen('Chats').chat_list.add_widget(
                Response(text=response, size_hint_x=.50))
        elif value == "" or value == "do you know chetan gf":
            response = "Yes chetan's GF is Prachi!!"
            screen_manager.get_screen('Chats').chat_list.add_widget(
                Response(text=response, size_hint_x=.50))
        elif value == "" or value == "":
            response = "Sorry i can't do that !"
            screen_manager.get_screen('Chats').chat_list.add_widget(
                Response(text=response, size_hint_x=.50))
        elif value == "You know raj" or value == "you know raj":
            response = MDRectangleFlatButton(text="yes")
            screen_manager.get_screen('Chats').chat_list.add_widget(
                Response(text=response, size_hint_x=.50))
        elif value == "Images":
            screen_manager.get_screen('Chats').chat_list.add_widget(ResponseImage(source="Bot3.png"))    
        elif value =="college image":
            screen_manager.get_screen('Chats').chat_list.add_widget(ResponseImage(source="clg_pic.jpg"))
        else:
            response = " Sorry could you please repeat it !!"
            screen_manager.get_screen('Chats').chat_list.add_widget(
                Response(text=response, size_hint_x=.75))

    def send(self):
        global size, halign, value
        if screen_manager.get_screen('Chats').text_input.text:
            value = screen_manager.get_screen('Chats').text_input.text
            if len(value) < 6:

                size = .22
                halign = "center"
            elif len(value) < 11:
                size = .32
                halign = "center"
            elif len(value) < 16:
                size = .45
                halign = "center"
            elif len(value) < 21:
                size = .58
                halign = "center"
            elif len(value) < 26:
                size = .71
                halign = "center"
            else:
                size = .77
                halign = "left"

            screen_manager.get_screen('Chats').chat_list.add_widget(
                Command(text=value, size_hint_x=size, halign=halign))
            Clock.schedule_once(self.response, 2)
            screen_manager.get_screen('Chats').text_input.text = ""


# LabelBase.register(name="Poppins",fn_regular="Poppins-Regular.ttf")
Myapp().run()
