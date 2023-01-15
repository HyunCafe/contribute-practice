# <p align="center"> <img width="80" src="assests/flamey.gif" alt="flamey from studio ghilbi" /> First time Practice Contributions! <img width="80" src="assests/flamey.gif" alt="flamey from studio ghilbi" />
</p>

<p align="center">
<img align="center" width="700" src="assests/Coffee.gif" alt="hot coffee" />
</p>

## Introduction
Welcome to our beginner-friendly GitHub repository for practicing making contributions!

This repo is designed for first-time contributors to get familiar with the process 
of forking a repo, cloning it to their local machine, making changes, 
and submitting a pull request. 

We've included some simple tasks for you to complete, 
along with step-by-step instructions on how to submit your changes.

Whether you're new to programming or just new to open source contributions, 
this is the perfect place to get started.
So, fork the repo, clone it, and let's get started! <br>

## Objectives
* Provide an introduction and overview of the repository for first-time contributors
* Explain the process of forking a repo, cloning it to a local machine, making changes and submitting a pull request
* Include simple tasks for contributors to complete with step-by-step instructions on how to submit changes
* Explain that the repository is suitable for both new programmers and those new to open source contributions
* Encourage contributors to fork and clone the repo and get started with making contributions. <br><br><br>

<img width="500" src="assests/studiogif.gif" alt="cute lazy cat gif chasing butterfly" />

## Fork this repo 
<br><h2> Step 1 </h2>
<img align="right" width="400" src="assests/forkrepo.JPG" alt="step 1 fork this repo drown down button" /> <br>

* Click on the "Fork" drop down button located in the top right corner of the page.

* Click on the "+ Create a new fork* <br><br><br>

<h2> Step 2 </h2>
<img align="right" width="550" src="assests/createforkrepo.JPG" alt="step 2 fork this repository addition" /> <br>

* Click on "Create fork" <br><br>

* Once the repository has been forked, you will be taken to the forked repository's page. <br><br>

* This will be a copy of the original repository, but it will be under your account. <br><br><br><br><br><br><br><br>

## Clone this repo
<img align="right" width="400" src="assests/clonestep1.JPG" alt="step 1 click code then ssh then copy" /> <br>
* First, lets click on the "Code" drop down button, click on "SSH" then click the "Copy Icon" <br>

* Then, let's go to our local machine, open the terminal, and create a new directory to put our newly cloned repo in and name it "contribute-practice" 
```
mkdir contribute-practice
```
* and cd into the directory
```
cd contribute-practice
```
* Clone the forked repository to your local machine by typing git clone followed by the SSH link that you copied.
```
git clone copyoftheurlssh
```
<br><br>
## Create a branch
* Now let's create a new branch through the terminal using the git switch _BranchName_. 

Replace _BranchName_ with the name of the new branch you want to create. 

For example:
```
git switch -c HyunCafe
```
<br><br>
## Contribution time!
* Open the contributing.md file, you can use a text editor of your choice, for example, nano contributing.md or vi contributing.md
I personally use vs code, so I would type:
```
code .
```

*  Follow the directions under the contributing.md and now lets commit your changes!

*  Remember the order for git best practices! <br>
git status >> git add (files changed) >> git commit -m "insert short description of changes made" >> git push

type:
```
git status
```
now you can see the files that were changed, now add them
```
git add (files changed)
```
now lets commit our changes with a short description
```
git commit -m "Add: Added my name to list, My first contribution!"
```
Push the changes to your forked repository on GitHub using the command git push origin <branch-name>, where <branch-name> is the name of the branch you are working on.
```
git push -u origin your-branch-name
```
<br><br>
## Making a Pull Request
<h2> Step 1 </h2>
<img align="right" width="400" src="assests/prstep1.JPG" alt="step 1 Pull request" /> <br><br><br><br><br>

* Go to your forked repository on GitHub, click on "contibute" drowp down click on "Open pull request"<br><br><br>


<br><br><h2> Step 2 </h2>
<img align="right" width="400" src="assests/prstep2.JPG" alt="step 2 Pull request" /> <br>

* Fill in the title and description of the pull request, to explain the changes you made and why they should be merged with the main branch of the original repository.

* Once you have filled out the details, click the "Create pull request" button to submit your pull request for review. <br><br><br><br><br><br>


## Great job! All done! Wasn't so bad was it?

<p align="center"><br>
<img width="700" align="center" src="assests/totoro.gif" alt="cute studio ghilbi gif" />
  </p> <br>

* Great job! You've just successfully completed the usual fork -> clone -> make changes -> pull request workflow, which is commonly used by contributors. Keep it up and keep contributing!

* I will get around to merging the request when I can, I am usually good about it!
