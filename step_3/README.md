# Learning Flask - v0.12.1
I'm learning [Flask](http://flask.pocoo.org)!

I will create this flask app with macOS. All the steps in this tutorial will assume someone is starting with a fresh install of macOS.

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
