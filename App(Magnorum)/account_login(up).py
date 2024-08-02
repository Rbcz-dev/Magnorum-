from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Purple"
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(Builder.load_file('login.kv'), name='login')
        self.screen_manager.add_widget(Builder.load_file('signup.kv'), name='signup')
        self.screen_manager.add_widget(Builder.load_file('principal.kv'), name='home')
        return self.screen_manager

    def theme(self):
        if self.theme_cls.theme_style == 'Light':
            self.theme_cls.theme_style = 'Dark'
        elif self.theme_cls.theme_style == 'Dark':
            self.theme_cls.theme_style = 'Light'

    def toggle_password(self):
        login_screen = self.screen_manager.get_screen('login')
        senha_input = login_screen.ids.senha_input
        toggle_button = login_screen.ids.toggle_button
        if senha_input.password:
            senha_input.password = False
            toggle_button.icon = 'eye'
            senha_input.icon_right = 'eye'
        else:
            senha_input.password = True
            toggle_button.icon = 'eye-off'
            senha_input.icon_right = 'eye-off'

    def toggle_password_s(self):
        signup_screen = self.screen_manager.get_screen('signup')
        senha_s_input = signup_screen.ids.senha_s_input
        confirm_s_input = signup_screen.ids.confirm_s_input
        toggle_s = signup_screen.ids.toggle_s
        if senha_s_input.password and confirm_s_input.password:
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

if __name__ == "__main__":
    MainApp().run()
