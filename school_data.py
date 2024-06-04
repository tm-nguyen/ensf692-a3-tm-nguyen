# school_data.py
# AUTHOR NAME
#
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Declare any global variables needed to store the data here

# Data from 2013 to 2022 
data = np.array([
    year_2013, year_2014, year_2015, year_2016, year_2017,
    year_2018, year_2019, year_2020, year_2021, year_2022
])

# Ensure the array is 3-dimensional with 10 years, 20 schools, 3 grades
data = data.reshape(10, 20, 3)

# List of school names 
school_names = [
    "Centennial High School", "Robert Thirsk School", "Louise Dean School", "Queen Elizabeth High School", "Forest Lawn High School",
    "Crescent Heights High School", "Western Canada High School", "Central Memorial High School", "James Fowler High School",
    "Ernest Manning High School", "William Aberhart High School", "National Sport School", "Henry Wise Wood High School", 
    "Bowness High School", "Lord Beaverbrook High School", "Jack James High School", "Sir Winston Churchill High School", 
    "Dr. E. P. Scarlett High School", "John G Diefenbaker High School", "Lester B. Pearson High School"
]

# List of school codes 
school_codes = [
    1224, 1679, 9626, 9806, 9813, 9815, 9816, 9823, 9825, 
    9826, 9829, 9830, 9836, 9847, 9850, 9856, 9857, 9858, 
    9860, 9865
]

# Dictionary mapping school names to codes 
school_name_to_code = {name: code for name, code in zip(school_names, school_codes)}

# You may add your own additional classes, functions, variables, etc.

def school_statistics(school_identifier):
    """
    Compute and print statistics for a specific school.


    :param school_identifier: School name or code.
    :raises ValueError: If the school name or code is invalid. 
    """
    # Determine the index of the school based on code or name 
    if isinstance(school_identifier, int):  # Check if the identifier is an integer
        try:
            school_index = school_codes.index(school_identifier)  # Find the index of the school code
        except ValueError:
            raise ValueError("You must enter a valid school name or code.")
    elif isinstance(school_identifier, str):  # Check if the identifier is a string
        try:
            school_code = school_name_to_code[school_identifier]  # Map school name to code
            school_index = school_codes.index(school_code)  # Find the index of the school code
        except KeyError:
            raise ValueError("You must enter a valid school name or code.")
    else:
        raise ValueError("You must enter a valid school name or code.")

    # Retrieve school data based on index 
    school_data = data[:, school_index, :]

    # Print school information and statistics 
    print(f"School Name: {school_names[school_index]}, School Code: {school_codes[school_index]}")
    print(f"Mean enrollment for Grade 10: {int(np.floor(school_data[:, 0].mean()))}")
    print(f"Mean enrollment for Grade 11: {int(np.floor(school_data[:, 1].mean()))}")
    print(f"Mean enrollment for Grade 12: {int(np.floor(school_data[:, 2].mean()))}")
    print(f"Highest enrollment for a single grade: {int(school_data.max())}")
    print(f"Lowest enrollment for a single grade: {int(school_data.min())}")

    # Calculate and print total enrollment per year 
    for year in range(data.shape[0]):  # Loop through each year 
        total_enrollment = int(np.floor(np.nansum(school_data[year, :])))  # Calculate total enrollment for the year
        print(f"Total enrollment for {2013 + year}: {total_enrollment}")

    # Calculate and print total enrollment over ten years
    total_ten_year = int(np.floor(np.nansum(school_data)))
    print(f"Total ten year enrollment: {total_ten_year}")

    # Calculate and print mean total yearly enrollment
    mean_total_yearly = int(np.floor(np.nanmean(np.nansum(school_data, axis=1))))
    print(f"Mean total yearly enrollment over 10 years: {mean_total_yearly}")

    # Check and print the median value of enrollments > 500
    over_500 = school_data[school_data > 500]
    if over_500.size == 0:
        print("No enrollments over 500.")
    else:
        print(f"For all enrollments over 500, the median value was: {int(np.floor(np.median(over_500)))}")

def general_statistics():

    # Compute and print general statistics for all schools.

    print(f"Mean enrollment in 2013: {int(np.floor(np.nanmean(data[0])))}")
    print(f"Mean enrollment in 2022: {int(np.floor(np.nanmean(data[-1])))}")
    total_graduating_2022 = int(np.floor(np.nansum(data[-1, :, 2])))
    print(f"Total graduating class of 2022: {total_graduating_2022}")
    print(f"Highest enrollment for a single grade: {int(np.nanmax(data))}")
    print(f"Lowest enrollment for a single grade: {int(np.nanmin(data))}")

def main():

    # Main program to compute and print school enrollment statistics.

    print("ENSF 692 School Enrollment Statistics")

    # Print Stage 1 requirements here
    # Stage 1: Array creation and print shape and dimensions
    print(f"Shape of full data array: {data.shape}")
    print(f"Dimensions of full data array: {data.ndim}")

    # Get user input and compute statistics for the specific school
    while True:
        user_input = input("Please enter the high school name or school code: ")
        try:
            print("\n***Requested School Statistics***\n")  # Print heading for requested school statistics
            if user_input.isdigit():  # Check if input is a digit 
                school_code = int(user_input)  # Convert input to integer
                school_statistics(school_code)  # Compute statistics for the school
            else:
                school_statistics(user_input)  # Compute statistics for the school name
            break
        except ValueError as e:
            print(e)  # Print error message

    # Print general statistics for all schools
    print("\n***General Statistics for All Schools***\n")
    general_statistics()

if __name__ == '__main__':
    main()
