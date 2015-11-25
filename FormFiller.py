'''This program parses game template files and writes a variety of useful documents
'''

from glob import glob
import math
import os
import random
import re
import shutil
import string
import sys


# Define some constants
TEMPLATE_DIR = 'templates'
OUTPUT_DIR = 'output'
GAF_TEMPLATE = TEMPLATE_DIR + '/GafTemplate'
DF_TEMPLATE = 'DF-new-df.properties'
SITE_COPY_FILE = OUTPUT_DIR + '/SiteCopy.txt'
OL_PROPERTIES_TEMPLATE = 'ONLINE.properties'
DL_PROPERTIES_TEMPLATE = 'DOWNLOAD.properties'
ARMADILLO_LINE = '-19,{email},XXXXXXXX-XXXXXXXX-XXXXXXXX-XXXXXXXX,0,0'
SK_INFO_FILE = OUTPUT_DIR + '/ShopkeeperInfo.txt'
DOWNLOAD_CDN_BASE_URL = 'http://downloadcdn.shockwave.com'
DOWNLOAD_FULL_PATH = DOWNLOAD_CDN_BASE_URL + '/pub/KEYWORD/INSTALLER_NAME'
DOWNLOAD_SERVER = 'pusher.west.mtvi.com'


# Create the Game class
class Game:
    def __init__(self):
        self.keyword = 'XXX'
        self.sku = 'XXX'
        self.installer_name = 'XXX'
        self.price = 'XXX'
        self.product_name = 'XXX'
        self.product_safe_name = 'XXX'
        self.primary_category = 'XXX'
        self.secondary_category = ''
        self.friendly_download_URL = 'XXX'
        self.detailed_download_URL = 'XXX'
        self.large_image_URL = '/i/picons/KEYWORD_small.jpg'
        self.email_template_subject = 'Your GAME download and license key from Shockwave'
        self.rnum = 'XXX'
        self.release_date = 'XXX'
        self.type = 'XXX'
        self.short_title = ''
        self.short_synopsis = ''
        self.full_synopsis = ''
        self.min_sys_reqs = ''
        self.credits = ''
        self.search_words = ''
        self.instructions = ''
        self.seo_title = ''
        self.meta_description = ''
        self.meta_keywords = ''

    def writeSKinfo(self, output_file):
        # Writes the Shopkeeper info for each game to output_file
        with open(output_file, 'a') as f:
            f.write(self.sku + '\n')
            f.write(self.product_name + '\n')
            f.write(self.price + '\n')
            f.write(self.primary_category + '\n')
            f.write(self.friendly_download_URL + '\n')
            f.write(self.detailed_download_URL + '\n')
            f.write(self.short_synopsis + '\n')
            f.write(self.full_synopsis + '\n')
            f.write(self.large_image_URL + '\n')
            f.write('*** CHANGE PRODUCT SUBTYPE TO "shockwave" ***\n')
            f.write(self.keyword + '\n')
            f.write(self.email_template_subject + '\n')
            f.write(self.product_safe_name + '\n')
            f.write(ARMADILLO_LINE + '\n')
            f.write('\n\n')

    def writeSiteCopyTemplate(self, output_file):
        with open(output_file, 'a') as f:
            f.write(self.type.upper() + "\n\n")
            f.write("Keyword: " + self.keyword + "\n\n")
            f.write("Title: " + self.product_name + "\n\n")
            f.write("Short Title: " + self.product_name + "\n\n")
            f.write("Short Synopsis: \n\n")
            f.write("Medium Synopsis: \n\n")
            f.write("Synopsis: \n\n")
            if self.type == 'download':
                f.write("System Reqs: Windows XP/Vista/7/8<br>1.0 GHz processor<br>2 GB RAM" +
                        "<br>DirectX 9.0c<br>256 MB video RAM<br>200 MB free disk space<br>\n\n")
            elif self.type == 'online':
                f.write("System Reqs: Windows 2000/XP/Vista/7<br>Macintosh OS X<br>" +
                        "800 MHz processor<br>1 GB RAM<br>Flash Player<br>128 MB video RAM<br>\n\n")
            f.write("Credits: \n\n")
            f.write("Search words: " + self.product_name + ", " + self.primary_category.lower() +
                    ", " + self.type.lower() + " games, " + self.type.lower() + "\n\n")
            f.write("Instructions: See in-game help for detailed instructions.<br><br>\n\n")
            f.write("SEO Title (70 max): " + self.product_name + " - " +
                    string.capwords(self.primary_category) + " games on Shockwave.com\n\n")
            f.write("metaDescription (160 max): " + self.product_name +
                    "; [SHORT SYNOPSIS] Play more " + self.primary_category.lower() +
                    " games at Shockwave.com\n\n")
            f.write("metaKeywords: " + self.product_name + ", " +
                    string.capwords(self.primary_category) + " Games\n\n")
            f.write("upsellCopy: \n\n")
            f.write(("-" * 20) + "\n\n") 

# End Game class definition


# Define several functions
def random_armadillo_nums():
    """Returns a list of numbers suitable for use in a game's gaf config file"""
    
    return (str(int(99999999 - math.floor(random.random()*89999999))) + "-" +
            str(int(99999999 - math.floor(random.random()*89999999))) + "-" +
            str(int(99999999 - math.floor(random.random()*89999999))) + "-" +
            str(int(99999999 - math.floor(random.random()*89999999))))


def get_game_info():
    """Parses files and returns a list of Game objects"""

    # Create a list to hold all of the game objects to be created
    game_objects = []

    # Open relevant files, read contents into a list of key/value pairs
    for textfile in os.listdir(os.getcwd()):
        if textfile.endswith('txt') and textfile.lower() != 'readme.txt':
            game = Game()
            with open(textfile, 'r') as f:
                for line in f:
                    line_contents = line.split('=')
                    
                    # Remove leading and trailing white space
                    for x in range(len(line_contents)):
                        line_contents[x] = line_contents[x].strip()

                    # Fill in values for the Game object
                    if line_contents[0] == 'keyword':
                        game.keyword = line_contents[1]

                    if line_contents[0] == 'Installer Name':
                        game.installer_name = line_contents[1]

                    if line_contents[0] == 'Price':
                        game.price = line_contents[1]

                    if line_contents[0] == 'Product Name':
                        game.product_name = line_contents[1]

                    if line_contents[0] == 'Product Safe Name':
                        game.product_safe_name = line_contents[1]

                    if line_contents[0] == 'Short Title':
                        game.short_title = line_contents[1]

                    if line_contents[0] == 'Primary Category':
                        game.primary_category = line_contents[1]

                    if line_contents[0] == 'Secondary Category':
                        game.secondary_category = line_contents[1]

                    if line_contents[0] == 'rnum':
                        game.rnum = line_contents[1]

                    if line_contents[0] == 'Release Date':
                        game.release_date = line_contents[1]

                    if line_contents[0] == 'Game Type':
                        game.type = line_contents[1].lower()

                    if line_contents[0] == 'Short Synopsis':
                        game.short_synopsis = line_contents[1]

                    if line_contents[0] == 'Synopsis':
                        game.full_synopsis = line_contents[1]

                    if line_contents[0] == 'Credits':
                        game.credits = line_contents[1]

                    if line_contents[0] == 'Instructions':
                        game.instructions = line_contents[1]

                    if line_contents[0] == 'System Reqs':
                        game.min_sys_reqs = line_contents[1]

            game.sku = game.keyword + '-pc'
            game.search_words = '{0}, {1}, {2} games, {2}'.format(game.product_name, game.primary_category.lower(), game.type)
            game.meta_description = '{0}; {1} Play more {2} games at Shockwave.com'.format(game.product_name, game.short_synopsis, game.primary_category.lower())

            # Various string parsing below to get each value exactly as we want it

            game.product_name = game.product_name.replace('\x99', '&#8482;')      # Replace (TM) character with html entity
            game.product_name = game.product_name.replace('\xAE', '&#174;')       # Replace (R) character with html entity

            game.email_template_subject = game.email_template_subject.replace('GAME', game.product_name)
            game.email_template_subject = game.email_template_subject.replace('&#8482;', '(TM)')    # Replace html entity with (TM)
            game.email_template_subject = game.email_template_subject.replace('&#174;', '(R)')      # Replace html entity with (R)
            game.email_template_subject = game.email_template_subject.replace('&#169;', '(C)')      # Replace html entity with (C)

            game.large_image_URL = game.large_image_URL.replace('KEYWORD', game.keyword)    # create large image url

            game.friendly_download_URL = DOWNLOAD_FULL_PATH.replace('KEYWORD', game.keyword)
            game.friendly_download_URL = game.friendly_download_URL.replace('INSTALLER_NAME', game.installer_name)

            game.detailed_download_URL = game.friendly_download_URL.replace(DOWNLOAD_CDN_BASE_URL, '')

            # Append Game object to the list of games
            game_objects.append(game)
            
    return game_objects


def create_gaf_folder(game):
    """Copy and fill gaf files - takes a single game object as an argument"""

    # Create the folder name for each game's folder, parsing safe name as necessary

    if game.type != 'download': # only do this for download games
        return
    
    folder_name = string.capwords(game.product_safe_name)

    # Remove the following characters: space, -, ', .
    translator_map = str.maketrans({" ": None,
                                    "'": None,
                                    "-": None,
                                    ".": None})
    
    folder_name = folder_name.translate(translator_map)
	
    if folder_name.startswith(('A ')):
        folder_name = folder_name[2:]

    if folder_name.startswith(('The', 'the')):
        folder_name = folder_name[3:]

    # Copy and rename gaf template folders
    try:
        shutil.copytree(GAF_TEMPLATE, OUTPUT_DIR + '/' + folder_name)
        os.rename(OUTPUT_DIR + '/' + folder_name + '/gaf.KEYWORD-pc.shockwave.com.32.en-us.config',
                  OUTPUT_DIR + '/' + folder_name + '/gaf.' + game.keyword + '-pc.shockwave.com.32.en-us.config')
    except WindowsError:
        print('Windows Error')
        pass

    # Fill out each game's gaf config file
    start_dir = os.getcwd() + '/' + OUTPUT_DIR
    for folder in os.listdir(start_dir):
        if os.path.isdir(start_dir + '/' + folder):
            folder_path = start_dir + '/' + folder
            try:
                gaf_file = glob(folder_path + '/*config')
                if os.path.basename(gaf_file[0]).startswith('gaf.' + game.keyword + '-pc'):
                    with open(gaf_file[0], 'r') as f:
                        gaf_contents = f.readlines()
                    with open(gaf_file[0], 'w') as f:
                        for entry in gaf_contents:
                            if entry.startswith('$(SKU)=XXX'):
                                entry = entry.replace('XXX', game.keyword + '-pc')
                            elif entry.startswith('$(PRODUCT_NAME)=XXX'):
                                entry = entry.replace('XXX', game.product_name)
                            elif entry.startswith('$(PRODUCT_SAFE_NAME)=XXX'):
                                entry = entry.replace('XXX', game.product_safe_name)
                            elif entry.startswith('$(GATEKEEPER_ENCRYPTION_TEMPLATE_OWNER)=XXX'):
                                entry = entry.replace('XXX', random_armadillo_nums())
                            elif entry.startswith('$(GATEKEEPER_ENCRYPTION_TEMPLATE_SUBSCRIBER)=XXX'):
                                entry = entry.replace('XXX', random_armadillo_nums())
                            elif entry.startswith('$(ARMADILLO_ENCRYPTION_PROJECT_ID)=XXX'):
                                entry = entry.replace('XXX', random_armadillo_nums())
                            f.write(entry)

            except IndexError:
                pass

    
def create_df_property_sheet(game):
    """Creates the DF property sheet for a game, takes a single game object as an argument"""
    
    df_property_sheet = OUTPUT_DIR + '/' + game.keyword + '-new-df.properties'
    shutil.copy(TEMPLATE_DIR + '/' + DF_TEMPLATE, df_property_sheet)
    with open(df_property_sheet, 'r') as f:
        file_contents = f.readlines()
    with open(df_property_sheet, 'w') as f:
        for line in file_contents:
            line = line.replace('KEYWORD1', game.keyword)
            f.write(line)


def create_game_property_sheet(game):
    """Creates the regular property sheet for a game, takes a single game object as an argument"""
    
    property_sheet = OUTPUT_DIR + '/' + game.keyword + '.properties'
    if game.type == 'download':
        shutil.copy(TEMPLATE_DIR + '/' + DL_PROPERTIES_TEMPLATE, property_sheet)
    else:
        shutil.copy(TEMPLATE_DIR + '/' + OL_PROPERTIES_TEMPLATE, property_sheet)

    with open(property_sheet, 'r') as f:
        file_contents = f.readlines()
    with open(property_sheet, 'w') as f:
        for line in file_contents:
            line = line.replace('DATE1', game.release_date)
            line = line.replace('KEYWORD1', game.keyword)
            line = line.replace('GENRE1', game.primary_category)
            line = line.replace('GENRE2', game.secondary_category)
            line = line.replace('FULL_TITLE1', game.product_name)
            line = line.replace('SHORT_TITLE1', game.short_title)
            line = line.replace('SHORT_SYNOPSIS1', game.short_synopsis)
            line = line.replace('FULL_SYNOPSIS1', game.full_synopsis)
            line = line.replace('MSR1', game.min_sys_reqs)
            line = line.replace('CREDITS1', game.credits)
            line = line.replace('INSTRUCTIONS1', game.instructions)
            line = line.replace('SEARCH_WORDS1', game.search_words)
            line = line.replace('META_DESCRIPTION1', game.meta_description)
            f.write(line)


def create_upload_script(game_list, script):
    """Creates the script used by WinSCP to upload new games to the server"""
    
    path = '/www/www-d/docs/batman.shockwave.com/download.shockwave.com/www/htdocs/pub/'
    with open(script, 'w') as f:
        f.write("option batch on\n" +
                "option confirm off\n" +
                "option transfer binary\n\n" +
                "open " + DOWNLOAD_SERVER + " -rawsettings SendBuf=0\n\n")

        for game in game_list:
            if game.type == 'download':
                f.write("mkdir " + path + game.keyword + "\n" +
                        "put " + game.installer_name + " " + path + game.keyword + "/" + game.installer_name + "\n\n")

        f.write("exit\n")

    with open(OUTPUT_DIR + "/RunWinSCPscript.bat", 'w') as f:
        f.write("WinSCP.exe /script=" + os.path.basename(script) + " /console")

        
def main():
    """Creates all necessary files for games which have (somewhat) completed templates in the root folder"""

    # Create output directory if it doesn't already exist
    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    # Delete SK Info file if it already exists
    if os.path.exists(SK_INFO_FILE):
        os.remove(SK_INFO_FILE)

    if os.path.exists(SITE_COPY_FILE):
        os.remove(SITE_COPY_FILE)

    # Read all template sheets to get info for each game
    game_info = get_game_info()

    # Write Shopkeeper info for all download games
    for game in game_info:
        if game.type == 'download':
            game.writeSKinfo(SK_INFO_FILE)

    for game in game_info:
        create_df_property_sheet(game)      # create dynamic feature property sheets for all games
        create_game_property_sheet(game)    # create game property sheets for all games
        create_gaf_folder(game)             # create and fill out gaf folder for all download games

        # DEPRECATED, we no longer need the SiteCopyTemplate now that we write all info to each game's property sheet
        # game.writeSiteCopyTemplate(SITE_COPY_FILE)      # create and partially fill out the site copy template
    
    # DEPRECATED, THIS WAS USED WITH THE VIACOM UPLOAD PROCESS
    # create_upload_script(game_info, OUTPUT_DIR + "/winscp_upload_script.txt")   # write script and .bat file used to upload DL games to server

  
if __name__ == '__main__':
    main()

