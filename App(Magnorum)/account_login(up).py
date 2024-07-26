from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.lang import Builder

class LoginScreen(MDScreen):
     def toggle_password(self):
        senha_input = self.ids.senha_input
        toggle_button = self.ids.toggle_button
        if senha_input.password:
            senha_input.password = False
            toggle_button.icon = 'eye'
            senha_input.icon_right = 'eye'
        else:
            senha_input.password = True
            toggle_button.icon = 'eye-off'
            senha_input.icon_right = 'eye-off'

class SignupScreen(MDScreen):
     def toggle_password_s(self):
        senha_s_input = self.ids.senha_s_input
        confirm_s_input= self.ids.confirm_s_input
        toggle_s = self.ids.toggle_s
        if senha_s_input.password and  confirm_s_input.password :
            senha_s_input.password = False
            confirm_s_input.password = False
            toggle_s.icon = 'eye'
            senha_s_input.icon_right = 'eye'
            confirm_s_input.icon_right = 'eye'
        else:
            senha_s_input.password = True
            confirm_s_input.password = True
            toggle_s.icon = 'eye-off'
            senha_s_input.icon_right = 'eye-off'
            confirm_s_input.icon_right = 'eye-off'
class HomeScreen(MDScreen):
    pass
class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Indigo"
        return Builder.load_file('account.kv')
    def theme(self):
        if self.theme_cls.theme_style == 'Light':
            self.theme_cls.theme_style = 'Dark'
        elif self.theme_cls.theme_style == 'Dark':
            self.theme_cls.theme_style = 'Light'
MainApp().run()