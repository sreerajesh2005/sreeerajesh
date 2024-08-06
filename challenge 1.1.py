def is_leap_year(year: int) -> bool:
    """
    Determine if the given year is a leap year.
    
    Args:
    year (int): The year to check.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def main():
    """
    Main function to get user input and check if the year is a leap year.
    """
    try:
        year = int(input("Enter the year: "))
        if is_leap_year(year):
            print(f'{year} is a leap year.')
        else:
            print(f'{year} is not a leap year.')
    except ValueError:
        print("Please enter a valid integer for the year.")

if __name__ == "__main__":
    main()
