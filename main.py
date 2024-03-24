import sys
import os
import itemUpdate
import modSpread
import rivenEndo

validArgs = ["--spread", "--riven", "--reset", "common", "uncommon", "rare", "legendary", ""]
flags     = ["--spread", "--riven", "--reset"]
rarities  = ["common", "uncommon", "rare", "legendary"]

defaultRarity = "legendary"

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def printArgs():
    print("--spread common|uncommon|rare|[legendary] - calculates spread and displays negitive values")
    print("--riven  n                                - calculates and displays the n top endo per plat value rivens")
    print("--reset                                   - resets the item data file; always first operation")

if __name__=='__main__':
    args = sys.argv[:]
    args.append("")

    if len(args) == 1:
        printArgs()
        sys.exit(0)

    if len(args) != len(set(args)):
        print("INVALID args duplicate entries")
        printArgs()
        sys.exit(1)

    args[0] = ""

    for arg in args:
        if arg in validArgs or arg.isnumeric():
            continue
        print("INVALID args")
        printArgs()
        sys.exit(1)

    if "--riven" in args and not args[args.index("--riven")+1].isnumeric():
        print("INVALID args")
        print("--riven must be folloed by numeric limit")
        printArgs()
        sys.exit(1)

    if "--spred" in args and not args[args.index("--spred")-1] in rarities:
        print("INVALID args")

    if "--reset" in args:
        itemUpdate.run()


    spreads = None
    rivens = None
    rivenCount = None

    for i in range(len(args)-1):
        if args[i] == "--spread":
            if args[i+1] in rarities:
                defaultRarity = args[i+1]
            spreads = modSpread.run(defaultRarity)

        elif args[i] == "--riven":
            rivens = rivenEndo.run()
            rivenCount = int(args[i+1])

        elif args[i] == "--reset":
            pass

    clear()

    if not rivens is None and not rivenCount is None:
        print("Rivens:")
        rivenEndo.render(rivens, rivenCount)
        print()

    if not spreads is None:
        print("Spreads:")
        modSpread.render(spreads)
