# https://open.kattis.com/problems/3dprinter
# Solution by Owen Cooke

def min_days(statues):
    # Initialize day and printer count
    days = 0
    printers = 1
    while statues > 0:
        if statues > printers:
            # Print new set of printers
            printers *= 2
        else:
            # Print statues
            statues -= printers
        days += 1
    return days

if __name__ == "__main__":
    days = min_days(int(input()))
    print(days)