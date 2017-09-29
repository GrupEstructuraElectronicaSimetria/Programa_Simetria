import os


def cleaning(extensions):
    for ext in extensions:
        filelist = [ f for f in os.listdir(".") if f.endswith('.'+ext)]
        for f in filelist:
            os.remove(f)