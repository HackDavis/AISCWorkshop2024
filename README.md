# HackDavis x AISC Weekend Workshop!

## Table of Contents

- [Introduction](#introduction)
- [Live Demo](#live-demo)
- [Tools and Frameworks Used](#tools-and-frameworks-used)
- [Setup](#setup)
- [Credits](#credits)

### Introduction

Welcome to this HackDavis x AISC Weekend workshop! Today we are going to be creating a full-stack web application, displaying your favorite ML/AI projects! (Don't forget to tag us if you do :3 @hackdavis @aisc)

### Live Demo

You can see a live demo of our website right here!~

### Tools and Frameworks Used

- Frontend: NextJS (Below 13)
- Backend: Flask
- Version Control: Git

### Setup

#### Git Setup

- Create a new repository
- Copy the link
- mkdir in local
- Connect to Remote Git!
  (Very Rough, will need more edit)


#### Creating Folder Structure 
- once in the directory that is connected to git 
#### NextJS Init

Documentation of NextJS can be found here: <a href="https://nextjs.org/docs" target = "_blank"> NextJS Documentation </a>
We will be using NextJS 12 and below which utilizes **Pages Router**.

Navigate to the top left and Make sure to set the documentation to <font color="Red"> Pages Router Settings! </font>

Now,

- cd into your newly made repository that is connected to the remote git.
- run _npx create-next-app@latest nextjs-blog --use-npm --example "https://github.com/vercel/next-learn/tree/main/basics/learn-starter"_
  This will create a new nextJS project downloading straight from their starting documentation

- run _cd nextjs-blog_ to get into the nextjs-blog directory
- run _npm run dev_

and boom! Your new nextJS project can now be seen in <a href="http://localhost:3000" target = "_blank"> http://localhost:3000 </a>

#### Backend with Flask 
Side note: some devices use _pip_ others use _pip3_. You should check which version you have by 
- cd into server folder 
- run _pip3 install -r requirements.txt_ This will download all the necessary dependencies that our server might need!
- run _python3 server.py_ This will start the server running it on a different local host. 
#### Frontend with NextJS
- Install the necessary dependencies
  - npm install sass (for SCSS)
  - 

NextJS's is a file-system based router. This means that the file structure determines how our website navigation works.

**Structure:**
- pages/index.js -> /
- pages/hackdavis/index.js -> /hackdavis
- pages/



