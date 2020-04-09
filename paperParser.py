#!/usr/bin/python3

from bs4 import BeautifulSoup
import os

directory = os.getcwd()

def parse():
    for filename in os.listdir(directory):
        if filename.endswith(".XML"):

            f = open(filename)

            with open(filename, "r", encoding="utf8") as f:
                contents = f.read()
                soup = BeautifulSoup(contents, "xml")

                items = soup.find_all("subject")

            match = 0

            for stuff in items:
                if 'computer and information sciences' in stuff.contents[0].lower():
                    match = match + 1

            if match >= 1:
                src = filename
                dst = "1_" + filename.lstrip("1_").lstrip("0_")
                os.rename(src, dst)
            else:
                src = filename
                dst = "0_" + filename.lstrip("1_").lstrip("0_")
                os.rename(src, dst)

            f.close()
        else:
            continue


def extract():

    newDir = directory+"/extractedAbstractFiles/"
    newDir2 = directory+"/extractedSummaryFiles/"
    os.makedirs(newDir, exist_ok=True)
    os.makedirs(newDir2, exist_ok=True)

    for filename in os.listdir(directory):
        if filename.startswith("1_"):
            f = open(filename)

            with open(filename, "r", encoding="utf8") as f:
                contents = f.read()
                soup = BeautifulSoup(contents, "xml")

                abstract = soup.find_all("abstract")
                sec = soup.find_all('sec')

                newFile = newDir+filename.lstrip('1_asset_id=10.1371%2Fjournal.')
                newFile2 = newDir2+filename.lstrip('1_asset_id=10.1371%2Fjournal.')

                f1 = open(newFile, 'w+')
                f2 = open(newFile2, 'w+')

            for stuff in abstract:
                f1.write(stuff.getText())
                continue

            for stuff in sec:
                intro = stuff.find_all('title')
                for stuff2 in intro:
                    if "Introduction" in stuff2:
                        f2.write(stuff.getText().lstrip('Introduction'))
            f2.close()                                                                
            f1.close()
            f.close()


if __name__ == "__main__":
    parse()
    extract()
