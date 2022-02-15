# EcoDilemmaAdvisor by Dinosavvy

**Team**: Jeyana Morozenko, Amr Othman, Emilia Azuma, Olga Schilling<br>
**Mentor**: Bas Visser

## Contents
[Introduction](#introduction)<br>
[Dinosavvy on a mission](#dinosavvy-on-a-mission)<br>
[UX dilemmas](#ux-dilemmas)<br>
[Data dilemmas](#data-dilemmas)<br>
[Tools](#tools)<br>
[Results](#results)<br>
[Conclusion](#conclusion)

## Introduction

Imagine: you are standing in the supermarket staring at cucumbers. You doubt which one is more sustainable to buy: the cucumber wrapped in plastic or the organic one without packaging, taking the risk that the latter might end up rotting in your fridge. You feel overwhelmed already while the meat section is still three rows ahead. What a pain!

Making a sustainable choice is usually tough for a consumer because there is rarely a straightforward answer, and it requires a lot of research to come up with one.

This is where the EcoDilemmaAdvisor app comes in handy. The goal of the app is to provide the user with concise, fact-driven advice on the potential impact of their choices on the environment. The app has two main characteristics: firstly, it’s instant, which means the user gets an answer to their dilemma right away; and secondly, it’s positive, which means that the app does not blame the consumer for their choices and tries to leave options open. These two features distinguish the app from the other similar tools and websites out there.

<img src="https://raw.githubusercontent.com/Jeyana/EcoDilemmaAdvisor/main/images/blogpost/high_fidelity_welcome.png" height="700"/> <img src="https://raw.githubusercontent.com/Jeyana/EcoDilemmaAdvisor/main/images/blogpost/high_fidelity_food_category.png" height="700"/>

## Dinosavvy on a Mission

Starting with this idea, we set off on a journey. The Dinosavvy team of four combined the Data Science and UX Design tracks in equal proportions. However, in the middle of the project, we felt it made more sense to shift more weight to DS as UX was going well. From the very beginning, we limited the scope of the dilemmas to the food category and decided to go for quality instead of quantity in the research. Instant does not mean superficial: quite the opposite, it takes a lot of in-depth study of the subject to develop a concise and fact-driven answer. It became our main focus reflected both in the UX and DS tracks.

## UX Dilemmas

![Anna user story](https://raw.githubusercontent.com/Jeyana/EcoDilemmaAdvisor/main/images/blogpost/Anna_story_captions.png)

Having sketched our users and their stories in Figma (you can appreciate our exquisite drawing skills above), we had a few questions to answer. Does the user have to create an account to access the app? Should we praise the user for making an environmentally-friendly choice? Is it even possible to stay positive, taking into account the seriousness of the climate crisis? How is it possible to formulate a concise answer to a dilemma when all the answers actually start with “It all depends…”? How do we give users the possibility to verify the answers and access the data they are based on without overloading them with information? 

To answer these questions, we started testing early on with a lo-fi prototype. The first testing round already gave us a clear idea about our user's needs and helped correct navigation errors and add useful features. For example, three out of five testers requested a related dilemmas section: even when looking up one question, you want to keep scrolling.

![EcoDilemmaAdvisor low-fidelity prototype](https://raw.githubusercontent.com/Jeyana/EcoDilemmaAdvisor/main/images/blogpost/low_fidelity_browse_dilemmas.png)

The testing left us no doubt: in a world where you have to enter your details to buy a movie ticket, most users are exhausted by the endless stream of accounts they have to create. As one of our testers put it: "I want to see what an app has to offer before I leave any of my personal details." That is why we gave our users an option to skip personalization and proceed to ask questions straight away. Those who opt for personalization can add their habits to reflect their lifestyles and values. The idea for the future is to adjust answers based on the user's personality with the help of machine learning.

Upon selecting a dilemma, the user gets an instant answer with a short explanation and a 'Read More' button with expanding content. The latter includes more information on the subject, limitations, graphs, sources and tips. Our users loved it!

## Data Dilemmas

We started by defining a few dilemmas and diving into the [Eurostat](https://ec.europa.eu/eurostat/web/climate-change/data/database) databases to find the answers. For example, we tried to answer a question on the sustainability of washable plastic containers based on the recycling rate of packaging waste by the type of packaging, but with little success. Every eco dilemma requires analysis of dozens and dozens of data sources, and an answer based on just one dataset will hardly ever be complete.

We discovered that the most suitable methodology here is Life Cycle Assessment (LCA), which means that the environmental impact of every single stage of a product life cycle is calculated: from manufacturing to recycling. Because of the complexity of these calculations, researchers and consultants use LCA-databases, such as [Ecoinvent](https://ecoinvent.org/the-ecoinvent-database/) or [Agri-footprint](https://tools.blonkconsultants.nl/tool/21/). However, since these databases are not open-source, we could not work with them directly.

We focused on what *individuals* can do to reduce their footprint. We questioned commonly given advice and dived deep into various aspects of everyday consumer decisions. In many cases, we ended up reading existing studies and meta-analyses, translating the findings into simple and friendly language, and visualizing already condensed numerical data. In addition to that, we came back to the raw data from Eurostat, which is, luckily, available for free. 

## Tools

### Communication and Collaboration

We had a live online meeting every week (30-60 minutes) and communicated via a Slack group channel between meetings. To collaborate throughout the project, the programmers used Git, and the designers used Figma. We highly recommend both Git and Figma. Git can be intimidating for a beginner, but you definitely need it if you have more than one programmer on the team.

### UI/UX Design

![EcoDilemmaAdvisor high-fidelity prototype, Dilemma screens](https://raw.githubusercontent.com/Jeyana/EcoDilemmaAdvisor/main/images/blogpost/high_fidelity_questions.png)

We used Figma for the entire design process, which was great for a remote team like us. It's cloud-based, just like Google Docs. This means that it's always live and up to date and that designers and developers can work on the same file, making communication very smooth.

Figma is intuitive enough so that a beginner wouldn't feel intimidated (there are tons of [tutorials](https://www.youtube.com/c/Figmadesign) on Youtube, both official and non-official). Still, it can also be very advanced with all the prototyping features. We're still on the journey of exploring the possibilities, and it seems there's a long way to go. It's been great to learn how easy it is to create and edit the design system with components, and how plugins (Better font Picker, Iconify, Unsplash to name a few) make the workflow much quicker. 

### Data Science 

Most of the code for EcoDilemmaAdvisor was written in **Python**. Python might seem weird at first for someone transferring from another programming language, but it soon wins you over with its conciseness and elegance. It's a great language for beginners because it reads almost like English if the code is written with care.

**PyCharm** was the IDE we chose to use (the free Community version was enough). Packages and environments were managed by **Conda**.

Before coming up with a concrete answer to an eco-related question, we explored the data and tried out different visualizations in **Jupyter Notebooks**. This tool allows having formatted text + an unlimited number of code cells and their output all in one place, in an organized and readable way. For someone who already can write Python code, getting used to Jupyter takes only a couple of hours, and if you want to try it out without bothering to install it first, there is Google Colab, which is very much like Jupyter but runs in the cloud.

All graphs in EcoDilemmaAdvisor are made using **Matplotlib**, a Python library which, despite being huge, is easy to get started with (using [this short tutorial](https://www.earthdatascience.org/courses/scientists-guide-to-plotting-data-in-python/plot-with-matplotlib/introduction-to-matplotlib-plots/), for example).

![Matplotlib bar plot from exploratory Jupyter Notebook](https://raw.githubusercontent.com/Jeyana/EcoDilemmaAdvisor/main/images/blogpost/recycling_plastic_EU_2019_whiteBG.png)

Matplotlib is integrated with **Pandas**, another python library with a handy DataFrame type. The latter looks very much like an Excel table and supports (almost) all imaginable operations on data. With Pandas, importing a .csv into your code is as simple as:

~~~
recycling_rate = pandas.read_csv('recycling_rate.csv')
~~~

In order to make the calculations run faster, instead of native Python data structures (list, dictionary, set, tuple) Pandas uses ndarray type from **NumPy** library. The bigger the datasets you're using, the more important speed becomes, so NumPy is also a must-know for a data scientist. In our case, the learning order was Python basics -> Matplotlib -> Pandas -> Numpy, and it worked fine.

### Software Development

<img src="https://raw.githubusercontent.com/Jeyana/EcoDilemmaAdvisor/main/images/blogpost/app_screenshot.png" alt="App screenshot" width="300"/>

We used **Kivy** and **KivyMD** frameworks to develop the graphical user interface (GUI) for Android and iOS. Kivy is an open-source Python framework for developing mobile apps and other multitouch application software with a natural user interface (NUI). To create a more attractive GUI, KivyMD was used. KivyMD applies the concept of Material Design ([developed by Google](https://material.io/design/introduction)) to provide widgets that can be used with Kivy. KivyMD framework is similar to Kivy but has a more attractive GUI. In short, you can say that KivyMD depends on Kivy.

Operating with Kivy or KivyMD is relatively straightforward, and we recommend using it for developing simple mobile applications in Python. There's a wide variety of buttons and icons to choose from. To add an icon, you can [search for possible icons](https://materialdesignicons.com/); then you can copy the icon identifier and include it in your Python code. 

## Results

The research we've done for this project influenced our habits. We didn't all become vegans, and none of us went off to lead a carbon-neutral life in a cave. However, we discovered that less radical actions could make a significant difference.

For example:
1. If you choose poultry and pork instead of beef, the impact of the meat you eat becomes at least three times lower.
2. It's enough to wash a reusable plastic container 15 times (two weeks of using the same lunchbox) to compensate for high manufacturing impact (compared to single-use plastics). And even if that container is not recycled at the end of use, one worn reusable container in a landfill is much better than a pile of styrofoam shells.
3. In the EU, households throw away more fruit and vegetables than manufacturers and restaurants combined. So if you eat most of the food you bought before it gets spoiled, it really helps. You "save" not only the food itself but all the resources spent in producing and transporting it.

Don't just take our word for it, check out the [Q&A Jupyters](https://github.com/Jeyana/EcoDilemmaAdvisor/tree/main/jupyter) in the "jupyter" folder in [our github repo](https://github.com/Jeyana/EcoDilemmaAdvisor). We cited the sources diligently and provided graphical representation of the data for most questions.

Low- and high-fidelity prototypes of the app are in [this Figma file](https://www.figma.com/file/9gizYNqChzTnGfj9fJ7akE/EcoDilemmaAdvisor-APP?node-id=0%3A1). EcoDilemmaAdvisor's laconic, intuitive and beautiful interface (see high-fidelity) is waiting to be fully implemented.

The entry point of Kyvy MD proof-of-concept app is [frontend/main.py](https://github.com/Jeyana/EcoDilemmaAdvisor/tree/main/frontend). There is an environment.yml file in the repository root folder. It's created with Conda and contains all the requirements for running the app and the Jupyter Notebooks.

## Conclusion

None of the team members had experience as a frontend developer, so we didn't manage to create a perfect mobile app in two months, but we put together a decent proof of concept.

We did not expect the eco dilemmas to be that complicated and tough to answer. Looking for answers is very interesting, though, and we encourage everyone to do it — it might be depressing sometimes, but it gives you plenty of dinner table conversation topics. There are a lot of good sources online to satisfy your curiosity: [Milieucentraal](http://www.milieucentraal.nl) (in Dutch), [Climate change food calculator](https://www.bbc.com/news/science-environment-46459714), or this [book](https://g.co/kgs/fHrmMp) on the carbon footprint of everything, to name a few. 

We strongly believe the EcoDilemmaAdvisor app would be a valuable addition to every smartphone as the environmental crisis is everyone's problem, and this app is a tool to find solutions. The next steps in developing this project would include defining and researching dilemmas for other categories such as household and transport and incorporating machine learning into the app. Hopefully, this app will have a future.

Everyone here in the Dinosavvy team enjoyed the collaboration process a lot. We worked on the project from the Netherlands, Ukraine, Brazil and Argentina; in the middle of moving houses and driving through Patagonia. Thank you, TechLabs! It was a great adventure! 