import os
import re


def doReName(path):
    patternList = [re.compile(r'E(\d+)'), re.compile(r'EP(\d+)'), re.compile(r'第(\d+)集'), re.compile(r'\((\d+)\)')]
    entries = os.listdir(path)
    for entry in entries:
        fName = f"{path}\\{entry}"
        if '.' in entry:
            nameEnd = entry.split('.')[-1]
            if entry.endswith('.jpg') or entry.endswith('.nfo') or entry.endswith('.png'):
                os.remove(fName)
                continue
            numbers = None
            for pattern in patternList:
                match = pattern.search(entry)
                if match:
                    numbers = match[1]
                    if len(numbers) < 2:
                        numbers = '0' + numbers
                    break
            if numbers is not None:
                newName = f"{path}\\E{numbers}.{nameEnd}"
                os.rename(fName, newName)


