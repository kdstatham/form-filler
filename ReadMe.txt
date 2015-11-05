Important - The 'FormFiller.py' script was written to run on Python 3.x.  It *might not* run on a Python 2.x release without modifications.

You may wish to change the necessary date fields in the 'GafTemplate' (folder name and in config file) before running 'FormFiller.py'.

STEP-BY-STEP INSTRUCTIONS

1. Copy the 'ProductionTemplate' folder to your computer.  It is advised but not necessary to rename it for the release you're working on.

2. For each game in the release:
		- Copy the 'templates/game_info_template.txt' file to its parent directory (the same folder which contains "FormFiller.py")
		- Rename the file to keyword.txt, where 'keyword' is the keyword for the game in question.
		- Fill out the file with the appropriate game information

3. Once you have a completed template file for each game in the release, double-click the "FormFiller.py" file to run it.

4. A folder named 'output' will be created in the same location as the "FormFiller.py" script.  Inside it you will find the following:
		- A completed properties sheet for each game, used for Rosebud.
		- A completed properties sheet for each dynamic feature, used for Rosebud.
		- A 'ShopkeeperInfo.txt' file, used to fill out each download game's game record in Shopkeeper.
		- A 'SiteCopy.txt' file.  This will be partially filled out for each game, but will require copy changes specific to each game.
		- Gaf folders for each download game, each with the appropriate folder structure and a completed config file.