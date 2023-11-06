from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
import argparse
import calendar


def step1(name: str):
    print(f"Hello, my name is {name}!")

def step2(bday: str):
    birthdate: datetime = datetime.strptime(bday, '%Y-%m-%d')
    age: int = relativedelta(datetime.now(), birthdate).years
    print(f"I am {age} this year.")

def step3():
    dow: str = calendar.day_name[date.today().weekday()] 
    print(f"Today is {dow}.")

def getArgs():
    parser = argparse.ArgumentParser(description="Get user input.")
    parser.add_argument(
        "-n",
        "--name",
        action="store",
        required=True,
        type=str,
        help="Enter name in string.",
    )
    parser.add_argument(
        "-bd",
        "--birthdate",
        action="store",
        required=True,
        type=str,
        help="Enter birthdate in yyyy-mm-dd format.",
    )
    return parser.parse_args()

if __name__ == "__main__":

    arg = getArgs()

    step1(name=arg.name)
    step2(bday=arg.birthdate)
    step3()