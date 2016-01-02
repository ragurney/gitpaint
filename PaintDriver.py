import configparser
import logging
import os
from subprocess import check_output

Config = configparser.ConfigParser()
#configSections = ["Git Exe Options", "Dummy Repo Options"]

gitLocation = ""
dummyRepoPath = ""
dummyFilePath = ""

# Bash Commands
#  TODO: Add more info (date, part of letter done), also, definitely change this string lol
bashCD =  "cd {}\n"
bashGitAddFile = "{} {}add -A dummyFile.txt\n"
            #"{} commit -m \"File Updated\"\n" \
            #"{} push origin master\n" \
            #"start chrome.exe\n"


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

#def setup():
    # Could later extend to log part of letter drawn with that commit


def loggingsetup():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)

def run_bash_commands(gitPath, dummyRepoPath, dummyFilePath):
    bashCommand = "start chrome.exe"
    check_output(bashCommand, shell=True)

def update_dummy_file(gitLocation, dummyRepoPath):
    file = open(os.path.join(dummyRepoPath,'dummyFile.txt'), 'w')
    file.write(" ")
    file.close()

    # execute bash commands
    #print(bashFile.format(dummyRepoPath, gitLocation, gitLocation, gitLocation))
   # check_output((bashFile.format(dummyRepoPath, gitLocation, gitLocation, gitLocation)), shell=True)
    check_output(bashCD.format(dummyRepoPath), shell=True)
    check_output(bashGitAddFile.format(gitLocation), shell=True)
#-A, commit, push

def main():
    Config.read(".\\config.ini")

    #forsaking usability for hardcoding, but added efficiency //TODO: be smarterer
    gitLocation = Config["Path Options"]["Git Exe Path"]
    dummyRepoPath = Config["Path Options"]["Dummy Repo Path"]
    update_dummy_file(gitLocation, dummyRepoPath)

main()
