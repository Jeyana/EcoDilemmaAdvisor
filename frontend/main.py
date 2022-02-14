from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList, OneLineListItem, TwoLineListItem
from kivymd.uix.button import MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
from navigation_drawer import navigation_helper
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.text import LabelBase

Window.size = (400, 630)

#add screens to screen manager
screen_helper = """
ScreenManager:
    Home:
    Personalize:
    QuestionScreen:
    QuestionScreen2:
    QuestionScreen3:
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
    Navbar:
    ToolBar:
    ResetPassword:
    NewPassword:
    SignupLater:
    SavedQuestions:
    QuestionList:
    QuestionList2:
    Profile:
    NewEmail:

#screens                             
<Home>:
    name: 'home'
        
    FloatLayout:
        Image:
            id: img
            source: 'img/Dinosavvy.png'
            pos_hint: {'center_x': 0.5,'center_y': 0.75}
            size_hint: (0.2,0.2)

    MDRoundFlatIconButton:
        icon: 'account-arrow-right'
        text: 'Personalize'
        font_name:"DMSans"
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'personalize'
    
    MDLabel:
        text: 'Welcome to'
        halign: "center"
        theme_text_color: "Primary"
        font_name:"DMSans"
        font_style: "H6"
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}
    
    MDLabel:
        text: 'EcoDilemmaAdvisor'
        halign: "center"
        theme_text_color: "Primary"
        font_name:"DMSans"
        font_style: "H4"
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        
    MDLabel:
        text: 'Thanks for caring'
        halign: "center"
        theme_text_color: "Primary"
        font_style: "H6"
        font_name:"DMSans"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    
    MDFillRoundFlatIconButton:
        icon: 'comment-question-outline'
        text: 'Ask a question'
        font_name:"DMSans"
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: root.manager.current = 'questionlist'
        Image:
            id: img
            source: 'img/Dinosavvy.png'
            pos_hint: {'center_x': 0.5,'center_y': 0.2}
            size_hint: (0.2,0.2)
            
 
   
<Personalize>:
    name: 'personalize'
    
    MDIconButton:
        icon: "account"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.96}
        size_hint: (0.01, 0.01)
    
    MDLabel:
        text: 'Personalize!'
        halign: 'center' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_style: "H5"
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}
        
    MDLabel:
        text: 'Just one more step so we can save your preferences'
        font_name:"DMSans"
        font_size:15
        halign: "center"
        theme_text_color: "Primary"
        pos_hint:{'center_x': 0.5, 'center_y': 0.84}
        halign: 'center'
        size_hint: (0.8, 0.5)
      
    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.1, 'center_y': 0.95}
        on_press: root.manager.current = 'home'

    MDRoundFlatButton:
        text: 'New User'
        font_name:"DMSans"
        pos_hint: {'center_x':0.5,'center_y':0.55}
        on_press: root.manager.current = 'signup'
    
    MDFillRoundFlatButton:
        text: 'Already have an account? Log in'
        font_name:"DMSans"
        pos_hint: {'center_x':0.5,'center_y':0.45}
        on_press: root.manager.current = 'login'
    
    MDTextButton:
        text: "Skip"
        font_name:"DMSans"
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
        text: 'Create account to save dilemma'
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_style: "H4"
        pos_hint: {'center_x': 0.57, 'center_y': 0.92}
        
    MDLabel:
        text: 'Just one more step so we can save your preferences'
        font_name:"DMSans"
        font_style: "H6"
        pos_hint:{'center_x': 0.47, 'center_y': 0.84}
        halign: 'left'
        size_hint: (0.8, 0.5)
    
    MDTextField:
        hint_text: "Enter username"
        helper_text: "Usernames can't contain spaces"
        helper_text_mode: "on_focus"
        font_name:"DMSans"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.7}
        size_hint_x:None
        width:330
    
    MDTextField:
        hint_text: "Enter email"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        font_name:"DMSans"
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
        font_name:"DMSans"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.25, 'center_y': 0.1}
        on_press: root.manager.current = 'personalize'

    MDTextButton:
        text: "Create account"
        theme_text_color: "Custom"
        font_name:"DMSans"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.78, 'center_y': 0.35}
        on_press: root.manager.current = 'habits'
  
    MDTextButton:
        text: "Skip"
        theme_text_color: "Custom"
        font_name:"DMSans"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.85, 'center_y': 0.1}
        on_press: root.manager.current = 'habits'
        
<Signup>:
    name: 'signup'
    
    MDIconButton:
        icon: "emoticon-excited-outline"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.96}
        size_hint: (0.01, 0.01)
        
    MDLabel:
        text: 'Great Job!'
        halign: 'center' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_style: "H5"
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}
        
    MDLabel:
        text: 'Just one more step so we can save your preferences'
        font_name:"DMSans"
        font_size:15
        halign: "center"
        theme_text_color: "Primary"
        pos_hint:{'center_x': 0.5, 'center_y': 0.84}
        halign: 'center'
        size_hint: (0.8, 0.5)
               
    MDTextField:
        hint_text: "Email"
        font_name:"DMSans"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        size_hint_x:None
        width:330
    
    MDTextField:
        hint_text: "Choose a password"
        font_name:"DMSans"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:330
    
    MDTextField:
        hint_text: "Confirm password"
        font_name:"DMSans"
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
        font_name:"DMSans"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.25, 'center_y': 0.1}
        on_press: root.manager.current = 'personalize'

    MDFillRoundFlatButton:
        text: "Create account"
        font_name:"DMSans"
        theme_text_color: "Custom"
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        size_hint: (0.9, 0.08)
        on_press: root.manager.current = 'habits'
  
    MDTextButton:
        text: "Skip"
        font_name:"DMSans"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.75, 'center_y': 0.1}
        on_press: root.manager.current = 'habits'
        
<Habits>:
    name: 'habits'
    
    MDLabel:
        text: 'Habits'
        font_name:"DMSans"
        halign: "center"
        theme_text_color: "Primary"
        font_style: "H5"
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}
    
    MDLabel:
        text: 'Select what applies to you'
        font_name:"DMSans"
        font_size:15
        halign: "center"
        theme_text_color: "Primary"
        pos_hint:{'center_x': 0.5, 'center_y': 0.84}
        size_hint: (0.8, 0.5)
        
    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.1, 'center_y': 0.95}
        on_press: root.manager.current = 'personalize'
             
    MDIconButton:
        icon: "repeat"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.96}
        size_hint: (0.01, 0.01)
        
    MDFillRoundFlatButton:
        text: "Next"
        font_name:"DMSans"
        theme_text_color: "Custom"
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        size_hint: (0.9, 0.08)
        on_press: root.manager.current = 'location'
    
    MDTextButton:
        text: "Skip"
        font_name:"DMSans"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: root.manager.current = 'questionlist'
    
  

<Location>:
    name: 'location'
    
    MDLabel:
        text: 'Where are you?'
        font_name:"DMSans"
        halign: "center"
        theme_text_color: "Primary"
        font_style: "H5"
        pos_hint: {'center_x': 0.5, 'center_y': 0.92}
        size_hint: (0.8, 0.5)

    MDLabel:
        text: 'This helps optimize your preferences'
        font_name:"DMSans"
        halign: "center"
        font_size:15
        theme_text_color: "Primary"
        pos_hint: {'center_x': 0.5, 'center_y': 0.84}
        size_hint: (0.8, 0.5)

    MDIconButton:
        icon: "map-marker"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.25  , 'center_y': 0.925}
        size_hint: (0.1, 0.1)
        user_font_size: "35sp"

    MDIconButton:
        icon: "home"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: root.manager.current = 'home'
    
    MDTextButton:
        text: "Back"
        font_name:"DMSans"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.25, 'center_y': 0.5}
        on_press: root.manager.current = 'habits'

      
    MDTextButton:
        text: "Skip"
        font_name:"DMSans"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.89, 'center_y': 0.43}
        on_press: root.manager.current = 'questionlist'

        
    MDFillRoundFlatButton:
        text: "Next"
        font_name:"DMSans"
        theme_text_color: "Custom"
        pos_hint: {'center_x': 0.75, 'center_y': 0.5}
        size_hint: (0.4, 0.08)
        on_press: root.manager.current = 'questionlist'
          
<LogIn>:
    name: 'login'
    
    MDTextField:
        hint_text: "Enter email"
        font_name:"DMSans"
        helper_text: "forgot username? use your email"
        helper_text_mode: "on_focus"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        size_hint_x:None
        width:300
    
    MDTextField:
        hint_text: "Enter password"
        font_name:"DMSans"
        helper_text: "or click on forgot password"
        helper_text_mode: "on_focus"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:300
    
    MDRoundFlatButton:
        text: 'Log in'
        font_name:"DMSans"
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'questionlist'
    
    MDTextButton:
        text: "Forgot password"
        font_name:"DMSans"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.73, 'center_y': 0.45}
        on_press: root.manager.current = 'resetpassword'
    
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
        font_name:"DMSans"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.25, 'center_y': 0.1}
        on_press: root.manager.current = 'personalize'

<ResetPassword>:
    name: 'resetpassword'
    
    MDLabel:
        text: 'Reset password'
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_style: "H5"
        pos_hint: {'center_x': 0.57, 'center_y': 0.92}
    
    MDTextField:
        hint_text: "Enter email"
        font_name:"DMSans"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        size_hint_x:None
        width:300
          
    MDTextButton:
        text: "Reset password"
        font_name:"DMSans"
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
        font_name:"DMSans"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.25, 'center_y': 0.1}
        on_press: root.manager.current = 'personalize'

<NewPassword>:
    name: 'newpassword'
    
    MDLabel:
        text: 'Set your new password'
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_style: "H5"
        pos_hint: {'center_x': 0.57, 'center_y': 0.92}
            
    
    MDTextField:
        hint_text: "Enter username"
        font_name:"DMSans"
        helper_text: "Usernames can't contain spaces"
        helper_text_mode: "on_focus"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.7}
        size_hint_x:None
        width:330
    
    MDTextField:
        hint_text: "Enter email"
        font_name:"DMSans"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        size_hint_x:None
        width:330
    
    MDTextField:
        hint_text: "Enter password"
        font_name:"DMSans"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:330
    
    MDTextField:
        hint_text: "Repeat password"
        font_name:"DMSans"
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
        font_name:"DMSans"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.25, 'center_y': 0.1}
        on_press: root.manager.current = 'resetpassword'

    MDTextButton:
        text: "Save new password"
        font_name:"DMSans"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.73, 'center_y': 0.35}
        on_press: root.manager.current = 'questionlist'
  
    MDTextButton:
        text: "Skip"
        font_name:"DMSans"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.75, 'center_y': 0.1}
        on_press: root.manager.current = 'question'

<QuestionScreen3>:
    name: 'questionscreen3'
    
    MDLabel:
        text: 'Is it better to buy fresh or frozen vegetables?'
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:20
        pos_hint: {'center_x': 0.58, 'center_y': 0.9}
        
    FloatLayout:
        Image:
            id: img
            halign: 'left' 
            source: 'img/Group 94.png'
            pos_hint: {'center_x': 0.5,'center_y': 0.6}
            size_hint: (1,0.7)
            
<QuestionList>:
    name: 'questionlist'
    MDLabel:
        text: 'Dilemmas'
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_style: "H5"
        pos_hint: {'center_x': 0.63, 'center_y': 0.95}
    
    MDIconButton:
        icon: 'comment-question-outline'    
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.1, 'center_y': 0.95}
        size_hint: (0.01, 0.01)
        
    MDLabel:
        text: 'Food'
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:20
        pos_hint: {'center_x': 0.58, 'center_y': 0.9}

    Image:
        id: img
        halign: 'left' 
        source: 'img/frozenQ.png'
        pos_hint: {'center_x': 0.28,'center_y': 0.79}
        size_hint: (0.6,0.6)
    
    MDTextButton:
        text: 'Fresh or frozen fruits and vegetables?'
        halign: 'left' 
        font_name:"DMSans"
        font_size:13
        pos_hint: {'center_x': 0.28, 'center_y': 0.68}
        size_hint: (0.42,0.42)
        on_press: root.manager.current = 'question'

    Image:
        id: img
        halign: 'left' 
        source: 'img/meat.png'
        pos_hint: {'center_x': 0.28,'center_y': 0.31}
        size_hint: (0.6,0.6)
            
    MDTextButton:
        text: 'Local meat or vegan alternative?'
        halign: 'left' 
        font_name:"DMSans"
        font_size:13
        pos_hint: {'center_x': 0.28, 'center_y': 0.20}
        size_hint: (0.42,0.42)
    
    Image:
        id: img
        halign: 'left' 
        source: 'img/bags.png'
        pos_hint: {'center_x': 0.28,'center_y': 0.55}
        size_hint: (0.6,0.6)
            
    MDTextButton:
        text: 'Paper or fabric bags'
        halign: 'left' 
        font_name:"DMSans"
        font_size:13
        pos_hint: {'center_x': 0.28, 'center_y': 0.44}
        size_hint: (0.42,0.42)
        
    Image:
        id: img
        halign: 'left' 
        source: 'img/3.png'
        pos_hint: {'center_x': 0.75,'center_y': 0.79}
        size_hint: (0.6,0.6)
    
    MDTextButton:
        text: 'Glass container or plastic containers?'
        halign: 'left' 
        font_name:"DMSans"
        font_size:13
        pos_hint: {'center_x': 0.75, 'center_y': 0.68}
        size_hint: (0.42,0.42)
    
    Image:
        id: img
        halign: 'left' 
        source: 'img/mealkits.png'
        pos_hint: {'center_x': 0.75,'center_y': 0.55}
        size_hint: (0.6,0.6)
    
    MDTextButton:
        text: 'Meal kits or Supermarket shopping?'
        halign: 'left' 
        font_name:"DMSans"
        font_size:13
        pos_hint: {'center_x': 0.75, 'center_y': 0.44}
        size_hint: (0.42,0.42)
        
    Image:
        id: img
        halign: 'left' 
        source: 'img/milk.png'
        pos_hint: {'center_x': 0.75,'center_y': 0.31}
        size_hint: (0.6,0.6)
    
    MDTextButton:
        text: 'What type of milk is better?'
        halign: 'left' 
        font_name:"DMSans"
        font_size:13
        pos_hint: {'center_x': 0.75, 'center_y': 0.20}
        size_hint: (0.42,0.42)

    
    
    MDIconButton:
        icon: "home"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: root.manager.current = 'home'            
    
    MDIconButton:
        icon: "chevron-down"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.15}
        on_press: 
            root.manager.transition.direction = 'up'
            root.manager.current = 'questionlist2' 

<QuestionList2>:
    name: 'questionlist2'
    MDLabel:
        text: 'Food'
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:20
        pos_hint: {'center_x': 0.58, 'center_y': 0.9}

    Image:
        id: img
        halign: 'left' 
        source: 'img/frozenQ.png'
        pos_hint: {'center_x': 0.28,'center_y': 0.79}
        size_hint: (0.6,0.6)
    
    MDTextButton:
        text: 'fresh or frozen fruits and vegetables?'
        halign: 'left' 
        font_name:"DMSans"
        font_size:13
        pos_hint: {'center_x': 0.28, 'center_y': 0.68}
        size_hint: (0.42,0.42)
        on_press: root.manager.current = 'question'

    Image:
        id: img
        halign: 'left' 
        source: 'img/meat.png'
        pos_hint: {'center_x': 0.28,'center_y': 0.31}
        size_hint: (0.6,0.6)
            
    MDTextButton:
        text: 'Local meat or vegan alternative?'
        halign: 'left' 
        font_name:"DMSans"
        font_size:13
        pos_hint: {'center_x': 0.28, 'center_y': 0.20}
        size_hint: (0.42,0.42)
    
    Image:
        id: img
        halign: 'left' 
        source: 'img/bags.png'
        pos_hint: {'center_x': 0.28,'center_y': 0.55}
        size_hint: (0.6,0.6)
            
    MDTextButton:
        text: 'Paper or fabric bags'
        halign: 'left' 
        font_name:"DMSans"
        font_size:13
        pos_hint: {'center_x': 0.28, 'center_y': 0.44}
        size_hint: (0.42,0.42)
        
    Image:
        id: img
        halign: 'left' 
        source: 'img/3.png'
        pos_hint: {'center_x': 0.75,'center_y': 0.79}
        size_hint: (0.6,0.6)
    
    MDTextButton:
        text: 'Glass container or plastic containers?'
        halign: 'left' 
        font_name:"DMSans"
        font_size:13
        pos_hint: {'center_x': 0.75, 'center_y': 0.68}
        size_hint: (0.42,0.42)
    
    Image:
        id: img
        halign: 'left' 
        source: 'img/mealkits.png'
        pos_hint: {'center_x': 0.75,'center_y': 0.55}
        size_hint: (0.6,0.6)
    
    MDTextButton:
        text: 'Meal kits or Supermarket shopping?'
        halign: 'left' 
        font_name:"DMSans"
        font_size:13
        pos_hint: {'center_x': 0.75, 'center_y': 0.44}
        size_hint: (0.42,0.42)
        
    Image:
        id: img
        halign: 'left' 
        source: 'img/milk.png'
        pos_hint: {'center_x': 0.75,'center_y': 0.31}
        size_hint: (0.6,0.6)
    
    MDTextButton:
        text: 'What type of milk is better?'
        halign: 'left' 
        font_name:"DMSans"
        font_size:13
        pos_hint: {'center_x': 0.75, 'center_y': 0.20}
        size_hint: (0.42,0.42)
    
    MDIconButton:
        icon: "home"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: root.manager.current = 'home'            
    
    MDIconButton:
        icon: "chevron-up"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.96}
        on_press: 
            root.manager.transition.direction = 'down'
            root.manager.current = 'questionlist'        

<QuestionScreen>:
    name: 'question'
    
    MDLabel:
        text: 'Is it better to buy fresh or frozen vegetables?'
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:20
        pos_hint: {'center_x': 0.58, 'center_y': 0.9}
    
    FloatLayout:
        Image:
            id: img
            halign: 'left' 
            source: 'img/frozen.png'
            pos_hint: {'center_x': 0.5,'center_y': 0.69}
            size_hint: (1,0.7)
            
    MDFillRoundFlatButton:
        text: "Vegetables"
        font_name:"DMSans"
        theme_text_color: "Custom"
        pos_hint: {'center_x': 0.18, 'center_y': 0.49}
        size_hint: (0.15, 0.05)
        on_press: root.manager.current = 'question'
   
    MDFillRoundFlatButton:
        text: "Fruits"
        font_name:"DMSans"
        theme_text_color: "Custom"
        pos_hint: {'center_x': 0.41, 'center_y': 0.49}
        size_hint: (0.15, 0.05)
        on_press: root.manager.current = 'question'     
    
    MDLabel:
        text: 'Fresh.\\n' +\
            '\\n' +\
            'There is no solid evidence that buying frozen vegetables benefits the environment but it is' +\
            'a proven fact that fresh vegetables are better for health.' 
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:15
        pos_hint: {'center_x': 0.5, 'center_y': 0.27}
        size_hint: (0.85, 0.4)
    
    MDFillRoundFlatIconButton:
        text: "Save"
        font_name:"DMSans"
        icon: "star-outline"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.73, 'center_y': 0.42}
        size_hint: (0.41, 0.06)
        on_press: root.manager.current = 'question'
    
    MDRoundFlatIconButton:
        text: "Share"
        font_name:"DMSans"
        icon: "share-variant"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.28, 'center_y': 0.42}
        size_hint: (0.41, 0.06)
        on_press: root.manager.current = 'question'
    
    MDIconButton:
        icon: "chevron-down"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.15}
        on_press: 
            root.manager.transition.direction = 'up'
            root.manager.current = 'questionscreen2'        
    
     
    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.1, 'center_y': 0.96}
        on_press: root.manager.current = 'questionlist'
  
    MDIconButton:
        icon: "home"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.05}
        on_press: root.manager.current = 'home'
    
    MDIconButton:
        icon: "account"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.25, 'center_y': 0.05}
        on_press: root.manager.current = 'profile'
    
    MDIconButton:
        icon: "star-outline"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.75, 'center_y': 0.05}
        on_press: root.manager.current = 'savedquestions'
            

          
        
<QuestionScreen2>:
    name: 'questionscreen2'
    
    MDLabel:
        text: 'Is it better to buy fresh or frozen vegetables?'
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:20
        pos_hint: {'center_x': 0.58, 'center_y': 0.9}
    
      
    
    MDLabel:
        text: 'Consider meal planning, so that the veggies you bought do not get spoiled. If you already' +\
            'have something in your home that you are not sure you will eat in time (bought fresh), ' +\
            'consider freezing it while it is still edible or giving it away.' +\
            ' \\n' +\
            ' \\n' +\
            'Fresh fruit and vegetables contribute to almost 50% of the food waste generated by households.' +\
            'We need to think not only of the food itself, but of the resources spent on growing it and CO2' +\
            'emissions resulting from transporting it.\\n' +\
            ' \\n' +\
            'In 2016, the project FUSIONS estimated that 173 kg of fruits and vegetables are thrown away per' +\
            'person per year in Europe. Most of this comes from households (therefore, what you personally ' +\
            'do really counts!)' 
            
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:15
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint: (0.85, 0.5)
    
    MDIconButton:
        icon: "chevron-down"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.05}
        on_press: 
            root.manager.transition.direction = 'up'
            root.manager.current = 'questionscreen3'        
    
    MDIconButton:
        icon: "chevron-up"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.96}
        on_press: 
            root.manager.transition.direction = 'down'
            root.manager.current = 'question'  
            
    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.1, 'center_y': 0.96}
        on_press: root.manager.current = 'questionlist'
        
    MDIconButton:
        icon: "home"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.05}
        on_press: root.manager.current = 'home'
    
    MDIconButton:
        icon: "account"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.25, 'center_y': 0.05}
        on_press: root.manager.current = 'profile'
    
    MDIconButton:
        icon: "star-outline"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.75, 'center_y': 0.05}
        on_press: root.manager.current = 'savedquestions' 
        
    MDFillRoundFlatIconButton:
        text: "Save"
        font_name:"DMSans"
        icon: "star-outline"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.73, 'center_y': 0.17}
        size_hint: (0.41, 0.06)
        on_press: root.manager.current = 'question'
  
    MDRoundFlatIconButton:
        text: "Share"
        font_name:"DMSans"
        icon: "share-variant"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.28, 'center_y': 0.17}
        size_hint: (0.41, 0.06)
        on_press: root.manager.current = 'question'
        
<QuestionScreeno>:
    name: 'questionscreeno'
    
    MDLabel:
        text: 'Is it better to buy fresh or frozen vegetables?'
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:20
        pos_hint: {'center_x': 0.58, 'center_y': 0.9}
    
    FloatLayout:
        Image:
            id: img
            halign: 'left' 
            source: 'img/frozen.png'
            pos_hint: {'center_x': 0.5,'center_y': 0.69}
            size_hint: (1,0.7)
            
    MDFillRoundFlatButton:
        text: "Vegetables"
        font_name:"DMSans"
        theme_text_color: "Custom"
        pos_hint: {'center_x': 0.18, 'center_y': 0.49}
        size_hint: (0.15, 0.05)
        on_press: root.manager.current = 'question'
   
    MDFillRoundFlatButton:
        text: "Fruits"
        font_name:"DMSans"
        theme_text_color: "Custom"
        pos_hint: {'center_x': 0.41, 'center_y': 0.49}
        size_hint: (0.15, 0.05)
        on_press: root.manager.current = 'question'     
    
    MDLabel:
        text: 'Fresh.\\n' +\
            '\\n' +\
            'There is no solid evidence that buying frozen vegetables benefits the environment but it is\\n' +\
            'a proven fact that fresh vegetables are better for health.\\n' +\
            'Consider meal planning, so that the veggies you bought do not get spoiled. If you already \\n' +\
            'have something in your home that you are not sure you will eat in time (bought fresh), \\n' +\
            'consider freezing it while it is still edible or giving it away.'
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:15
        pos_hint: {'center_x': 0.5, 'center_y': 0.26}
        size_hint: (0.85, 0.5)
    
    MDIconButton:
        icon: "chevron-down"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.05}
        on_press: 
            root.manager.transition.direction = 'down'
            root.manager.current = 'question'        
    
    MDIconButton:
        icon: "chevron-up"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.95}
        on_press: 
            root.manager.transition.direction = 'down'
            root.manager.current = 'question'  
            
    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.1, 'center_y': 0.96}
        on_press: root.manager.current = 'home'
        
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
    
<SavedQuestions>:
    name: 'savedquestions'
    
    MDLabel:
        text: 'Is it better to buy fresh or frozen vegetables?'

    


        
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
            font_name:"DMSans"


      
<Profile>:
    name: 'profile'
    
    MDLabel:
        text: 'Profile'
        font_name:"DMSans"
        halign: "left"
        theme_text_color: "Primary"
        font_style: "H5"
        pos_hint: {'center_x': 0.6, 'center_y': 0.9}
    
    MDLabel:
        text: 'Habits'
        font_name:"DMSans"
        font_size:19
        halign: "left"
        theme_text_color: "Primary"
        pos_hint:{'center_x': 0.55, 'center_y': 0.84}
        size_hint: (0.8, 0.5)
        
    MDIconButton:
        icon: "repeat"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.12, 'center_y': 0.84}
        size_hint: (0.007, 0.007)

    MDIconButton:
        icon: "pencil"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.9, 'center_y': 0.84}
        size_hint: (0.007, 0.007)
        on_press: root.manager.current = 'habits'   
    
    MDLabel:
        text: 'Eat Meat alternatives\\n' +\
            'Vegeterian\\n' +\
            'Use cars minimally\\n' +\
            'Fly less\\n' +\
            'Sort out garbage\\n' +\
            'Carpool'    
        font_name:"DMSans"
        font_size:12
        halign: "left"
        theme_text_color: "Primary"
        pos_hint:{'center_x': 0.55, 'center_y': 0.74}
        size_hint: (0.8, 0.4)
        
    MDLabel:
        text: 'Location'
        font_name:"DMSans"
        font_size:19
        halign: "left"
        theme_text_color: "Primary"
        pos_hint:{'center_x': 0.55, 'center_y': 0.54}
        size_hint: (0.8, 0.5)
    
    MDLabel:
        text: 'Netherlands'
        font_name:"DMSans"
        font_size:15
        halign: "left"
        theme_text_color: "Primary"
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint: (0.8, 0.5)
        
    MDIconButton:
        icon: "map-marker"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.12, 'center_y': 0.54}
        size_hint: (0.007, 0.007)
    
    MDIconButton:
        icon: "pencil"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.9, 'center_y': 0.54}
        size_hint: (0.007, 0.007)
        on_press: root.manager.current = 'location'   

 
    MDLabel:
        text: 'Profile'
        font_name:"DMSans"
        font_size:19
        halign: "left"
        theme_text_color: "Primary"
        pos_hint:{'center_x': 0.55, 'center_y': 0.34}
        size_hint: (0.8, 0.5)
    
    MDIconButton:
        icon: "account"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.12, 'center_y': 0.34}
        size_hint: (0.007, 0.007)
    
    MDLabel:
        text: 'Email:                   email@email.com'
        font_name:"DMSans"
        font_size:15
        halign: "left"
        theme_text_color: "Primary"
        pos_hint:{'center_x': 0.5, 'center_y': 0.30}
        size_hint: (0.8, 0.5)
            
    MDIconButton:
        icon: "pencil"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.9, 'center_y': 0.30}
        size_hint: (0.007, 0.007)
        on_press: root.manager.current = 'newemail'

    MDLabel:
        text: 'Password:           ***********'
        font_name:"DMSans"
        font_size:15
        halign: "left"
        theme_text_color: "Primary"
        pos_hint:{'center_x': 0.5, 'center_y': 0.25}
        size_hint: (0.8, 0.5)
    
    MDIconButton:
        icon: "pencil"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.9, 'center_y': 0.25}
        size_hint: (0.007, 0.007)
        on_press: root.manager.current = 'resetpassword'

    MDIconButton:
        icon: "home"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.05}
        on_press: root.manager.current = 'home'
    
    MDIconButton:
        icon: "star-outline"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.75, 'center_y': 0.05}
        on_press: root.manager.current = 'savedquestions'   


<NewEmail>:
    name: 'newemail'
    
    MDLabel:
        text: 'Choose a new email'
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_style: "H5"
        pos_hint: {'center_x': 0.57, 'center_y': 0.92}
    
    MDTextField:
        hint_text: "Enter email"
        font_name:"DMSans"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        size_hint_x:None
        width:300
    
    MDTextField:
        hint_text: "Confirm email"
        font_name:"DMSans"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:300
              
    MDTextButton:
        text: "Submit"
        font_name:"DMSans"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.73, 'center_y': 0.55}
        on_press: root.manager.current = 'profile'
    
    MDIconButton:
        icon: "home"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: root.manager.current = 'home'
    
    MDTextButton:
        text: "Back"
        font_name:"DMSans"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.25, 'center_y': 0.1}
        on_press: root.manager.current = 'profile'
"""

##Define screen classes
class NewEmail(Screen):
    pass
class Profile(Screen):
    pass
class QuestionList2(Screen):
    pass
class QuestionList(Screen):
    pass
class QuestionScreen3(Screen):
    pass
class SavedQuestions(Screen):
    pass
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
class Personalize(Screen):
    pass
class QuestionScreen(Screen):
    pass
class QuestionScreen2(Screen):
    pass
class LogIn(Screen):
    pass
class First(Screen):
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

class Signup(Screen):
    pass
class Habits(Screen):
    def load_table(self):
        layout = AnchorLayout()
        self.data_tables = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.545},
            size_hint=(0.8, 0.5),
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
class Dilemmas(Screen):
    pass
class Settings(Screen):
    pass
class Navbar(Screen):
    pass



# Create the screen manager
sm = ScreenManager()
sm.add_widget(Home(name='home'))
sm.add_widget(Personalize(name='personalize'))
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
sm.add_widget(SignupLater(name='signuplater'))
sm.add_widget(Navbar(name='navbar'))
sm.add_widget(ToolBar(name='toolbar'))
sm.add_widget(QuestionScreen2(name='questionscreen2'))
sm.add_widget(NewPassword(name='newpassword'))
sm.add_widget(ResetPassword(name='resetpassword'))
sm.add_widget(QuestionScreen3(name='questionscreen3'))
sm.add_widget(QuestionList(name='questionlist'))
sm.add_widget(QuestionList2(name='questionlist2'))
sm.add_widget(Profile(name='profile'))
sm.add_widget(NewEmail(name='newemail'))



class DinosavvyApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "900"
        self.theme_cls.theme_style = "Light"
        return screen

    def call(self, button):
        print('called from', button)

    class ContentNavigationDrawer(BoxLayout):
        pass

    class DrawerList(ThemableBehavior, MDList):
        pass

LabelBase.register(name='DMSans',
                   fn_regular='DMSans-Regular.ttf')


DinosavvyApp().run()


