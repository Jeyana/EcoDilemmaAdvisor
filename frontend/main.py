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
from kivy.properties import ObjectProperty
from kivymd.uix.menu import MDDropdownMenu

Window.size = (400, 630)

# add screens to screen manager
screen_helper = """
ScreenManager:
    Home:
    Personalize:
    FreshQuestion:
    FreshQuestion2:
    MeatQuestion:
    MeatQuestion2:
    MeatQuestion3:
    MilkQuestion:
    MilkQuestion2:
    MilkQuestion3:
    QuestionScreen3:
    LogIn:
    First:
    Error:
    Home:
    Habits:
    HabitsEdit:
    Location:
    LocationEdit:
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
    FoodQuestionList:
    FoodQuestionList2:
    FashionQuestionList:
    TransportQuestionList:
    Profile:
    ResetEmail:

#screens                             
<Home>:
    name: 'home'

    FloatLayout:
        Image:
            id: img
            source: 'img/Logo Stacked.png'
            pos_hint: {'center_x': 0.5,'center_y': 0.8}
            size_hint: (0.5,0.5)

    FloatLayout:
        Image:
            id: img
            source: 'img/By logo.png'
            pos_hint: {'center_x': 0.5,'center_y': 0.1}
            size_hint: (0.5,0.5)

    FloatLayout:
        Image:
            id: img
            source: 'img/Rectangle 28.png'
            size_hint: (0.9,0.25)
            pos_hint: {'center_x': 0.5, 'center_y': 0.48}

    FloatLayout:
        Image:
            id: img
            source: 'img/pink question mark.png'
            size_hint: (0.1,0.1)
            pos_hint: {'center_x': 0.22, 'center_y': 0.47}

    MDTextButton:
        text: "Personalize"
        font_name:"DMSans"
        font_size:15
        halign:"center"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.4, 'center_y': 0.5}
        on_press: root.manager.current = 'personalize'
        size_hint: (0.9,0.25)

    MDLabel:
        text: 'See dilemmas based on your habits  \\n' +\
            'and save your preferences'
        font_name:"DMSans"
        font_size:12
        halign:"left"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.8, 'center_y': 0.45}

    FloatLayout:
        Image:
            id: img
            source: 'img/Rectangle 28.png'
            size_hint: (0.9,0.4)
            pos_hint: {'center_x': 0.5, 'center_y': 0.28}

    MDTextButton:
        text: "Ask a question"
        font_name:"DMSans"
        font_size:15
        halign:"center"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.43, 'center_y': 0.31}
        size_hint: (0.9,0.25)
        md_bg_color: app.theme_cls.primary_dark
        on_press: root.manager.current = 'questionlist'

    MDLabel:
        text: 'Take me directly to the questions' 
        font_name:"DMSans"
        font_size:12
        halign:"left"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.8, 'center_y': 0.275}

    FloatLayout:
        Image:
            id: img
            source: 'img/pencil.png'
            size_hint: (0.1,0.1)
            pos_hint: {'center_x': 0.22, 'center_y': 0.29}

    FloatLayout:
        Image:
            id: img
            source: 'img/By logo.png'
            pos_hint: {'center_x': 0.5,'center_y': 0.1}
            size_hint: (0.5,0.5)

    FloatLayout:
        Image:
            id: img
            source: 'img/plants.png'
            pos_hint: {'center_x': 0.9,'center_y': 0.06}
            size_hint: (0.5,0.5)        

    FloatLayout:
        Image:
            id: img
            source: 'img/bushes.png'
            pos_hint: {'center_x': 0.1,'center_y': 0.055}
            size_hint: (0.5,0.5)  

<Personalize>:
    name: 'personalize'

    MDLabel:
        text: 'Personalize!'
        halign: "center"
        theme_text_color: "Primary"
        font_style: "H6"
        font_name:"DMSans"
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}

    MDLabel:
        text: 'Just one more step so we can save your preferences'
        font_style: "Subtitle2"
        font_name:"DMSans"
        halign: "center"
        theme_text_color: "Primary"
        pos_hint:{'center_x': 0.5, 'center_y': 0.75}
        size_hint: (0.8, 0.5)

    FloatLayout:
        Image:
            id: img
            source: 'img/signup.png'
            size_hint: (0.4,0.4)
            pos_hint: {'center_x': 0.5, 'center_y': 0.9}

    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.1, 'center_y': 0.95}
        on_press: root.manager.current = 'home'

    MDRoundFlatButton:
        text: "New User"
        font_name:"DMSans"
        theme_text_color: "Custom"
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        size_hint: (0.9, 0.08)
        on_press: root.manager.current = 'signup'

    MDFillRoundFlatButton:
        text: "Already have an account? Log in"
        font_name:"DMSans"
        theme_text_color: "Custom"
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        size_hint: (0.9, 0.08)
        on_press: root.manager.current = 'login'


    MDTextButton:
        text: "Skip"
        font_name:"DMSans"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: root.manager.current = 'location'    

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

    MDLabel:
        text: 'Great Job!'
        halign: "center"
        theme_text_color: "Primary"
        font_style: "H6"
        font_name:"DMSans"
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}

    MDLabel:
        text: 'Just one more step so we can save your preferences'
        font_style: "Subtitle2"
        font_name:"DMSans"
        halign: "center"
        theme_text_color: "Primary"
        pos_hint:{'center_x': 0.5, 'center_y': 0.75}
        size_hint: (0.8, 0.5)

    FloatLayout:
        Image:
            id: img
            source: 'img/signup.png'
            size_hint: (0.4,0.4)
            pos_hint: {'center_x': 0.5, 'center_y': 0.9}

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
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.1, 'center_y': 0.96}
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
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: root.manager.current = 'habits'

<Habits>:
    name: 'habits'

    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.1, 'center_y': 0.96}
        on_press: root.manager.current = 'signup'

    MDLabel:
        text: 'Tell us your habits'
        halign: "center"
        theme_text_color: "Primary"
        font_style: "H6"
        font_name:"DMSans"
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}

    MDLabel:
        text: 'We use this information to suggest more relevant dilemmas to you'
        font_style: "Subtitle2"
        font_name:"DMSans"
        halign: "center"
        theme_text_color: "Primary"
        pos_hint:{'center_x': 0.5, 'center_y': 0.75}
        size_hint: (0.8, 0.5)

    FloatLayout:
        Image:
            id: img
            source: 'img/Healthy life.png'
            size_hint: (0.4,0.4)
            pos_hint: {'center_x': 0.5, 'center_y': 0.9}

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
        on_press: root.manager.current = 'location'



<Location>:
    name: 'location'

    FloatLayout:
        Image:
            id: img
            source: 'img/location.png'
            size_hint: (0.4,0.4)
            pos_hint: {'center_x': 0.5, 'center_y': 0.9}

    MDLabel:
        text: 'Where are you?'
        halign: "center"
        theme_text_color: "Primary"
        font_style: "H6"
        font_name:"DMSans"
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}

    MDLabel:
        text: 'We will find more accurate information according to your location'
        font_style: "Subtitle2"
        font_name:"DMSans"
        halign: "center"
        theme_text_color: "Primary"
        pos_hint:{'center_x': 0.5, 'center_y': 0.75}
        size_hint: (0.8, 0.5)

    MDTextField:
        hint_text: "Enter Location"
        font_name:"DMSans"
        icon_right: "map-marker"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        size_hint_x:None
        width:330

    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.1, 'center_y': 0.96}
        on_press: root.manager.current = 'habits'


    MDFillRoundFlatButton:
        text: "Next"
        font_name:"DMSans"
        theme_text_color: "Custom"
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        size_hint: (0.9, 0.08)
        on_press: root.manager.current = 'questionlist'

    MDTextButton:
        text: "Skip"
        font_name:"DMSans"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: root.manager.current = 'questionlist'

<LogIn>:
    name: 'login'

    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.1, 'center_y': 0.96}
        on_press: root.manager.current = 'personalize'

    MDLabel:
        text: 'Welcome back!'
        halign: "center"
        theme_text_color: "Primary"
        font_style: "H6"
        font_name:"DMSans"
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}

    MDLabel:
        text: 'Log in so we can save your preferences'
        font_style: "Subtitle2"
        font_name:"DMSans"
        halign: "center"
        theme_text_color: "Primary"
        pos_hint:{'center_x': 0.5, 'center_y': 0.75}
        size_hint: (0.8, 0.5)

    FloatLayout:
        Image:
            id: img
            source: 'img/signup.png'
            size_hint: (0.4,0.4)
            pos_hint: {'center_x': 0.5, 'center_y': 0.9}

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

    MDTextButton:
        text: "Forgot password"
        font_name:"DMSans"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.73, 'center_y': 0.45}
        on_press: root.manager.current = 'resetpassword'

    MDFillRoundFlatButton:
        text: "Log in"
        font_name:"DMSans"
        theme_text_color: "Custom"
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        size_hint: (0.9, 0.08)
        on_press: root.manager.current = 'profile'


    MDTextButton:
        text: "Skip"
        font_name:"DMSans"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: root.manager.current = 'questionlist'

<ResetPassword>:
    name: 'resetpassword'

    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.1, 'center_y': 0.96}
        on_press: root.manager.current = 'profile'

    MDLabel:
        text: 'Reset password'
        halign: "center"
        theme_text_color: "Primary"
        font_style: "H6"
        font_name:"DMSans"
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}

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
        on_press: root.manager.current = 'freshquestion'

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
        on_press: root.manager.current = 'QuestionList'

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
        on_press: root.manager.current = 'freshquestion'

<QuestionList>:
    name: 'questionlist'
    MDLabel:
        text: 'Browse Dilemmas'
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:22
        pos_hint: {'center_x': 0.575, 'center_y': 0.95}

    MDTextButton:
        text: 'Food'
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:15
        pos_hint: {'center_x': 0.12, 'center_y': 0.9}
        on_press: root.manager.current = 'foodquestionlist'

    MDTextButton:
        text: 'Transport'
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:15
        pos_hint: {'center_x': 0.145, 'center_y': 0.6}
        on_press: root.manager.current = 'transportquestionlist'

    MDTextButton:
        text: 'Fashion'
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:15
        pos_hint: {'center_x': 0.135, 'center_y': 0.33}
        on_press: root.manager.current = 'fashionquestionlist'

    MDTextButton:
        text: 'See More'
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:14
        pos_hint: {'center_x': 0.87, 'center_y': 0.9}
        on_press: root.manager.current = 'foodquestionlist'


    MDTextButton:
        text: 'See More'
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:14
        pos_hint: {'center_x': 0.87, 'center_y': 0.6}
        on_press: root.manager.current = 'transportquestionlist'

    MDTextButton:
        text: 'See More'
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:14
        pos_hint: {'center_x': 0.87, 'center_y': 0.33}
        on_press: root.manager.current = 'fashionquestionlist'

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
        font_size:12
        pos_hint: {'center_x': 0.28, 'center_y': 0.68}
        size_hint: (0.42,0.42)
        on_press: root.manager.current = 'freshquestion'

    Image:
        id: img
        halign: 'left' 
        source: 'img/leather.png'
        pos_hint: {'center_x': 0.28,'center_y': 0.23}
        size_hint: (0.6,0.6)

    MDTextButton:
        text: 'Real Leather vs vegan leather?'
        halign: 'left' 
        font_name:"DMSans"
        font_size:12
        pos_hint: {'center_x': 0.28, 'center_y': 0.135}
        size_hint: (0.42,0.42)

    Image:
        id: img
        halign: 'left' 
        source: 'img/bus.png'
        pos_hint: {'center_x': 0.28,'center_y': 0.49}
        size_hint: (0.6,0.6)

    MDTextButton:
        text: 'Bus vs carpooling'
        halign: 'left' 
        font_name:"DMSans"
        font_size:12
        pos_hint: {'center_x': 0.28, 'center_y': 0.395}
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
        font_size:12
        pos_hint: {'center_x': 0.75, 'center_y': 0.68}
        size_hint: (0.42,0.42)

    Image:
        id: img
        halign: 'left' 
        source: 'img/cars.png'
        pos_hint: {'center_x': 0.75,'center_y': 0.49}
        size_hint: (0.6,0.6)

    MDTextButton:
        text: 'Cars vs motorcycles'
        halign: 'left' 
        font_name:"DMSans"
        font_size:12
        pos_hint: {'center_x': 0.75, 'center_y': 0.395}
        size_hint: (0.42,0.42)

    Image:
        id: img
        halign: 'left' 
        source: 'img/cotton.png'
        pos_hint: {'center_x': 0.75,'center_y': 0.23}
        size_hint: (0.6,0.6)

    MDTextButton:
        text: 'Organic cotton vs regular cotton'
        halign: 'left' 
        font_name:"DMSans"
        font_size:12
        pos_hint: {'center_x': 0.75, 'center_y': 0.126}
        size_hint: (0.42,0.42)

    MDIconButton:
        icon: "home"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.05}

    MDIconButton:
        icon: "account-outline"
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

    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.92, 'center_y': 0.95}
        on_press: root.manager.current = 'home'
        
<FoodQuestionList>:
    name: 'foodquestionlist'
    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.1, 'center_y': 0.96}
        on_press: root.manager.current = 'questionlist'

    MDLabel:
        text: 'Food Dilemmas'
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:18
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
        on_press: root.manager.current = 'freshquestion'

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
        on_press: root.manager.current = 'meatquestion'

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
        on_press: root.manager.current = 'milkquestion'

    MDTextButton:
        text: "See More"
        font_name:"DMSans"
        font_size:13
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.13}
        on_press: 
            root.manager.transition.direction = 'up'
            root.manager.current = 'foodquestionlist2'

    MDIconButton:
        icon: "chevron-down"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: 
            root.manager.transition.direction = 'up'
            root.manager.current = 'foodquestionlist2'  

    MDIconButton:
        icon: "home-outline"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.05}
        on_press: root.manager.current = 'questionlist'

    MDIconButton:
        icon: "account-outline"
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

<FoodQuestionList2>:
    name: 'foodquestionlist2'

    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.1, 'center_y': 0.96}
        on_press: root.manager.current = 'questionlist'

    MDLabel:
        text: 'More Food Dilemmas'
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:18
        pos_hint: {'center_x': 0.58, 'center_y': 0.9}
    Image:
        id: img
        halign: 'left' 
        source: 'img/compost.png'
        pos_hint: {'center_x': 0.28,'center_y': 0.79}
        size_hint: (0.6,0.6)

    MDTextButton:
        text: 'Should I compost organic waste?'
        halign: 'left' 
        font_name:"DMSans"
        font_size:13
        pos_hint: {'center_x': 0.28, 'center_y': 0.68}
        size_hint: (0.42,0.42)

    Image:
        id: img
        halign: 'left' 
        source: 'img/fruitwaste.png'
        pos_hint: {'center_x': 0.28,'center_y': 0.31}
        size_hint: (0.6,0.6)

    MDTextButton:
        text: 'Which fruit generate the least organic waste??'
        halign: 'left' 
        font_name:"DMSans"
        font_size:13
        pos_hint: {'center_x': 0.28, 'center_y': 0.20}
        size_hint: (0.42,0.42)

    Image:
        id: img
        halign: 'left' 
        source: 'img/vegetablewaste.png'
        pos_hint: {'center_x': 0.28,'center_y': 0.55}
        size_hint: (0.6,0.6)

    MDTextButton:
        text: 'Which vegetables generate the least organic waste?'
        halign: 'left' 
        font_name:"DMSans"
        font_size:13
        pos_hint: {'center_x': 0.28, 'center_y': 0.44}
        size_hint: (0.42,0.42)

    Image:
        id: img
        halign: 'left' 
        source: 'img/waste.png'
        pos_hint: {'center_x': 0.75,'center_y': 0.79}
        size_hint: (0.6,0.6)

    MDTextButton:
        text: 'How to reduce organic waste?'
        halign: 'left' 
        font_name:"DMSans"
        font_size:13
        pos_hint: {'center_x': 0.75, 'center_y': 0.68}
        size_hint: (0.42,0.42)

    Image:
        id: img
        halign: 'left' 
        source: 'img/zerowaste.png'
        pos_hint: {'center_x': 0.75,'center_y': 0.55}
        size_hint: (0.6,0.6)

    MDTextButton:
        text: 'Can I get organic waste down to zero?'
        halign: 'left' 
        font_name:"DMSans"
        font_size:13
        pos_hint: {'center_x': 0.75, 'center_y': 0.44}
        size_hint: (0.42,0.42)

    Image:
        id: img
        halign: 'left' 
        source: 'img/tea.png'
        pos_hint: {'center_x': 0.75,'center_y': 0.31}
        size_hint: (0.6,0.6)

    MDTextButton:
        text: 'Tea or coffee?'
        halign: 'left' 
        font_name:"DMSans"
        font_size:13
        pos_hint: {'center_x': 0.75, 'center_y': 0.20}
        size_hint: (0.42,0.42)



    MDIconButton:
        icon: "chevron-up"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.96}
        on_press: 
            root.manager.transition.direction = 'down'
            root.manager.current = 'foodquestionlist'        

    MDIconButton:
        icon: "home-outline"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.05}
        on_press: root.manager.current = 'questionlist'

    MDIconButton:
        icon: "account-outline"
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


<TransportQuestionList>:
    name: 'transportquestionlist'
    MDLabel:
        text: 'Transport Dilemmas'
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:18
        pos_hint: {'center_x': 0.63, 'center_y': 0.95}

    MDIconButton:
        icon: "home-outline"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.05}
        on_press: root.manager.current = 'questionlist'

    MDIconButton:
        icon: "account-outline"
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

<FashionQuestionList>:
    name: 'fashionquestionlist'
    MDLabel:
        text: 'Fashion Dilemmas'
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:18
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
        on_press: root.manager.current = 'freshquestion'

    Image:
        id: img
        halign: 'left' 
        source: 'img/meat.png'
        pos_hint: {'center_x': 0.28,'center_y': 0.15}
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
        pos_hint: {'center_x': 0.28, 'center_y': 0.49}
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
        pos_hint: {'center_x': 0.75, 'center_y': 0.45}
        size_hint: (0.42,0.42)

    Image:
        id: img
        halign: 'left' 
        source: 'img/milk.png'
        pos_hint: {'center_x': 0.75,'center_y': 0.1}
        size_hint: (0.6,0.6)

    MDTextButton:
        text: 'What type of milk is better?'
        halign: 'left' 
        font_name:"DMSans"
        font_size:13
        pos_hint: {'center_x': 0.75, 'center_y': 0.20}
        size_hint: (0.42,0.42)

    MDIconButton:
        icon: "home-outline"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.05}

    MDIconButton:
        icon: "account-outline"
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


<FreshQuestion>:
    name: 'freshquestion'

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
        on_press: root.manager.current = 'freshquestion'

    MDFillRoundFlatButton:
        text: "Fruits"
        font_name:"DMSans"
        theme_text_color: "Custom"
        pos_hint: {'center_x': 0.41, 'center_y': 0.49}
        size_hint: (0.15, 0.05)
        on_press: root.manager.current = 'freshquestion'     

    MDLabel:
        text: 'Fresh.\\n' +\
            '\\n' +\
            'There is no solid evidence that buying frozen vegetables benefits the environment but it is' +\
            'a proven fact that fresh vegetables are better for health.' 
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:15
        pos_hint: {'center_x': 0.5, 'center_y': 0.32}
        size_hint: (0.85, 0.4)

    MDFillRoundFlatIconButton:
        text: "Save"
        font_name:"DMSans"
        icon: "star-outline"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.73, 'center_y': 0.17}
        size_hint: (0.41, 0.06)
        on_press: root.manager.current = 'savedquestions'

    MDRoundFlatIconButton:
        text: "Share"
        font_name:"DMSans"
        icon: "share-variant"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.28, 'center_y': 0.17}
        size_hint: (0.41, 0.06)
        on_press: root.manager.current = 'freshquestion'

    MDTextButton:
        text: "See More"
        font_name:"DMSans"
        font_size:13
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.11}
        on_press: 
            root.manager.transition.direction = 'up'
            root.manager.current = 'freshquestion2'


    MDIconButton:
        icon: "chevron-down"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.09}
        on_press: 
            root.manager.transition.direction = 'up'
            root.manager.current = 'freshquestion2'        


    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.1, 'center_y': 0.96}
        on_press: root.manager.current = 'foodquestionlist'

    MDIconButton:
        icon: "home-outline"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.05}
        on_press: root.manager.current = 'questionlist'

    MDIconButton:
        icon: "account-outline"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.25, 'center_y': 0.05}
        on_press: root.manager.current = 'profile'

    MDIconButton:
        icon: "star-outline"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.75, 'center_y': 0.05}
        on_press: root.manager.current = 'freshquestion'






<Freshquestion2>:
    name: 'freshquestion2'

    MDLabel:
        text: 'Is it better to buy fresh or frozen vegetables?'
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:20
        pos_hint: {'center_x': 0.58, 'center_y': 0.9}



    MDLabel:
        text: 'Consider meal planning, so that the veggies you bought do not get spoiled. If you already' +\
            ' have something in your home that you are not sure you will eat in time (bought fresh), ' +\
            'consider freezing it while it is still edible or giving it away.' +\
            ' \\n' +\
            'What you do with the food you buy really matters. The majority of organic waste comes not from ' +\
            ' manufacturing facilities or food service, but from customers!' +\
            ' In 2016,it was estimated that 92 kg of fruit/ vegetables (per person per year) is thrown' +\
            ' away by consumers.' 

        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:13
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        size_hint: (0.85, 0.5)

    FloatLayout:
        Image:
            id: img
            halign: 'left' 
            source: 'img/piechart.png'
            pos_hint: {'center_x': 0.5,'center_y': 0.38}
            size_hint: (0.75,0.4)

    MDIconButton:
        icon: "chevron-up"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.96}
        on_press: 
            root.manager.transition.direction = 'down'
            root.manager.current = 'freshquestion'  

    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.1, 'center_y': 0.96}
        on_press: root.manager.current = 'foodquestionlist'

    MDIconButton:
        icon: "home-outline"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.05}
        on_press: root.manager.current = 'questionlist'

    MDIconButton:
        icon: "account-outline"
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
        on_press: root.manager.current = 'freshquestion2'

    MDRoundFlatIconButton:
        text: "Share"
        font_name:"DMSans"
        icon: "share-variant"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.28, 'center_y': 0.17}
        size_hint: (0.41, 0.06)
        on_press: root.manager.current = 'freshquestion'






<QuestionScreen3>:
    name: 'questionscreen3'


    MDIconButton:
        icon: "chevron-down"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.09}
        on_press: 
            root.manager.transition.direction = 'up'
            root.manager.current = 'questionscreen3'    

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
            pos_hint: {'center_x': 0.5,'center_y': 0.65}
            size_hint: (1,0.7)

    MDLabel:
        text: 'Avoidable VS Unavoidable Waste'
        halign: 'center' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:16
        pos_hint: {'center_x': 0.5, 'center_y': 0.45}

    MDLabel:
        text: 'Unavoidable waste for fruit and vegetables'
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:16
        pos_hint: {'center_x': 0.63, 'center_y': 0.42}

    MDLabel:
        text: 'Unavoidable waste is the inedible fraction of the fruit and vegetables (e.g. peeling, trimmings). Its '+\
            ' never eaten. It can be composted, some of it can be reused on manufacturing level (e. g. coconut shells).'


        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:15
        pos_hint: {'center_x': 0.5, 'center_y': 0.31}
        size_hint: (0.85, 0.5) 

    MDIconButton:
        icon: "chevron-down"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: 
            root.manager.transition.direction = 'up'
            root.manager.current = 'questionscreen4'   

    MDIconButton:
        icon: "chevron-up"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.96}
        on_press: 
            root.manager.transition.direction = 'down'
            root.manager.current = 'questionscreen2'  

    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.1, 'center_y': 0.96}
        on_press: root.manager.current = 'questionlist'

    MDIconButton:
        icon: "home-outline"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.05}
        on_press: root.manager.current = 'questionlist'

    MDIconButton:
        icon: "account-outline"
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
        on_press: root.manager.current = 'freshquestion'

    MDRoundFlatIconButton:
        text: "Share"
        font_name:"DMSans"
        icon: "share-variant"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.28, 'center_y': 0.17}
        size_hint: (0.41, 0.06)
        on_press: root.manager.current = 'freshquestion'

<QuestionScreen4>:
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
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: 
            root.manager.transition.direction = 'up'
            root.manager.current = ''        

    MDIconButton:
        icon: "chevron-up"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.96}
        on_press: 
            root.manager.transition.direction = 'down'
            root.manager.current = 'questionscreen3'  

    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.1, 'center_y': 0.96}
        on_press: root.manager.current = 'questionlist'

    MDIconButton:
        icon: "home-outline"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.05}
        on_press: root.manager.current = 'questionlist'

    MDIconButton:
        icon: "account-outline"
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
        on_press: root.manager.current = 'freshquestion'

    MDRoundFlatIconButton:
        text: "Share"
        font_name:"DMSans"
        icon: "share-variant"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.28, 'center_y': 0.17}
        size_hint: (0.41, 0.06)
        on_press: root.manager.current = 'freshquestion'


<SavedQuestions>:
    name: 'savedquestions'

    MDLabel:
        text: 'Food Dilemmas'
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:18
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
        on_press: root.manager.current = 'freshquestion'

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

    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.1, 'center_y': 0.95}
        on_press: root.manager.current = 'profile'

    MDIconButton:
        icon: "home-outline"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.05}
        on_press: root.manager.current = 'questionlist'

    MDIconButton:
        icon: "star"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.75, 'center_y': 0.05}
        on_press: root.manager.current = 'savedquestions'   

    MDIconButton:
        icon: "account-outline"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.25, 'center_y': 0.05}
        on_press: root.manager.current = 'profile'




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

    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.1, 'center_y': 0.96}
        on_press: root.manager.current = 'questionlist'

    MDLabel:
        text: 'Profile'
        halign: "center"
        theme_text_color: "Primary"
        font_style: "H6"
        font_name:"DMSans"
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}

    FloatLayout:
        Image:
            id: img
            source: 'img/Healthy life.png'
            size_hint: (0.4,0.4)
            pos_hint: {'center_x': 0.5, 'center_y': 0.9}

    MDLabel:
        text: 'Habits'
        font_name:"DMSans"
        font_size:19
        halign: "left"
        theme_text_color: "Primary"
        pos_hint:{'center_x': 0.5, 'center_y': 0.73}  
        size_hint: (0.8, 0.5)

    MDIconButton:
        icon: "pencil"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.9, 'center_y': 0.73}
        size_hint: (0.007, 0.007)
        on_press: root.manager.current = 'habitsedit'   

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
        pos_hint:{'center_x': 0.55, 'center_y': 0.63}
        size_hint: (0.8, 0.4)

    MDLabel:
        text: 'Location'
        font_name:"DMSans"
        font_size:19
        halign: "left"
        theme_text_color: "Primary"
        pos_hint:{'center_x': 0.5, 'center_y': 0.48}
        size_hint: (0.8, 0.5)

    MDLabel:
        text: 'Netherlands'
        font_name:"DMSans"
        font_size:15
        halign: "left"
        theme_text_color: "Primary"
        pos_hint:{'center_x': 0.5, 'center_y': 0.44}
        size_hint: (0.8, 0.5)


    MDIconButton:
        icon: "pencil"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.9, 'center_y': 0.48}
        size_hint: (0.007, 0.007)
        on_press: root.manager.current = 'locationedit'   


    MDLabel:
        text: 'Profile'
        font_name:"DMSans"
        font_size:19
        halign: "left"
        theme_text_color: "Primary"
        pos_hint:{'center_x': 0.5, 'center_y': 0.35}
        size_hint: (0.8, 0.5)


    MDLabel:
        text: 'Email:                   email@email.com'
        font_name:"DMSans"
        font_size:15
        halign: "left"
        theme_text_color: "Primary"
        pos_hint:{'center_x': 0.5, 'center_y': 0.31}
        size_hint: (0.8, 0.5)

    MDIconButton:
        icon: "pencil"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.9, 'center_y': 0.31}
        size_hint: (0.007, 0.007)
        on_press: root.manager.current = 'resetemail'

    MDLabel:
        text: 'Password:           ***********'
        font_name:"DMSans"
        font_size:15
        halign: "left"
        theme_text_color: "Primary"
        pos_hint:{'center_x': 0.5, 'center_y': 0.26}
        size_hint: (0.8, 0.5)

    MDIconButton:
        icon: "pencil"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.9, 'center_y': 0.26}
        size_hint: (0.007, 0.007)
        on_press: root.manager.current = 'resetpassword'

    MDIconButton:
        icon: "home-outline"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.05}
        on_press: root.manager.current = 'questionlist'

    MDIconButton:
        icon: "star-outline"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.75, 'center_y': 0.05}
        on_press: root.manager.current = 'savedquestions'   

    MDIconButton:
        icon: "account"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.25, 'center_y': 0.05}
        on_press: root.manager.current = 'profile'

    FloatLayout:
        Image:
            id: img
            source: 'img/By logo.png'
            pos_hint: {'center_x': 0.5,'center_y': 0.12}
            size_hint: (0.5,0.5)


<HabitsEdit>:
    name: 'habitsedit'

    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.1, 'center_y': 0.96}
        on_press: root.manager.current = 'profile'

    MDLabel:
        text: 'Tell us your habits'
        halign: "center"
        theme_text_color: "Primary"
        font_style: "H6"
        font_name:"DMSans"
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}

    MDLabel:
        text: 'We use this information to suggest more relevant dilemmas to you'
        font_style: "Subtitle2"
        font_name:"DMSans"
        halign: "center"
        theme_text_color: "Primary"
        pos_hint:{'center_x': 0.5, 'center_y': 0.75}
        size_hint: (0.8, 0.5)

    FloatLayout:
        Image:
            id: img
            source: 'img/Healthy life.png'
            size_hint: (0.4,0.4)
            pos_hint: {'center_x': 0.5, 'center_y': 0.9}

    MDFillRoundFlatButton:
        text: "Save"
        font_name:"DMSans"
        theme_text_color: "Custom"
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        size_hint: (0.9, 0.08)
        on_press: root.manager.current = 'profile'

<LocationEdit>:
    name: 'locationedit'

    FloatLayout:
        Image:
            id: img
            source: 'img/location.png'
            size_hint: (0.4,0.4)
            pos_hint: {'center_x': 0.5, 'center_y': 0.9}

    
    
    MDLabel:
        text: 'Where are you?'
        halign: "center"
        theme_text_color: "Primary"
        font_style: "H6"
        font_name:"DMSans"
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}

    MDLabel:
        text: 'We will find more accurate information according to your location'
        font_style: "Subtitle2"
        font_name:"DMSans"
        halign: "center"
        theme_text_color: "Primary"
        pos_hint:{'center_x': 0.5, 'center_y': 0.75}
        size_hint: (0.8, 0.5)

    MDTextField:
        hint_text: "Enter Location"
        font_name:"DMSans"
        icon_right: "map-marker"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        size_hint_x:None
        width:330
        
    MDIconButton:
        icon: "map-marker"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.25  , 'center_y': 0.925}
        size_hint: (0.1, 0.1)
        user_font_size: "35sp"

    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.1, 'center_y': 0.96}
        on_press: root.manager.current = 'profile'


    MDFillRoundFlatButton:
        text: "Save"
        font_name:"DMSans"
        theme_text_color: "Custom"
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        size_hint: (0.9, 0.08)
        on_press: root.manager.current = 'profile'




<ResetEmail>:
    name: 'resetemail'

    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.1, 'center_y': 0.96}
        on_press: root.manager.current = 'profile'

    MDLabel:
        text: 'Choose a new email'
        halign: "center"
        theme_text_color: "Primary"
        font_style: "H6"
        font_name:"DMSans"
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}


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
        pos_hint: {'center_x': 0.8, 'center_y': 0.45}
        on_press: root.manager.current = 'profile'

    MDIconButton:
        icon: "home-outline"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: root.manager.current = 'questionlist'




<MilkQuestion>:
    name: 'milkquestion'

    MDLabel:
        text: 'Milk substitutes: soy, oat, rice or almond drink?'
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:20
        pos_hint: {'center_x': 0.52, 'center_y': 0.9}
        size_hint: (0.9,0.7)


    FloatLayout:
        Image:
            id: img
            halign: 'left' 
            source: 'img/milkQ.png'
            pos_hint: {'center_x': 0.5,'center_y': 0.69}
            size_hint: (1,0.7)

    MDFillRoundFlatButton:
        text: "Vegan"
        font_name:"DMSans"
        theme_text_color: "Custom"
        pos_hint: {'center_x': 0.18, 'center_y': 0.49}
        size_hint: (0.15, 0.05)
        on_press: root.manager.current = 'milkquestion'

    MDFillRoundFlatButton:
        text: "Drinks"
        font_name:"DMSans"
        theme_text_color: "Custom"
        pos_hint: {'center_x': 0.41, 'center_y': 0.49}
        size_hint: (0.15, 0.05)
        on_press: root.manager.current = 'milkquestion'     

    MDLabel:
        text: '\\n' +\
            'Oat. !\\n' +\
            'According to a recent Oxford study, oat milk is the most sustainable option when it comes to milk' +\
            ' substitutes. If we look at greenhouse gases emissions, all four drinks score around three times better'+ \
            ' than cows milk. There is no solid evidence that buying frozen vegetables benefits the environment but'+ \
            ' it is. ' +\
            'Even though almond milk shows the lowest emissions, its production is still very harmful to the' +\
            ' environment.' 
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:13
        pos_hint: {'center_x': 0.5, 'center_y': 0.35}
        size_hint: (0.85, 0.4)

    MDFillRoundFlatIconButton:
        text: "Save"
        font_name:"DMSans"
        icon: "star-outline"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.73, 'center_y': 0.17}
        size_hint: (0.41, 0.06)
        on_press: root.manager.current = 'savedquestions'

    MDRoundFlatIconButton:
        text: "Share"
        font_name:"DMSans"
        icon: "share-variant"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.28, 'center_y': 0.17}
        size_hint: (0.41, 0.06)
        on_press: root.manager.current = 'milkquestion'

    MDTextButton:
        text: "See More"
        font_name:"DMSans"
        font_size:13
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.11}
        on_press: 
            root.manager.transition.direction = 'up'
            root.manager.current = 'milkquestion2'


    MDIconButton:
        icon: "chevron-down"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.09}
        on_press: 
            root.manager.transition.direction = 'up'
            root.manager.current = 'milkquestion2'        


    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.1, 'center_y': 0.96}
        on_press: root.manager.current = 'foodquestionlist'

    MDIconButton:
        icon: "home-outline"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.05}
        on_press: root.manager.current = 'questionlist'

    MDIconButton:
        icon: "account-outline"
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


<MilkQuestion2>:
    name: 'milkquestion2'

    MDLabel:
        text: 'Milk substitutes: soy, oat, rice or almond drink?'
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:20
        pos_hint: {'center_x': 0.52, 'center_y': 0.9}
        size_hint: (0.9,0.7)

    MDLabel:
        text: 'The choice of the most sustainable dairy alternative is not straightforward. ' +\
            ' \\n' +\
            'One should look not only at CO2 emissions but also at environmental side effects, and of course at' +\
            ' the nutritional value. Rice milk scores low in terms of the latter two: little nutrition, a lot of ' +\
            ' CO2e. However, when it comes to the production drawbacks, almond is the least attractive option.' +\
            ' Production of one glass of almond milk leads to only 140g CO2e emissions but requires almost 74 liter' +\
            ' of water, more than any other milk substitute. This means that almond farming, which is mainly located' +\
            ' in California, US, has a drought effect on the environment, not to mention the high pressure on ' +\
            ' honeybees.' 
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:13
        pos_hint: {'center_x': 0.5, 'center_y': 0.68}
        size_hint: (0.85, 0.5)

    FloatLayout:
        Image:
            id: img
            halign: 'left' 
            source: 'img/milkbargraph.png'
            pos_hint: {'center_x': 0.5,'center_y': 0.34}
            size_hint: (0.55,0.4)

    MDTextButton:
        text: "See More"
        font_name:"DMSans"
        font_size:13
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.11}
        on_press: 
            root.manager.transition.direction = 'up'
            root.manager.current = 'milkquestion3'        

    MDIconButton:
        icon: "chevron-down"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.09}
        on_press: 
            root.manager.transition.direction = 'up'
            root.manager.current = 'milkquestion3'        

    MDIconButton:
        icon: "chevron-up"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.96}
        on_press: 
            root.manager.transition.direction = 'down'
            root.manager.current = 'milkquestion'  

    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.1, 'center_y': 0.96}
        on_press: root.manager.current = 'foodquestionlist'

    MDIconButton:
        icon: "home-outline"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.05}
        on_press: root.manager.current = 'questionlist'

    MDIconButton:
        icon: "account-outline"
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
        on_press: root.manager.current = 'savedquestions'

    MDRoundFlatIconButton:
        text: "Share"
        font_name:"DMSans"
        icon: "share-variant"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.28, 'center_y': 0.17}
        size_hint: (0.41, 0.06)
        on_press: root.manager.current = 'milkquestion2'



<MilkQuestion3>:
    name: 'milkquestion3'

    MDLabel:
        text: 'Milk substitutes: soy, oat, rice or almond drink?'
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:20
        pos_hint: {'center_x': 0.52, 'center_y': 0.9}
        size_hint: (0.9,0.7)

    MDLabel:
        text: 'Although soy production is exhausting for the environment because it causes deforestation, its main ' +\
            ' use is cattle feed and not human consumption. In other words, soy drink is a sustainable alternative' +\
            ' to milk as it cuts the food chain in half. The choice of the most sustainable dairy alternative is not' +\
            ' straightforward. ' +\
            ' \\n' +\
            'It is important to note though that consuming enough dairy products every day is still very important.' +\
            ' Soy drink does not have the same health effects as dairy, but often contains added vitamin B12 and' +\
            'calcium. The nutritional value of oat drink compares to soy, and there are no environmental' +\
            ' consequences associated with its consumption, even taken into account its increasing popularity: the' +\
            ' Oxford study declared it the winner in the battle of plant-based drinks.' +\
            ' \\n' +\
            'The Guardian expects another major player to join the battle soon: hazelnuts. In the meantime, you can ' +\
            ' give oat and/or soy drink a try by putting them in your porridge, pancake batter, coffee or tea. It' +\
            ' might take some time to get used to the new taste, but even if it still does not taste good after a ' +\
            ' while, do not worry - new alternatives are coming!' 

        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:13
        pos_hint: {'center_x': 0.5, 'center_y': 0.55}
        size_hint: (0.85, 0.5)

    MDIconButton:
        icon: "chevron-up"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.96}
        on_press: 
            root.manager.transition.direction = 'down'
            root.manager.current = 'milkquestion2'  

    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.1, 'center_y': 0.96}
        on_press: root.manager.current = 'foodquestionlist'

    MDIconButton:
        icon: "home-outline"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.05}
        on_press: root.manager.current = 'questionlist'

    MDIconButton:
        icon: "account-outline"
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
        on_press: root.manager.current = 'freshquestion'

    MDRoundFlatIconButton:
        text: "Share"
        font_name:"DMSans"
        icon: "share-variant"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.28, 'center_y': 0.17}
        size_hint: (0.41, 0.06)
        on_press: root.manager.current = 'freshquestion'




<MeatQuestion>:
    name: 'meatquestion'

    MDLabel:
        text: 'Chicken, pork or beef?'
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:20
        pos_hint: {'center_x': 0.52, 'center_y': 0.9}
        size_hint: (0.9,0.7)


    FloatLayout:
        Image:
            id: img
            halign: 'left' 
            source: 'img/milkQ.png'
            pos_hint: {'center_x': 0.5,'center_y': 0.69}
            size_hint: (1,0.7)

    MDFillRoundFlatButton:
        text: "Vegan"
        font_name:"DMSans"
        theme_text_color: "Custom"
        pos_hint: {'center_x': 0.18, 'center_y': 0.49}
        size_hint: (0.15, 0.05)
        on_press: root.manager.current = 'milkquestion'

    MDFillRoundFlatButton:
        text: "Drinks"
        font_name:"DMSans"
        theme_text_color: "Custom"
        pos_hint: {'center_x': 0.41, 'center_y': 0.49}
        size_hint: (0.15, 0.05)
        on_press: root.manager.current = 'milkquestion'     

    MDLabel:
        text: 'Chicken. Pork is the second best option.'  +\
            '\\n' +\
            '\\n' +\
            ' All meat products have a high environmental impact, but the impact of beef is almost three times ' +\
            ' higher than that of chicken or pork. Consider eating less meat: this is good for the climate because ' +\
            ' around 5 kg of plant-based feed is needed to produce 1 kg of meat.'             
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:13
        pos_hint: {'center_x': 0.5, 'center_y': 0.35}
        size_hint: (0.85, 0.4)

    MDFillRoundFlatIconButton:
        text: "Save"
        font_name:"DMSans"
        icon: "star-outline"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.73, 'center_y': 0.17}
        size_hint: (0.41, 0.06)
        on_press: root.manager.current = 'savedquestions'

    MDRoundFlatIconButton:
        text: "Share"
        font_name:"DMSans"
        icon: "share-variant"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.28, 'center_y': 0.17}
        size_hint: (0.41, 0.06)
        on_press: root.manager.current = 'meatquestion'

    MDTextButton:
        text: "See More"
        font_name:"DMSans"
        font_size:13
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.11}
        on_press: 
            root.manager.transition.direction = 'up'
            root.manager.current = 'meatquestion2'


    MDIconButton:
        icon: "chevron-down"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.09}
        on_press: 
            root.manager.transition.direction = 'up'
            root.manager.current = 'meatquestion2'        


    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.1, 'center_y': 0.96}
        on_press: root.manager.current = 'foodquestionlist'

    MDIconButton:
        icon: "home-outline"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.05}
        on_press: root.manager.current = 'questionlist'

    MDIconButton:
        icon: "account-outline"
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


<MeatQuestion2>:
    name: 'meatquestion2'

    MDLabel:
        text: 'Chicken, pork or beef?'
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:20
        pos_hint: {'center_x': 0.52, 'center_y': 0.9}
        size_hint: (0.9,0.7)

    MDLabel:
        text: 'According to CE Delft, the price of beef should be around 40% higher if the damage to the environment' +\
            ' had been calculated in its price. Beef industry produces large amounts of manure and ammonia emissions' +\
            ' and leads to deterioration of air- and water quality. For example, a weekly meal of steak for a' +\
            'family of 4 people produces 700 kilos of CO2 emissions on an annual basis. The choice of the most' +\
            'sustainable dairy alternative is not straightforward. ' 
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:13
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        size_hint: (0.85, 0.5)

    FloatLayout:
        Image:
            id: img
            halign: 'left' 
            source: 'img/meatpiechart.png'
            pos_hint: {'center_x': 0.5,'center_y': 0.34}
            size_hint: (0.8,0.5)

    MDLabel:
        text: 'Emissions per kg of meat' 
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:16
        pos_hint: {'center_x': 0.5, 'center_y': 0.52}
        size_hint: (0.85, 0.5)
        
    MDTextButton:
        text: "See More"
        font_name:"DMSans"
        font_size:13
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.11}
        on_press: 
            root.manager.transition.direction = 'up'
            root.manager.current = 'meatquestion3'        

    MDIconButton:
        icon: "chevron-down"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.09}
        on_press: 
            root.manager.transition.direction = 'up'
            root.manager.current = 'meatquestion3'        

    MDIconButton:
        icon: "chevron-up"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.96}
        on_press: 
            root.manager.transition.direction = 'down'
            root.manager.current = 'meatquestion'  

    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.1, 'center_y': 0.96}
        on_press: root.manager.current = 'foodquestionlist'

    MDIconButton:
        icon: "home-outline"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.05}
        on_press: root.manager.current = 'questionlist'

    MDIconButton:
        icon: "account-outline"
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
        on_press: root.manager.current = 'savedquestions'

    MDRoundFlatIconButton:
        text: "Share"
        font_name:"DMSans"
        icon: "share-variant"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.28, 'center_y': 0.17}
        size_hint: (0.41, 0.06)
        on_press: root.manager.current = 'meatquestion2'



<MeatQuestion3>:
    name: 'meatquestion3'

    MDLabel:
        text: 'Chicken, pork or beef?'
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:20
        pos_hint: {'center_x': 0.52, 'center_y': 0.9}
        size_hint: (0.9,0.7)

    MDLabel:
        text: 'According to CE Delft, the price of beef should be around 40% higher if the damage to the environment' +\
            ' had been calculated in its price. Beef industry produces large amounts of manure and ammonia emissions' +\
            ' and leads to deterioration of air- and water quality. For example, a weekly meal of steak for a' +\
            'family of 4 people produces 700 kilos of CO2 emissions on an annual basis. The choice of the most' +\
            'sustainable dairy alternative is not straightforward. ' 
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:13
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        size_hint: (0.85, 0.5)

    FloatLayout:
        Image:
            id: img
            halign: 'left' 
            source: 'img/meatpiechart.png'
            pos_hint: {'center_x': 0.5,'center_y': 0.34}
            size_hint: (0.8,0.5)

    MDLabel:
        text: 'Emissions per kg of meat' 
        halign: 'left' 
        font_name:"DMSans"
        theme_text_color: "Primary"
        font_size:16
        pos_hint: {'center_x': 0.5, 'center_y': 0.52}
        size_hint: (0.85, 0.5)
        
    MDTextButton:
        text: "See More"
        font_name:"DMSans"
        font_size:13
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.11}
        on_press: 
            root.manager.transition.direction = 'up'
            root.manager.current = 'meatquestion3'        

    MDIconButton:
        icon: "chevron-down"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.09}
        on_press: 
            root.manager.transition.direction = 'up'
            root.manager.current = 'meatquestion3'        

    MDIconButton:
        icon: "chevron-up"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.96}
        on_press: 
            root.manager.transition.direction = 'down'
            root.manager.current = 'meatquestion'  

    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.1, 'center_y': 0.96}
        on_press: root.manager.current = 'foodquestionlist'

    MDIconButton:
        icon: "home-outline"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.05}
        on_press: root.manager.current = 'questionlist'

    MDIconButton:
        icon: "account-outline"
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
        on_press: root.manager.current = 'savedquestions'

    MDRoundFlatIconButton:
        text: "Share"
        font_name:"DMSans"
        icon: "share-variant"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.28, 'center_y': 0.17}
        size_hint: (0.41, 0.06)
        on_press: root.manager.current = 'meatquestion3'

"""


##Define screen classes
class LocationEdit(Screen):
    pass


class HabitsEdit(Screen):
    def load_table(self):
        layout = AnchorLayout()
        self.data_tables = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.48},
            size_hint=(0.95, 0.42),
            check=True,
            rows_num=10,
            column_data=[
                ("", dp(12)),
                ("Habits", dp(70))],
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


class ResetEmail(Screen):
    pass


class Profile(Screen):
    pass


class FoodQuestionList2(Screen):
    pass


class FoodQuestionList(Screen):
    pass


class FashionQuestionList(Screen):
    pass


class TransportQuestionList(Screen):
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


class FreshQuestion(Screen):
    pass


class FreshQuestion2(Screen):
    pass


class MilkQuestion(Screen):
    pass


class MilkQuestion2(Screen):
    pass

class MilkQuestion3(Screen):
    pass

class MeatQuestion(Screen):
    pass


class MeatQuestion2(Screen):
    pass

class MeatQuestion3(Screen):
    pass

class LogIn(Screen):
    pass


class First(Screen):
    pass


class Error(Screen):
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
            pos_hint={'center_x': 0.5, 'center_y': 0.48},
            size_hint=(0.95, 0.42),
            check=True,
            rows_num=10,
            column_data=[
                ("", dp(12)),
                ("Habits", dp(70))],
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
sm.add_widget(FreshQuestion(name='freshquestion'))
sm.add_widget(FreshQuestion2(name='freshquestion2'))
sm.add_widget(MilkQuestion(name='milkquestion'))
sm.add_widget(MilkQuestion2(name='milkquestion2'))
sm.add_widget(MilkQuestion3(name='milkquestion3'))
sm.add_widget(MeatQuestion(name='meatquestion'))
sm.add_widget(MeatQuestion2(name='meatquestion2'))
sm.add_widget(MeatQuestion3(name='meatquestion3'))
sm.add_widget(First(name='first'))
sm.add_widget(Error(name='error'))
sm.add_widget(Home(name='home'))
sm.add_widget(Habits(name='habits'))
sm.add_widget(Location(name='location'))
sm.add_widget(LogIn(name='login'))
sm.add_widget(Dilemmas(name='dilemmas'))
sm.add_widget(Signup(name='signup'))
sm.add_widget(SignupLater(name='signuplater'))
sm.add_widget(Navbar(name='navbar'))
sm.add_widget(ToolBar(name='toolbar'))
sm.add_widget(NewPassword(name='newpassword'))
sm.add_widget(ResetPassword(name='resetpassword'))
sm.add_widget(QuestionScreen3(name='questionscreen3'))
sm.add_widget(FoodQuestionList(name='foodquestionlist'))
sm.add_widget(FoodQuestionList2(name='foodquestionlist2'))
sm.add_widget(QuestionList(name='questionlist'))
sm.add_widget(QuestionList2(name='questionlist2'))
sm.add_widget(Profile(name='profile'))
sm.add_widget(ResetEmail(name='resetemail'))
sm.add_widget(HabitsEdit(name='habitsedit'))
sm.add_widget(LocationEdit(name='locationedit'))
sm.add_widget(TransportQuestionList(name='transportquestionlist'))
sm.add_widget(FashionQuestionList(name='fashionquestionlist'))


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
