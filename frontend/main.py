from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList, OneLineListItem, TwoLineListItem
from kivymd.uix.button import MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout

Window.size = (400, 630)


#add screens to screen manager/screen helper
screen_helper = """
ScreenManager:
    Home:
    ProfileScreen:
    QuestionScreen:
    LogIn:
    First:
    Error:
    Food:
    Transport:
    Fashion:
    Home:
    Habits:
    Location:
    Dilemmas:
    Signup:
    Personalize:
    Navbar:
    ToolBar:
    ResetPassword:
    NewPassword:
    SignupLater:

#screens                             
<Home>:
    name: 'home'
       #toolbar   
    
    FloatLayout:
        Image:
            id: img
            source: 'img/Dinosavvy.png'
            pos_hint: {'center_x': 0.5,'center_y': 0.8}
            size_hint: (0.2,0.2)
    
    MDRoundFlatButton:
        text: '        Personalize'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'profile'
    
    MDLabel:
        text: 'DinoSavvy'
        halign: "center"
        theme_text_color: "Primary"
        font_style: "H3"
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
    
    MDLabel:
        text: 'Thanks for caring'
        halign: "center"
        theme_text_color: "Primary"
        font_style: "H6"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    
    MDRoundFlatButton:
        text: '         Ask a question'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: root.manager.current = 'question'
    
    MDIconButton
        icon: 'account-arrow-right'
        pos_hint: {'center_x': 0.4, 'center_y': 0.3}
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
    
    MDIconButton
        icon: 'comment-question-outline'
        pos_hint: {'center_x': 0.375, 'center_y': 0.2}
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
    
   
<ProfileScreen>:
    name: 'profile'
    
    MDLabel:
        text: 'Personalize'
        halign: 'center'
    
    MDRoundFlatButton:
        text: 'New User'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'signup'
    
    MDRoundFlatButton:
        text: 'Already have an account? Log in'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: root.manager.current = 'login'
    
    MDTextButton:
        text: "Skip"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.85, 'center_y': 0.1}
        on_press: root.manager.current = 'question'
    
    MDIconButton:
        icon: "home"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: root.manager.current = 'home'    
            
<SignupLater>:
    name: 'signuplater'
    
    MDLabel:
        text: 'Create to save dilemma'
        theme_text_color: "Primary"
        font_style: "H4"
        pos_hint: {'center_x': 0.57, 'center_y': 0.92}
        
    MDLabel:
        text: 'Just one more step so we can save your preferences'
        font_style: "H6"
        pos_hint:{'center_x': 0.47, 'center_y': 0.82}
        halign: 'left'
        size_hint: (0.8, 0.5)
    
    MDTextField:
        hint_text: "Enter username"
        helper_text: "Usernames can't contain spaces"
        helper_text_mode: "on_focus"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.7}
        size_hint_x:None
        width:330
    
    MDTextField:
        hint_text: "Enter email"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        size_hint_x:None
        width:330
    
    MDTextField:
        hint_text: "Enter password"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:330
    
    MDTextField:
        hint_text: "Repeat password"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.4}
        size_hint_x:None
        width:330
    
    MDIconButton:
        icon: "home"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: root.manager.current = 'home'
    
    MDTextButton:
        text: "Back"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.25, 'center_y': 0.1}
        on_press: root.manager.current = 'profile'

    MDTextButton:
        text: "Create account"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.78, 'center_y': 0.35}
        on_press: root.manager.current = 'habits'
  
    MDTextButton:
        text: "Skip"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.85, 'center_y': 0.1}
        on_press: root.manager.current = 'habits'
        
<Signup>:
    name: 'signup'
    
    MDLabel:
        text: 'Great Job!'
        theme_text_color: "Primary"
        font_style: "H4"
        pos_hint: {'center_x': 0.57, 'center_y': 0.92}
        
    MDLabel:
        text: 'Just one more step so we can save your preferences'
        font_style: "H6"
        pos_hint:{'center_x': 0.47, 'center_y': 0.82}
        halign: 'left'
        size_hint: (0.8, 0.5)
    
    MDTextField:
        hint_text: "Enter username"
        helper_text: "Usernames can't contain spaces"
        helper_text_mode: "on_focus"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.7}
        size_hint_x:None
        width:330
    
    MDTextField:
        hint_text: "Enter email"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        size_hint_x:None
        width:330
    
    MDTextField:
        hint_text: "Enter password"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:330
    
    MDTextField:
        hint_text: "Repeat password"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.4}
        size_hint_x:None
        width:330
    
    MDIconButton:
        icon: "home"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: root.manager.current = 'home'
    
    MDTextButton:
        text: "Back"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.25, 'center_y': 0.1}
        on_press: root.manager.current = 'profile'

    MDTextButton:
        text: "Create account"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.78, 'center_y': 0.35}
        on_press: root.manager.current = 'habits'
  
    MDTextButton:
        text: "Skip"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.75, 'center_y': 0.1}
        on_press: root.manager.current = 'habits'
        
   
<LogIn>:
    name: 'login'
    
    MDTextField:
        hint_text: "Enter email"
        helper_text: "forgot username? use your email"
        helper_text_mode: "on_focus"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        size_hint_x:None
        width:300
    
    MDTextField:
        hint_text: "Enter password"
        helper_text: "or click on forgot password"
        helper_text_mode: "on_focus"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:300
    
    MDRoundFlatButton:
        text: 'Log in'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'question'
    
    MDTextButton:
        text: "Forgot password"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.73, 'center_y': 0.45}
        on_press: root.manager.current = 'reset'
    
    MDIconButton:
        icon: "redo"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.75, 'center_y': 0.1}
        on_press: root.manager.current = 'question'
    
    MDIconButton:
        icon: "home"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: root.manager.current = 'home'
    
    MDTextButton:
        text: "Back"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.25, 'center_y': 0.1}
        on_press: root.manager.current = 'profile'

<ResetPassword>:
    name: 'reset'
    
    MDLabel:
        text: 'Reset password'
        theme_text_color: "Primary"
        font_style: "H5"
        pos_hint: {'center_x': 0.57, 'center_y': 0.92}
    
    MDTextField:
        hint_text: "Enter email"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        size_hint_x:None
        width:300
          
    MDTextButton:
        text: "Reset password"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.73, 'center_y': 0.55}
        on_press: root.manager.current = 'newpassword'
    
    MDIconButton:
        icon: "redo"
        pos_hint: {'center_x': 0.75, 'center_y': 0.1}
        on_press: root.manager.current = 'question'
    
    MDIconButton:
        icon: "home"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: root.manager.current = 'home'
    
    MDTextButton:
        text: "Back"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.25, 'center_y': 0.1}
        on_press: root.manager.current = 'profile'

<NewPassword>:
    name: 'newpassword'
    
    MDLabel:
        text: 'Set your new password'
        theme_text_color: "Primary"
        font_style: "H5"
        pos_hint: {'center_x': 0.57, 'center_y': 0.92}
            
    
    MDTextField:
        hint_text: "Enter username"
        helper_text: "Usernames can't contain spaces"
        helper_text_mode: "on_focus"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.7}
        size_hint_x:None
        width:330
    
    MDTextField:
        hint_text: "Enter email"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        size_hint_x:None
        width:330
    
    MDTextField:
        hint_text: "Enter password"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:330
    
    MDTextField:
        hint_text: "Repeat password"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.4}
        size_hint_x:None
        width:330
    
    MDIconButton:
        icon: "home"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: root.manager.current = 'home'
    
    MDTextButton:
        text: "Back"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.25, 'center_y': 0.1}
        on_press: root.manager.current = 'reset'

    MDTextButton:
        text: "Save new password"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.73, 'center_y': 0.35}
        on_press: root.manager.current = 'question'
  
    MDTextButton:
        text: "Skip"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.75, 'center_y': 0.1}
        on_press: root.manager.current = 'question'

<QuestionScreen>:
    name: 'question'
    
    MDLabel:
        text: 'Ask a question'
        halign: 'center'
    
    MDIconButton:
        icon: "account"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.85, 'center_y': 0.1}
        on_press: root.manager.current = 'home'   
        
    MDFloatingActionButtonSpeedDial:
        callback: app.call
        data: 
            {'Facebook': 'facebook',
            'Twitter': 'twitter',
            'Linkedin': 'linkedin',
            'Other': 'share-variant'}
        root_button_anim: True
        hint_animation: True 
        bg_hint_color: app.theme_cls.primary_light
    
    MDIconButton:
        icon: "home"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: root.manager.current = 'home'
        
    MDTextButton:
        text: "Back"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.25, 'center_y': 0.1}
        on_press: root.manager.current = 'location'

      
    MDTextButton:
        text: "Skip"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.85, 'center_y': 0.1}
        on_press: root.manager.current = 'habits'
        
<ToolBar>:
    name: 'toolbar'
    BoxLayout:
        orientation: 'vertical'
        
        MDToolbar:
            title: 'Demo Application'
            left_action_items: [["menu", lambda x: app.navigation_draw()]]
            right_action_items: [["dots-vertical", lambda x: app.callback()], ["clock", lambda x: app.callback_2()]]
            elevation:5
            
        MDLabel:
            text: 'hello world'
            halign: 'center'



<Habits>:
    name: 'habits'
    
    MDLabel:
        text: 'Habits'
        halign: "center"
        theme_text_color: "Primary"
        font_style: "H4"
        pos_hint: {'center_x': 0.20, 'center_y': 0.92}
    
    MDLabel:
        text: 'Select what applies to you'
        halign: "center"
        theme_text_color: "Primary"
        font_style: "H5"
        pos_hint: {'center_x': 0.42, 'center_y': 0.85}
    
    MDIconButton:
        icon: "home"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: root.manager.current = 'home'
        
    MDTextButton:
        text: "Back"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.25, 'center_y': 0.1}
        on_press: root.manager.current = 'profile'
    
    MDIconButton:
        icon: "repeat"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.45, 'center_y': 0.92}
        size_hint: (0.5, 0.5)
        user_font_size: "35sp"
  
    

    MDTextButton:
        text: "Skip"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.75, 'center_y': 0.1}
        on_press: root.manager.current = 'location'
    
    MDTextButton:
        text: "Remember my habits"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.71, 'center_y': 0.18}
        on_press: root.manager.current = 'location'
  

<Location>:
    name: 'location'
    MDLabel:
        text: 'Where are you'
        halign: "center"
        theme_text_color: "Primary"
        font_style: "H4"
        pos_hint: {'center_x': 0.4, 'center_y': 0.92}
        size_hint: (0.8, 0.5)
    
    MDIconButton:
        icon: "map-marker"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.2  , 'center_y': 0.8}
        size_hint: (0.5, 0.5)
        user_font_size: "35sp"

    MDIconButton:
        icon: "home"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: root.manager.current = 'home'
    
    MDTextButton:
        text: "Back"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.25, 'center_y': 0.1}
        on_press: root.manager.current = 'location'

      
    MDTextButton:
        text: "Skip"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.75, 'center_y': 0.1}
        on_press: root.manager.current = 'habits'
"""
##Define screen classes

class SignupLater(Screen):
    pass
class NewPassword(Screen):
    pass
class ResetPassword(Screen):
    pass
class ToolBar(Screen):
    pass
class Home(Screen):
    pass
class ProfileScreen(Screen):
    pass
class QuestionScreen(Screen):
    pass
class LogIn(Screen):
    pass
class First(Screen):
    pass
class Personalize(Screen):
    pass
class Error(Screen):
    pass
class Food(Screen):
    pass
class Transport(Screen):
    pass
class Fashion(Screen):
    pass
class Home(Screen):
    pass
class Location(Screen):
    pass
class Dilemmas(Screen):
    pass
class Settings(Screen):
    pass
class Navbar(Screen):
    pass
class Signup(Screen):
    pass
class Habits(Screen):
    def load_table(self):
        layout = AnchorLayout()
        self.data_tables = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(0.8, 0.6),
            check=True,
            rows_num=10,
            column_data=[
                ("", dp(12)),
                ("Habits", dp(45))],
            row_data=[
                ("", "Eat meat alternatives"),
                ("", "Vegeterian"),
                ("", "Use cars minimally"),
                ("", "Fly less"),
                ("", "Sort out garbage"),
                ("", "Carpool"),
                ("", "Minimize single use plastics"),
                ("", "Package free shopping")]
                                 )

        self.add_widget(self.data_tables)
        return layout

    def on_row_press(self, instance_table, instance_row):
        print(instance_table, instance_row)

    def on_check_press(self, instance_table, current_row):
        print(instance_table, current_row)

    def on_enter(self):
        self.load_table()




# Create the screen manager
sm = ScreenManager()
sm.add_widget(Home(name='home'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(QuestionScreen(name='question'))
sm.add_widget(First(name='first'))
sm.add_widget(Error(name='error'))
sm.add_widget(Food(name='food'))
sm.add_widget(Transport(name='transport'))
sm.add_widget(Fashion(name='fashion'))
sm.add_widget(Home(name='home'))
sm.add_widget(Habits(name='habits'))
sm.add_widget(Location(name='location'))
sm.add_widget(LogIn(name='login'))
sm.add_widget(Dilemmas(name='dilemmas'))
sm.add_widget(Signup(name='signup'))
sm.add_widget(Personalize(name='personalize'))
sm.add_widget(Navbar(name='navbar'))
sm.add_widget(ToolBar(name='toolbar'))




class DinosavvyApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen

    def call(self, button):
        print('called from', button)

    class ContentNavigationDrawer(BoxLayout):
        pass

    class DrawerList(ThemableBehavior, MDList):
        pass




DinosavvyApp().run()


