import os
import pickle
import random
import argparse
import sys

def menu():
    print("1. Compress sentence")
    print("2. Decompress sentence")
    print("3. Compress file")
    initMenuChoice = input("\nSelect a choice: ")
    if initMenuChoice == "1":
        words = input("Specify sentence to enumerate: ")
        wordsArray = list(words)

        uniqueWords = unique(wordsArray)

        errorList = []
        el = errorList

        el.append("Caught words " + words)

        doStuff(words, uniqueWords, wordsArray)
    elif initMenuChoice == "3":

        words = []

        fn = input("Specify file name to compress: ")
        try:
            with open(fn, 'r') as f:
                words = f.read()
        except UnicodeDecodeError:
            print("Does not support this filetype.")

        wordsArray = list(words)

        uniqueWords = unique(wordsArray)

        errorList = []
        el = errorList

        el.append("Caught words " + words)

        doStuff(words, uniqueWords, wordsArray)
    elif initMenuChoice == "2":
        readFile()
    else:
        print("Select one of the options...")
        menu()


def unique(input):
    output = []
    for x in input:
        if x not in output:
            output.append(x)
    return output


def saveToFile(words, uniqueWords, remake):
    print(
        "[Ambiguous instructions and a level of human guesswork are required to enhance security on this still slightly broken program]")
    keycode = input("Please enter encryption keycode (four digit number): ")

    sr = []

    for i in remake:
        i = i + (int(keycode) - 615)
        print(i)
        sr.append(i)

    print("SR LIST" + str(sr))

    mut = []

    srNew = []

    for n in sr:
        print(n)
        mutVal = random.randint(1, 1000)
        mut.append(mutVal)
        srNew.append(n + mutVal)

    if not os.path.exists("compressed"):
        os.makedirs("compressed")

    fileName = input("Please select a file name")

    with open(("./compressed/" + fileName + "Uniques.txt"), "wb") as f:
        pickle.dump(uniqueWords, f)
    with open(("./compressed/" + fileName + "Nums.txt"), "wb") as f:
        pickle.dump(srNew, f)
    with open(("./compressed/" + fileName + "Mut.txt"), "wb") as f:
        pickle.dump(mut, f)

    print("Saved to: " + fileName)

    menu()


def readFile():
    print(
        "[Ambiguous instructions and a level of human guesswork are required to enhance security on this still slightly broken program]")
    keycode = input("Please enter encryption keycode (four digit number): ")

    fileName = input("Please select a file name: ")

    read = []

    with open(("./compressed/" + fileName + "Uniques.txt"), "rb") as f:
        uniques = pickle.load(f)
        print(str(uniques))

    with open(("./compressed/" + fileName + "Nums.txt"), "rb") as f:
        nums = pickle.load(f)
        print(str(nums))

    with open(("./compressed/" + fileName + "Mut.txt"), "rb") as f:
        mut = pickle.load(f)
        print(str(mut))

    readSr = []

    print("Work in progress")
    xNu = 0
    for i in nums:
        ire = int(nums[xNu])
        iInit = ire - int(keycode)
        iNew = iInit - mut[xNu]
        readSr.append(uniques[iNew])
        xNu = xNu + 1

    print(readSr)

    strJoin = ''.join(readSr)

    print(strJoin)

    print("Fin: " + str(readSr))

    if not os.path.exists("output"):
        os.makedirs("output")

    with open("./output/" + fileName + "Output.txt", "w") as x_file:
        x_file.write(strJoin)

    menu()


def moreThing(words, uniqueWords, nums):
    if any(uniqueWords) in words:
        print("Starting sorter")

    remake = []

    for i in words:
        index = uniqueWords.index(i)
        remake.append(index + 615)

    print("Original words" + str(words))
    print("Final: " + str(remake))

    saveToFile(words, uniqueWords, remake)


def doStuff(words, uniqueWords, wordsArray):
    print("Unique words: " + str(uniqueWords))

    nums = []

    for i, c in enumerate(uniqueWords):
        nums.append(i + 1)

    print("Number sequence: " + str(nums))

    moreThing(wordsArray, uniqueWords, nums)


print("// File crypter and decrypter -- (secure version) //")

parser = argparse.ArgumentParser(description='ADD YOUR DESCRIPTION HERE')

if len(sys.argv) > 1:
    parser = argparse.ArgumentParser(description='ADD YOUR DESCRIPTION HERE')
    parser.add_argument('-df','--decrypt-file', help="Decrypt a file", required=False)
    parser.add_argument('-cf', '--compress-file', help="Compress a file", required=False)
    parser.add_argument('-cs', '--compress-string', help="Compress a string", required=False)
    args = parser.parse_args()

    if args.():
        print("Bobo")

else:
    menu()

