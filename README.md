# Learning Flask - v0.12.1
I'm learning [Flask](http://flask.pocoo.org)!

I will create this flask app with macOS. All the steps in this tutorial will assume someone is starting with a fresh install of macOS.

## Step 0: What This Is

Let me explain my philosophy behind what this is and why I'm doing it. First, this is **not** a full-fledged tutorial for using Flask. It is more like a breadcrumb trail for me to retrace my steps while I am learning Flask. I am searching the internet and looking for help in other tutorials, then creating working examples for me to test. As such, I'm not going into much detail in my steps and this tutorial won't build a deep understanding. The examples and code should be used like a playground for testing things.

So, if you want to read about Flask and learn that way, try some [other resources](https://www.fullstackpython.com/flask.html).

Here's how my examples can help you. I have multiple examples that can be easily run from a terminal. So you won't have to piece together code from other tutorials to see this work. Furthermore, the examples isolate some key concepts. You don't have to see the lines of code that verify sessions while learning about the database, for example. Just go right to the step with a concept you need to learn, run it, then look at the code to see how it fits together. And don't be afraid to tinker!

## Step 1: Installation

The first part of installation will cover installing Anaconda3 and creating a virtual environment to work from. This is completely optional and you can skip ahead to the 'Installing Flask' section.

### Step 1.1: Install Anaconda3 (Optional)

1. Navigate to the Anaconda [download](https://www.continuum.io/downloads) page.
2. Download the Python 3.6 version for macOS.
3. Run the following command from the Terminal app to install Anaconda3 ```bash ~/Downloads/Anaconda3-4.3.1-MacOSX-x86_64.sh```.
  - The file ```Anaconda3-4.3.1-MacOSX-x86_64.sh``` is the current file name; check your download file name before running this command.
4. Follow the prompts that show up in the terminal to continue installing.
5. After the installation script has exited, run the command ```conda list``` in the terminal to ensure it installed correctly. If you get an error, Anaconda3 did not install properly. Check the Anaconda website for more information.

### Step 1.2: Create a Virtual Environment (Optional)

Run the following command to create a virtual environment using Anaconda3:

```
conda create --name learning-flask python=3.6
```

Note that ```learning-flask``` could be any name you want it to be. To activate the environment, enter the following command:

```
source activate learning-flask
```

When you are finished using the virtual environment, simply enter ```source deactivate``` in the terminal.

### Step 1.3: Installing Flask

To install Flask, enter the following command in the Mac Terminal app:

```
pip install Flask
```

You can try running ```flask --version``` to ensure it installed correctly. Alternatively, a file named ```requirements.txt``` contains all of the dependencies needed for this tutorial. Simply type ```pip install -r requirements.txt``` to install flask and all of the other dependencies this tutorial uses.

## Step 2: Running Flask Example

Enter the following in Mac's Terminal app to run the flask example:

```
python routes.py
```

Then, navigate a browser window to [http://127.0.0.1:5000](http://127.0.0.1:5000) to see the result.

In this example ```routes.py``` is using the ```index()``` function to load the ```index.html``` example found in ```templates/index.html```. The CSS for this example is located in ```static/css/main.css```.

Next, we'll look at an example with multiple pages that reuse templates. Before we move on, let me explain how the rest of the examples will work. I've created separate folders for the rest of the steps that each represent their own Flask app. This allows me to compartmentalize the lessons as I learn to use Flask. Simply click the link to a step below, or change directories to the appropriate step and run the ```routes.py``` file the same way you did for this example. The ```README.md``` files within each folder will explain the new concepts.

## Other Steps

[Step 3: Pages and Templates](https://github.com/rsm5139/learning-flask/tree/master/step_3)

[Step 4: Database and Forms](https://github.com/rsm5139/learning-flask/tree/master/step_4)

[Step 5: Authentication and Sessions](https://github.com/rsm5139/learning-flask/tree/master/step_5)

*Coming Soon*

[Step 6: Reactive Design](https://github.com/rsm5139/learning-flask/tree/master/step_6)