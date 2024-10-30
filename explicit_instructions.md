These explicit instructions assume no coding experience and the macOS operating system.

The instructions allow you to run a script that given a collection of Spotify Streaming_History_Audio.json files will iterate through each song played for more than 20 seconds, remove unnecessary technical data and combine them into a `.csv` file that can be opened in Numbers or Excel.

1. Start by downloading the code repository where you are currently reading this. On Github, press the green `Code` button in the upper right portion of your frame and click `Download ZIP`. Place this zip folder on your desktop and extract the contents to a folder which will be named `customWrapped-main`.
2. Navigate to this folder in Finder and enter the `input` folder. Place the `Streaming_History_Audio_XXX.json` files from your Spotify export here.
3. Now, open your computer terminal by entering Spotlight and typing `terminal`. This should place you in your user folder. Validate this by entering the command `pwd` (print working directory), which should result in `/Users/your_username`.
4. Using the change directory command `cd`, navigate to your `customWrapped-main` folder by entering `cd Desktop/customWrapped-main` in the terminal. You can use the tab key to auto-complete long directory names by typing `cd Des` hitting the tab key.
5. Now we want to create a virtual environment to run our python code in. This prevents any installed python extensions from being available outside of this folder. Do this by entering the command `python3 -m venv venv` into the terminal, making sure you are in the `customWrapped-main` folder.
6. This should create a new directory called `venv`, which you can validate by entering the `ls` (list directory contents) command and confirming that there is a folder called `venv`.
7. To enter the virtual environment, enter the command `source venv/bin/activate`. This should make the text `(venv)` appear at the beginning of your terminal command prompt.
8. Now, we want to install the python extensions required to run the script. We do this by entering `pip3 install -r requirements.txt`, making sure we are in our virtual environment `venv` and in our `customWrapped-main` directory. This will install the `pandas` python library among a few others.
9. Assuming our library extensions were installed successfully, we are now able to run the program. Start the script by entering `python3 merge_and_filter_raw_data.py`. You can again auto-complete the script name by writing `python3 merge` and hitting the tab key.
10. This should hopefully yield the text `Successfully merged streaminig history and placed in output folder.`. You can now find your output spreadsheet file in the `output` directory and open it in Finder.
