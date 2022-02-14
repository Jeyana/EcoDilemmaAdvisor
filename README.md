# EcoDilemmaAdvisor by Dinosavvy

#### Team: Jeyana Morozenko, Amr Othman, Emilia Azuma, Olga Schilling
#### Mentor: Bas Visser


## Introduction

Imagine: you are standing in the supermarket staring at cucumbers. You doubt which one is more sustainable to buy: the cucumber wrapped in plastic or the organic one without packaging, taking the risk that the latter might end up rotting in your fridge. You feel overwhelmed already while the meat section is still three rows ahead. What a pain!

Making a sustainable choice is usually tough for a consumer because there is rarely a straightforward answer, and it requires a lot of research to come up with one.

This is where the EcoDilemmaAdvisor app comes in handy. The goal of the app is to provide the user with concise, fact-driven advice on the potential impact of their choices on the environment. The app has two main characteristics: firstly, it’s instant, which means the user gets an answer to their dilemma right away; and secondly, it’s positive, which means that the app does not blame the consumer for their choices and tries to leave options open. These two features distinguish the app from the other similar tools and websites out there.

![High fidelity welcome]
![High fidelity food category]

## Dinosavvy on a mission

Starting with this idea, we set off on a journey. The Dinosavvy team of four combined the Data Science and UX Design tracks in equal proportions. However, in the middle of the project, we felt it made more sense to shift more weight to DS as UX was going well. From the very beginning, we limited the scope of the dilemmas to the food category and decided to go for quality instead of quantity in the research. Instant does not mean superficial: quite the opposite, it takes a lot of in-depth study of the subject to develop a concise and fact-driven answer. It became our main focus reflected both in the UX and DS tracks.

## UX dilemmas

![Anna user story](https://raw...)

Having sketched our users and their stories in Figma (you can appreciate our exquisite drawing skills above), we had a few questions to answer. Does the user have to create an account to access the app? Should we praise the user for making an environmentally-friendly choice? Is it even possible to stay positive, taking into account the seriousness of the climate crisis? How is it possible to formulate a concise answer to a dilemma when all the answers actually start with “It all depends…”? How do we give users the possibility to verify the answers and access the data they are based on without overloading them with information? 

To answer these questions, we started testing early on with a lo-fi prototype. The first testing round already gave us a clear idea about our user's needs and helped correct navigation errors and add useful features. For example, three out of five testers requested a related dilemmas section: even when looking up one question, you want to keep scrolling.

![EcoDilemmaAdvisor low-fidelity prototype]

The testing left us no doubt: in a world where you have to enter your details to buy a movie ticket, most users are exhausted by the endless stream of accounts they have to create. As one of our testers put it: "I want to see what an app has to offer before I leave any of my personal details." That is why we gave our users an option to skip personalization and proceed to ask questions straight away. Those who opt for personalization can add their habits to reflect their lifestyles and values. The idea for the future is to adjust answers based on the user's personality with the help of machine learning.

Upon selecting a dilemma, the user gets an instant answer with a short explanation and a 'Read More' button with expanding content. The latter includes more information on the subject, limitations, graphs, sources and tips. Our users loved it!

## Data dilemmas

We started by defining a few dilemmas and diving into the Eurostat databases to find the answers. For example, we tried to answer a question on the sustainability of washable plastic containers based on the recycling rate of packaging waste by the type of packaging, but with little success. Every eco dilemma requires analysis of dozens and dozens of data sources, and an answer based on just one dataset will hardly ever be complete.

We discovered that the most suitable methodology here is Life Cycle Assessment (LCA), which means that the environmental impact of every single stage of a product life cycle is calculated: from manufacturing to recycling. Because of the complexity of these calculations, researchers and consultants use LCA-databases, such as Ecoinvent or Agri-footprint. However, since these databases are not open-source, we could not work with them directly.

We focused on what *individuals* can do to reduce their footprint. We questioned commonly given advice and dived deep into various aspects of everyday consumer decisions. In many cases, we ended up reading existing studies and meta-analyses, translating the findings into simple and friendly language, and visualizing already condensed numerical data. In addition to that, we came back to the raw data from Eurostat, which is, luckily, available for free. 

## Tools

### Communication and collaboration

We had a live online meeting every week (30-60 minutes) and communicated via a Slack group channel between meetings. To collaborate throughout the project, the programmers used Git, and the designers used Figma. We highly recommend both Git and Figma. Git can be intimidating for a beginner, but you definitely need it if you have more than one programmer on the team.

### UI/UX Design

![EcoDilemmaAdvisor high-fidelity prototype, Dilemma screens]()

We used Figma for the entire design process, which was great for a remote team like us. It's cloud-based, just like Google Docs. This means that it's always live and up to date and that designers and developers can work on the same file, making communication very smooth.

Figma is intuitive enough so that a beginner wouldn't feel intimidated (there are tons of tutorials on Youtube, both official and non-official). Still, it can also be very advanced with all the prototyping features. We're still on the journey of exploring the possibilities, and it seems there's a long way to go. It's been great to learn how easy it is to create and edit the design system with components, and how plugins (Better font Picker, Iconify, Unsplash to name a few) make the workflow much quicker. 

### Data Science 

Most of the code for EcoDilemmaAdvisor was written in **Python**. Python might seem weird at first for someone transferring from another programming language, but it soon wins you over with its conciseness and elegance. It's a great language for beginners because it reads almost like English if the code is written with care.

**PyCharm** was the IDE we chose to use (the free Community version was enough). Packages and environments were managed by **Conda**.

Before coming up with a concrete answer to an eco-related question, we explored the data and tried out different visualizations in **Jupyter Notebooks**. This tool allows having formatted text + an unlimited number of code cells and their output all in one place, in an organized and readable way. For someone who already can write Python code, getting used to Jupyter takes only a couple of hours, and if you want to try it out without bothering to install it first, there is Google Colab, which is very much like Jupyter but runs in the cloud.

All graphs in EcoDilemmaAdvisor are made using **Matplotlib**, a Python library which, despite being huge, is easy to get started with (using this short tutorial, for example).

![Matplotlib bar plot from exploratory Jupyter Notebook]

Matplotlib is integrated with **Pandas**, another python library with a handy DataFrame type. The latter looks very much like an Excel table and supports (almost) all imaginable operations on data. With Pandas, importing a .csv into your code is as simple as:

~~~
recycling_rate = pandas.read_csv('recycling_rate.csv')
~~~

In order to make the calculations run faster, instead of native Python data structures (list, dictionary, set, tuple) Pandas uses ndarray type from **NumPy** library. The bigger the datasets you're using, the more important speed becomes, so NumPy is also a must-know for a data scientist. In our case, the learning order was Python basics -> Matplotlib -> Pandas -> Numpy, and it worked fine.

### Software development

![App screenshot]

We used **Kivy** and **KivyMD** frameworks to develop the graphical user interface (GUI) for Android and iOS. Kivy is an open-source Python framework for developing mobile apps and other multitouch application software with a natural user interface (NUI). To create a more attractive GUI, KivyMD was used. KivyMD applies the concept of Material Design (developed by Google, https://material.io/design/introduction) to provide widgets that can be used with Kivy. KivyMD framework is similar to Kivy but has a more attractive GUI. In short, you can say that KivyMD depends on Kivy.

Operating with Kivy or KivyMD is relatively straightforward, and we recommend using it for developing simple mobile applications in Python. There's a wide variety of buttons and icons to choose from. To add an icon, you can search for possible icons in https://materialdesignicons.com/; then you can copy the icon identifier and include it in your Python code. 

## Conclusion

In the end, we had three main puzzle pieces: a high-fidelity prototype, answers to dozens of eco dilemmas (Chicken, pork or beef? Tea or coffee? etc.), and a skeleton of the app written in Python. None of the team members had experience as a frontend developer, so we didn't manage to create a perfect mobile app in two months, but we put together a decent proof of concept.

We did not expect the eco dilemmas to be that complicated and tough to answer. Looking for answers is very interesting, though, and we encourage everyone to do it — it might be depressing sometimes, but it gives you plenty of dinner table conversation topics. There are a lot of good sources online to satisfy your curiosity: Milieucentraal (in Dutch), Climate change food calculator, or this book on the carbon footprint of everything, to name a few. 

We strongly believe the EcoDilemmaAdvisor app would be a valuable addition to every smartphone as the environmental crisis is everyone's problem, and this app is a tool to find solutions. The next steps in developing this project would include defining and researching dilemmas for other categories such as household and transport and incorporating machine learning into the app. Hopefully, this app will have a future.

Everyone here in the Dinosavvy team enjoyed the collaboration process a lot. We worked on the project from the Netherlands, Ukraine, Brazil and Argentina; in the middle of moving houses and driving through Patagonia. Thank you, TechLabs! It was a great adventure! 