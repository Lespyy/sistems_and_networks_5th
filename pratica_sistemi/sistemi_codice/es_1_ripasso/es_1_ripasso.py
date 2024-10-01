"""

name: Danilo Rinaldi

Class: 5AROB

assignment:

Status: not finished

Description:

"""


def main():
    list = ["4o", "o1-preview", "4o-mini", "o1-mini"]

    #DO NOT USE
    for i in range(len(list)):
        print("chat gpt" + list[i])

    print()

    # USE INSTEAD
    for version in list:
        print(f"chat gpt {version}")

    print()

    for index, version in enumerate(list):
        print(f"the version number {index + 1} of chat gpt is {version}")

    print()

    nomi = ["Danilo", "Camillo", "Verty", "Rinaldi"]

    #the shortest one wins and it doesn't give you any error
    for nome, versione in zip(nomi, list):
        print(f"{nome} use chat gpt {version}")

    print()

    nomi.append("Epik")

    print(nomi)

    print()

    print(nomi[0])

    print()

    #indicizzazione

    print(nomi[-1])

    print()

    print(nomi[-2])

    print()

    #slicing

    print(nomi[0:2]) #print from 0 to 2 excluded

    print()

    print(nomi[0:-1])

    #the first 0 can be omitted

    print()

    print(nomi[:-1])

    print()

    print(nomi[-2:])

    print()

    print(nomi[::2])#print the element every 2 ones

if __name__ == "__main__":
    main()