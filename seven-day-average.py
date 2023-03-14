
import csv
import requests


def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)

    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state in new_cases:
            states.append(state)
        if len(state) == 0:
            break

    print(f"\nSeven-Day Averages")

    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)


# TODO: Create a dictionary to store 14 most recent days of new cases by state
def calculate(reader):

    new_cases = {}
    previous_cases = {}

    for line in reader:
        state = line['state']
        cases = int(line['cases'])

        if state in previous_cases:
            new_cases_for_day = cases - previous_cases[state]
        else:
            new_cases_for_day = cases
        previous_cases[state] = cases

        if state not in new_cases:
            new_cases[state] = []
        new_cases[state].append(new_cases_for_day)

        if len(new_cases[state]) > 14:
            new_cases[state].pop(0)
    return new_cases


# TODO: Calculate and print out seven day average for given state
def comparative_averages(new_cases, states):

    for state in states:
        week1 = new_cases[state][0: 7]
        week2 = new_cases[state][7: 14]

        average_week1 = sum(week1) / 7
        average_week2 = sum(week2) / 7
        increase = ((average_week1 + average_week2) / average_week2) * 100
        print(
            f"{state} had a 7 day average of {average_week1}, and an increase of {increase}")


main()
