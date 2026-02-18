import os
import subprocess
from pathlib import Path
import shutil

def nusPackagePrompt():
    print("Enter NUS package path (folder can be dragged to the window)")
    packagePath = Path(input())
    if packagePath.exists():
        print("path exists, proceeded")
        subprocess.run(["utils/cdecrypt/cdecrypt.exe", packagePath, "utils/cdecrypt/out"])
        subprocess.run(['java', '-jar', 'utils/nuspacker/NUSPacker.jar', '-in', 'utils/cdecrypt/out', '-out', os.path.join(os.getcwd(), 'output')])
    else:
        print(f"Package path not found in entered location, please try again.")
        nusPackagePrompt()


try:
    shutil.rmtree("utils/cdecrypt/out")
except:
    pass
global keyPath
print("WUP Auto Packer by Grayforz")
keyPath = "utils/nuspacker/encryptKeyWith"
def keyCheck(filePath):
    if (os.path.getsize(filePath) == 0):
        print("Enter Wii U common key: ")
        key = input()
        if (len(key) == 32):
            file = open("utils/nuspacker/encryptKeyWith", "w")
            file.write(key)
            file.close()
        else:
            keyCheck(keyPath)

keyCheck(keyPath)

nusPackagePrompt()
print("Press enter to exit")
enter = input()

