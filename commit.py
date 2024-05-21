#!/usr/bin/python3


# Args to maipulate as needed

import os

message = "commit till 60"
content = "  "
number_of_commits = 60



def gitPush():
	os.system("git add .")
    # subprocess.run("git add .")
	os.system('git commit -m "commit"')
	os.system("git push origin main")


for i in range(1, number_of_commits):
    with open("README.md", "w+") as file:
        file.write("  ")
    gitPush()

