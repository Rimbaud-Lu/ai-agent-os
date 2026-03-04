import os

def push():

    os.system("git add .")
    os.system("git commit -m 'upgrade v4'")
    os.system("git push")
