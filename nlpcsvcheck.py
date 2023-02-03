from string import capwords
import re
import pickle


def regex_check_and_yell(param, check: re.Pattern, errmsg: str, inpmsg: str):
    # check if matches regex
    while check.fullmatch(param) is None:
        # if not, yell
        print(errmsg.format(param))
        param = input(inpmsg)
    return param


class Person:
    def __init__(self, inp: dict):
        # generic fixes
        self.first = capwords(inp['First'])
        self.last = capwords(inp['Last'])
        self.mi = 'X' if not inp['Middle Initial'] else capwords(
            inp['Middle Initial'])

        # regex fixes
        self.id = regex_check_and_yell(
            inp['ID'], re.compile(r'\w\w\d\d\d\d'),
            'ID Invalid: {}\nID is two letters followed by 4 digits',
            'Please enter a valid id: ')
        self.phone = regex_check_and_yell(
            inp['Office phone'], re.compile(r'\d\d\d-\d\d\d-\d\d\d\d'),
            'Phone {} is invalid\nEnter phone number in form 123-456-7890',
            'Enter phone number: ')

    def display(self):
        # a multiline fstring, how quaint
        print(
            f"""Employee id: {self.id}
\t{self.first} {self.mi} {self.last}
\t{self.phone}\n""")


# parse the csv line
# note this whole system wouldn't need to be done
# if i could just, yknow, import the builtin csv module
def parse_csv_line(headers: [str], inp: str) -> Person:
    # zip into dict
    parse = dict(zip(headers, inp.split(',')))
    return Person(parse)


def main():
    from sys import argv, exit
    if len(argv) > 2:
        print("generic error message about too many command line args")
        exit(1)

    # actual work
    with open(argv[1], 'r', encoding='utf-8-sig') as inp:
        # create keys
        headers = inp.readline().strip().split(',')
        # then create life
        people = [parse_csv_line(headers, x.strip()) for x in inp.readlines()]
        dict_people = {}
        for x in people:
            if x.id in dict_people:
                print(f"duplicate ID found: {x.id}")
                exit(2)
            dict_people[x.id] = x
        # then take life to the sewers
        with open("people.pkl", "wb") as sewers:
            pickle.dump(people, sewers)
        # then filter the sewer water
        with open("people.pkl", "rb") as sewer_water:
            people = pickle.load(sewer_water)
        # then yell at life
        print('\n\nEmployee list:\n')
        for person in people:
            person.display()
        # something something "philosopical quote"
    return


if __name__ == "__main__":
    main()
