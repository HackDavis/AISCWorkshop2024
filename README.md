# HackDavis x AISC Weekend Workshop!

### Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)
- [Backend with Flask](#backend-with-flask)
- [Frontend with NextJS](#frontend-with-nextjs)

# Introduction

Welcome to this HackDavis x AISC Weekend workshop! Today we are going to be creating a full-stack web application, displaying your favorite ML/AI projects! (Don't forget to tag us if you do :3 @hackdavis @aisc)

### Live Demo

You can see a live demo of our website right here!~

### Tools and Frameworks Used

- Frontend: NextJS (Below 13)
- Backend: Flask
- Version Control: Git

# Setup

### Git Setup

- Create a new repository
- Copy the link
- mkdir in local
- Connect to Remote Git!
  (Very Rough, will need more edit)

### Creating Directory Structure

Once in the directory that is connected to git, create a directory for frontend (this will be used with NextJS) and server(this will be used with flask)

```bash
mkdir frontend
mkdir server
```

# Backend with Flask

Side note: some devices use _pip_ others use _pip3_. You should check which version you have by

- cd into server directory
- run _pip3 install -r requirements.txt_ This will download all the necessary dependencies that our server might need!
- run _python3 server.py_ This will start the server running it on a different local host.



# Frontend with NextJS

### Init NextJS

Documentation of NextJS can be found here: <a href="https://nextjs.org/docs" target = "_blank"> NextJS Documentation </a>
We will be using NextJS 12 and below which utilizes **Pages Router**.

Navigate to the top left and Make sure to set the documentation to <font color="Red"> Pages Router Settings! </font>

Now,
Going into your newly made repository

```bash
cd <directory_name>
```

Create a new nextJS project straight from their starting documentation by running:

```bash
npx create-next-app@latest nextjs-blog --use-npm --example "https://github.com/vercel/next-learn/tree/main/basics/learn-starter"
```

Go into the _nextjs-blog_ directory and start the server!

```bash
cd nextjs-blog
npm run dev
```

and boom! Your new nextJS project can now be seen in <a href="http://localhost:3000" target = "_blank"> http://localhost:3000 </a>

## Context

NextJS's is a full-stack project. We are currently using **Pages Router** structure which is the version of NextJS Below 13. <font color="Pink"> Although there is much to cover about the specifics of the projects, we will just be focusing on frontend and how we can deploy so that we can start displaying our favorite ML Projects on your **resume!** </font>

### Routing 

- NextJS is a Pages Router is a file-system based router built on the concept of pages. This means that the structure of the project affects how we can navigate within routes, call APIs, etc.

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

This component directory can be used to store parts which is reusable but also so that our code in _index.js_ looks clean.

## Styling
We are going to be using SCSS, an extension of the normal css files but with just more SASS :3. 

So go ahead and install SCSS 
```bash 
npm install sass
```

Navigate to the _styles_ directory 
```
styles/
└── global.scss  
└── Home.module.scss  
```
- _global.scss_ is used for global styling, think fonts, title, background color etc.
- _Home.module.scss_ is what we are going to be styling today. This will be imported to our _index.js_ for styling.

## Index.js and Home.module.scss
Due to our limited time, a copy of our HTML and SCSS code will be provided in this repo. Just navigate to our _index.js_ and _Home.module.scss_ to take a look!






