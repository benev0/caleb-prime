import sys
import itemUpdate
import modSpread
import rivenEndo

validArgs = ["--spread", "--riven", "--reset", "common", "uncommon", "rare", "legendary", ""]
flags     = ["--spread", "--riven", "--reset"]
rarities  = ["common", "uncommon", "rare", "legendary"]

def printArgs():
    print("--spread common|uncommon|rare|[legendary] - calculates spread and displays negitive values")
    print("--riven  n                                - calculates and displays the n top endo per plat value rivens")
    print("--reset                                   - resets the item data file")

if __name__=='__main__':
    args = sys.argv[:]
    args.append("")
    args[0] = ""

    for arg in args:
        if arg in validArgs or arg.isnumeric():
            continue
        print("INVALID args")
        printArgs()
        sys.exit(1)

    if "--riven" in args and not args[args.index()+1].isnumeric():
        print("INVALID args")
        print("--riven must be folloed by numeric limit")
        sys.exit(1)

    if "--spred" in args and not args[args.index()-1] in rarities:
        print("INVALID args")

    for i in range(len(args)-1):
        if args[i] == "--spread":
            modSpread.run()

