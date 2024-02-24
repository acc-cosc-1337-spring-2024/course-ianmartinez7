#

# main.py

from value_return import get_hour, get_minutes, get_seconds

def main():
    epoch_seconds = 3800
    hours = get_hour(epoch_seconds)
    minutes = get_minutes(epoch_seconds)
    seconds = get_seconds(epoch_seconds)

    # Format the time to HH:MM:SS
    time_string = f"{hours:02}:{minutes:02}:{seconds:02}"
    print(time_string)

main()
