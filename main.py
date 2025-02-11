from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime

Builder.load_file("design.kv")

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"
    def login(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)

        if uname in users and users[uname]["password"] == pword:
            self.manager.current= "login_screen_success"
        else:
            self.ids.login_wrong.text = "username or password is wrong"
            

class SignUpScreen(Screen):
    def add_user(self, uname,pword):
        with open("users.json") as file:
            users = json.load(file)

        users[uname] = {
            'username' : uname,
            'password' : pword,
            'created' : datetime.now().strftime("%Y -%m- %d %H:%M:%S")
            }
        with open("users.json", "w") as file:
            json.dump(users, file)

        self.manager.current = "sign_up_screen_success"

class LoginScreenSucces(Screen):
    def search_countries(self, search_term):
        search_term = search_term.lower()

        with open("countries.txt") as file:
            all_countries = file.readlines()

        search_result = [country for country in all_countries if search_term in country.lower()]

        if search_result:
            self.ids.countries.text = ''.join(search_result)
        else:
            self.ids.countries.text = "No results found. try again ..."

    def log_out(self):
        self.manager.current = "login_screen"



class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.current = "login_screen"


class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget
    


if __name__ == "__main__":
    MainApp().run()

