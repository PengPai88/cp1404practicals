STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "SA": "South Australia", "TAS": "Tasmania"}

print("All states:")
for code, name in STATE_NAMES.items():
    print(f"{code:3} is {name}")

state_code = input("Enter short state: ").upper()
try:
    print(STATE_NAMES[state_code])
except KeyError:
    print("Invalid short state")