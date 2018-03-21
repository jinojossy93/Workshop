# Jino's Workshop
Common place to host all my workshop contents

# Git
First you will have to install GIT 
Go to the cloudshell accessing this [URL](https://console.cloud.google.com/cloudshell/editor)

# Install Git
<code>
	$ sudo apt-get update
	$ sudo apt-get install git
</code>

# Verify the installation was successful by typing git --version:
<code>
	$ git --version
</code>
git version 2.9.2

# Git Setup
Configure your Git username and email using the following commands, replacing my name with your own. These details will be associated with any commits that you create:
<code>
	$ git config --global user.name "Jino Jossy"
	$ git config --global user.email "jinojossy93@gmail.com"
</code> 

Now the next step is cloning my repository to pull the code changes for the excercise:

# Clone this repository
<code>
	$ git clone https://github.com/jinojossy93/Workshop.git
</code>

Next step is going to the Excercise folder:

# Excercise 1

<code>
	$ cd Workshop/excercise_1/
</code>

# Development Server
Now you are in the first excercise. You can now run the development server by using the following command
<code>
	$ dev_appserver.py .
</code>

And this can be deployed to Internet by doing following commands

# Setting project. 
Replace PROJECT_ID with your ID.
<code>
	$ gcloud config set project PROJECT_ID
</code>

# Deploying project. 
Replace VERSION with the version you need it can be number or string or both combined.
<code>
	$ gcloud app deploy . --version=VERSION
</code>

# Excercise 2
Do the same as above. It's a guest book application where the guest input is being saved to Database.
<code>
	$ cd Workshop/excercise_1/
</code>

In Excercise 2 we are using Datastore as our database to store the user's input.

Find more details about Datastore [here](https://cloud.google.com/appengine/docs/standard/python/datastore/)
