# HackDavis x AISC Weekend Workshop!

### Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)
- [Backend with Flask](#backend-with-flask)
- [Frontend with NextJS](#frontend-with-nextjs)

# Introduction

Welcome to this HackDavis x AISC Weekend workshop! Today we'll create a full-stack web application, displaying your favorite ML/AI projects! (Don't forget to tag us if you do :3 @hackdavis @aisc)

### Live Demo

You can see a live demo of our website right here!~

### Tools and Frameworks Used

- Frontend: NextJS (Below 13)
- Backend: Flask
- Version Control: Git

# Setup

## GitHub Account
If you do not alredy have a GitHub Account, click on the Sign Up button on the top-right corner of this page and create one :>

## Installations
#### VSCode
Visual Studio Code (or VSCode) is a code editor that combines the processes of editing, building, testing and packaging an application.

1. Download the VSCode installer for your OS from https://code.visualstudio.com/download. 
2. Run the installer and follow the installation wizard.

#### GitHub Desktop
Git is a version control system (i.e. it helps you track the changes you have made to your code over time) and GitHub is a platform that helps you manage Git repositories and collaborate on projects.

1. Download GitHub Desktop for your OS from https://desktop.github.com/. Run the installer and follow the installation wizard.
2. Open GitHub Desktop.
Click on **File > Options... > Accounts pane > Sign in to your GitHub.com account**. When prompted, click on continue with browser and sign in.
3. After GitHub authenticates your account, you can start using GitHub Desktop.

#### Node.js 
Node.js is a runtime environment that is used to run Javascript code and is need for frameworks like Next.js. It comes with the Node Package Manager (npm) that helps us manage the Javascript packages used in our project.

1. Download the Node.js installer for your OS from https://nodejs.org/en/download/current. Run the installer and follow the installation wizard.
2. Open VSCode to see the welcome page. Press ``` Ctrl+` ``` on Windows or ``` Command+` ``` on Mac to open the Terminal within VSCode. Run the commands ``` node --version ``` and ```npm --v``` to verify installations.

3. Troubleshooting:

    a.  If you get the error **node or npm is not recognized as a command**, try restarting VSCode.

    b. If the problem persists, search for Environment variables in your Start menu. Click on **Edit your Environment variables > Environment Variables**. Select the variable **Path** from the list and click on Edit.

    c. Check for **C:\Program Files\nodejs\\** in the list of paths that appear. If it's not there, click on New and add it to the list. Restart VSCode and it should work now.

## Repository
To use git's version control, let's create and set up our repo :>

### Creating a new repository
1. Your GitHub Profile > Repositories tab > **New** button.
2. Provide a name for your repo. Select between Public or Private visibility,  check **Add a README file** and create repository.

### Cloning a repository
1. On your repo's page, click on the green Code button > **Open with GitHub Desktop**.
2. In GitHub Desktop, choose the location for the clone. 
3. **Open in Visual Studio Code** in the area to the right. 

### Creating the directory structure
Full stack applications have two major parts- frontend and backend- that are commonly set up separately in a project repository. 

Open a Terminal in your VSCode (Make sure the path in Terminal is at the root of your repo!) Create directories for frontend (Next.js) and server (Flask):

```bash
mkdir frontend
mkdir server
```

### Git commands cheatsheet
These are commonly used CLI git commands. Today, we'll demo these using GitHub Desktop instead :>

cheatsheet: https://education.github.com/git-cheat-sheet-education.pdf

# Backend with Flask

## Init Python Virtual Environment
[Some devices use **pip** while others use **pip3**. run ```pip --version``` or ```pip3 --version``` on a terminal to check which version you've got]

Run these commands to set up your python virtual environment with necessary dependencies:
```bash
cd server
python -m venv venv
# Windows users:
.\venv\Scripts\activate
# Mac/Linux users:
source venv/bin/activate
pip install -r requirements.txt
```

Add ```server/venv``` at the end of your .gitignore file in the project root.

To start your python server, run
```
python server.py 
```
(inside the server directory!) on the terminal and follow the local host link it generates.

## Context
```
server/
└── eda.py
└── main.py
└── models.py
└── plot.py
└── server.py
```
- *eda.py* : exploratory data analysis code for the breast cancer dataset.

- *main.py, models.py and plot.py* : Code from <a href="https://colab.research.google.com/drive/1D9n5qeIeSIAs1vAuYnI640nvLR1QZBW1" target="_blank">AISC's Weekend Workshop 2</a> organized in multiple files.

- *server.py* : file defining the api routes and the responses for those api calls.

# Frontend with NextJS

## Init NextJS

Documentation of NextJS can be found here: <a href="https://nextjs.org/docs" target = "_blank"> NextJS Documentation </a>
We will be using NextJS 12 and below which utilizes **Pages Router**.

Navigate to the top left and Make sure to set the documentation to <font color="Red"> Pages Router Settings! </font>

Now,
going into your newly made repository's frontend directory

```bash
cd frontend
```

Create a new nextJS project straight from their starting documentation by running:

```bash
npx create-next-app@latest . --use-npm --example "https://github.com/vercel/next-learn/tree/main/basics/learn-starter"
```

Start the server:

```bash
npm run dev
```

and boom! Your new nextJS project can now be seen in <a href="http://localhost:3000" target = "_blank"> http://localhost:3000 </a>

NextJS is a full-stack project. <font color="Pink"> Although there is much to cover about the specifics of the projects, we will just be focusing on frontend and how we can deploy so that we can start displaying our favorite ML Projects on your **resume!** </font>

## Routing

NextJS's Pages Router is a file-system based router built on the concept of pages. This means that the structure of the project affects how we can navigate within routes, call APIs, etc.

Assume that we have the following

```
pages/
├── index.js               # Accessed using the '/' route
├── about.js               # Accessed using the '/about' route
└── hackdavis/
    └── index.js           # Accessed using the '/hackdavis' route
    └── about.js           # Accessed using the '/hackdavis/about' route
```

Directories with `_` as prefixes will not produce a route in the app. This means directories such as

```
pages/
└── hackdavis/
    └── index.js
    └── _components/ #This will not be shown as a route
                      (it cannot be accessed via '/hackdavis/_components)

```

This component directory can be used to store reusable parts and to keep our code in _index.js_ look clean.

## Styling

We are going to be using SCSS, an extension of the normal CSS files but with just more SASS :3.

So go ahead and install SCSS:

```bash
npm install sass
```

Navigate to the _styles_ directory in the file explorer:

```
styles/
└── global.scss
└── Home.module.scss
```

- _global.scss_ is used for global styling. Think fonts, title, background color etc.
- _Home.module.scss_ is what we are going to be styling today. This will be imported to our _index.js_ for styling.

## Index.js and Home.module.scss

Due to our limited time, a copy of our HTML and SCSS code will be provided in this repo. Just navigate to our _index.js_ and _Home.module.scss_ to take a look!

# Deploying
- Create a vercel account
- Import the git repository 
- Click Deploy
- Deployment Protection Settings Off 
