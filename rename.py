import os
import re


def doReName(path):
    pattern = re.compile(r'(E|EP)(\d{2})')
    pattern2 = re.compile(r'\((\d+)\)')
    entries = os.listdir(path)
    for entry in entries:
        fName = f"{path}\\{entry}"
        if entry.endswith('.jpg') or entry.endswith('.nfo') or entry.endswith('.png'):
            os.remove(fName)
            continue
        match = pattern.search(entry)
        if match:
            prefix, numbers = match.groups()
            nameEnd = entry.split('.')[-1]
            newName = f"{path}\\E{numbers}.{nameEnd}"
            os.rename(fName, newName)
            continue
        match2 = pattern2.findall(entry)
        if match2:
            numbers = match2[0]
            if len(numbers) < 2:
                numbers = '0' + numbers
            nameEnd = entry.split('.')[-1]
            newName = f"{path}\\E{numbers}.{nameEnd}"
            os.rename(fName, newName)


