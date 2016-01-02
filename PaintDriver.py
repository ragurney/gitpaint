import configparser
import logging
import os
import subprocess

Config = configparser.ConfigParser()
# configSections = ["Git Exe Options", "Dummy Repo Options"]

dummyFileName = 'dummyFile.txt'
batchFileName = 'dummyUpdateAndPush.bat'


batchFileCreated = False
gitLocation = ""
dummyRepoPath = ""
dummyFilePath = ""

# Bash Commands
#  TODO: Add more info (date, part of letter done), also, definitely change this string lol
batchFile = "cd {}\n" \
           "{} add -A dummyFile.txt\n" \
           "{} commit -m \"File Updated\"\n" \
           "{} push origin master\n" \
           "start chrome.exe\n"

vars = [gitLocation, dummyRepoPath, dummyFilePath]

"""def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                logging.warning("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1 """


def create_bash_file(batchFileCreated, gitLocation, dummyRepoPath):
    if not batchFileCreated:
        # Create batch File
        file = open(batchFileName, 'w')
        file.write("ECHO OFF\n\n" + batchFile.format(dummyRepoPath,
                                                     gitLocation, gitLocation, gitLocation))
        file.close()
        Config.set("File Status", "BAT Created", "True")


def loggingsetup():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)


def run_bash_commands(gitPath, dummyRepoPath, dummyFilePath):
    bashCommand = "start chrome.exe"


def update_dummy_file(gitLocation, dummyRepoPath):
    file = open(os.path.join(dummyRepoPath, 'dummyFile.txt'), 'w')
    file.write(" ")
    file.close()


def main():
    Config.read(".\\config.ini")
    # forsaking usability for hardcoding, but added efficiency //TODO: be smarterer
    gitLocation = Config["Path Options"]["Git Exe Path"]
    dummyRepoPath = Config["Path Options"]["Dummy Repo Path"]
    batchFileCreated = Config.getboolean("File Status", "BAT Created")

    # Create batch file for file updates if needed
    create_bash_file(batchFileCreated, gitLocation, dummyRepoPath)

    update_dummy_file(gitLocation, dummyRepoPath)


main()
