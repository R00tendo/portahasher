import os
import string
import sys
import hashlib
if sys.argv[1] == "-d":
    decrypted = []
    abc = string.ascii_letters
    abc = abc + "!\"#¤%&/()=?\'¨*_-:,.;[]}{$\\£@~€+1234567890<>|½µäåö \n"
    abc = list(abc)
    path = input("Path to where the hashed files are:")
    if os.path.isdir(path):
        print("Dir found")
        pass
    else:
        print("Dir not found...")
        exit()
    password = input("Enter password for the files:")
    os.chdir(path)
    files = os.listdir()
    string = ""
    print("Decryption in progress, please don't close this window since that will reset the whole decryption")
    for file in files:
        with open(file) as lines:
            for line in lines:
                line = line.replace("\n", "")
                for chara in abc:

                    curhash = hashlib.sha384(bytes(str(password), "utf-8") + bytes(chara, "utf-8")).hexdigest()


                    if  curhash in line:

                        string = string + chara
        decrypted.append("\n\n" + str(file))
        decrypted.append("_______________________________________________________")
        decrypted.append(string)
        string = ""
    seen = []

    for line in decrypted:
        print(line)
    """for line in decrypted:
        for seenline in seen:
            if line == seenline:
                print(seen)
                pass
            else:
                print(line)
                seen.append(line)"""

if sys.argv[1] == "-h":
    print("-e  to hash a directory")
    print("-d  to dehash the directory")
    exit()
if sys.argv[1] == "-e":
    print("Disclaimer: This program only supports the following file types txt, html, cvs, db, php, phtml, py, rb, go, c, webhtml, bat, url")
    filetypes = ['txt', 'html', 'cvs', 'db', 'php', 'phtml', 'py', 'rb', 'go', 'c', 'webhtml', 'bat', 'url']
    path = input("Path to where the files are:")
    if os.path.isdir(path):
        print("Dir found")
        pass
    else:
        print("Dir not found...")
        exit()
    path_to_save = input("Where to save the hashed files?:")
    if os.path.isdir(path_to_save):
        print("Dir found")
        pass
    else:
        print("Dir not found...")
        exit()
    password = input("Enter password for the files (please use a strong one):")
    os.chdir(path)
    files = os.listdir()
    print(files)
    goodtype = []
    good = False
    for file in files:
        filetype = file.split(".")
        print(filetype)
        for type in filetypes:
            if type in filetype[-1]:
                good = True


        if good:
              goodtype.append("good")
        else:
            print(filetype[-1])
            goodtype.append("bad")

    for thefile in range(len(goodtype) -1):
        if "good" in goodtype[thefile]:
            print(files[thefile] + " Has a good filetype")
        else:
            print(files[thefile] + " Has a bad filetype")
            cont = input("Do you want to ignore this file?(y/n):")
            if cont.lower() == "y":
                files.remove(files[thefile])

    password = bytes(str(password), "utf-8")
    for hash in files:
        with open(hash) as hsing:
            name = "hashed_" + hash.replace(" ", "")
            cur = os.getcwd()
            os.chdir("..")
            os.chdir(path_to_save)
            open(name, "w").write("")
            hashedfilewrite = open(name, "a")
            for line in hsing:
                for chara in list(line):

                    chara = bytes(chara, "utf-8")


                    hashchar = hashlib.sha384(password + chara)
                    hashchar.hexdigest()
                    print(hashchar.hexdigest())
                    hashedfilewrite.write(hashchar.hexdigest() + "\n")
                    chara = ""

            hashedfilewrite.close()
            os.chdir(cur)
