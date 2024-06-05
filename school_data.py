# school_data.py
# AUTHOR NAME: Tien Nguyen
#
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Declare any global variables needed to store the data here


# You may add your own additional classes, functions, variables, etc.


class SchoolData:
    """
    The SchoolData class stores the enrollment data from given_data.py and processes data.
    """

    def __init__(self):

        # Creates a 3D array to stores the enrollment data from 2013 to 2022, includes 10 years (2013 - 2022), 20 school, and 3D array.
        self.data = np.array([
            year_2013, year_2014, year_2015, year_2016, year_2017,
            year_2018, year_2019, year_2020, year_2021, year_2022
        ]).reshape(10, 20, 3)
        
        # Creates a school name list that stores all school name from the cvs file.
        self.school_names = [
            "Centennial High School", "Robert Thirsk School", "Louise Dean School", "Queen Elizabeth High School", "Forest Lawn High School",
            "Crescent Heights High School", "Western Canada High School", "Central Memorial High School", "James Fowler High School",
            "Ernest Manning High School", "William Aberhart High School", "National Sport School", "Henry Wise Wood High School", 
            "Bowness High School", "Lord Beaverbrook High School", "Jack James High School", "Sir Winston Churchill High School", 
            "Dr. E. P. Scarlett High School", "John G Diefenbaker High School", "Lester B. Pearson High School"
        ]
        
        # Creates a school code list and corresponds to the order of the school name.
        self.school_codes = [
            1224, 1679, 9626, 9806, 9813, 9815, 9816, 9823, 9825, 
            9826, 9829, 9830, 9836, 9847, 9850, 9856, 9857, 9858, 
            9860, 9865
        ]
        
        # Create a add_school_info dictionary to mapping the school name to school code.
        self.add_school_info = {}
        # Uses for loop to add all the school names and codes to the dictionary. Uses the len to know how many school in the data.
        for i in range(len(self.school_names)):
            # By every i in the loop, add the school name and then school code corresponding to value i to the dictionary.
            self.add_school_info[self.school_names[i]] = self.school_codes[i]

    def school_calculate(self, school_data, school_index):
        """
        Prints enrollment statistics for a specific school
        
        The def uses two Parameters:
        - school_data: as numpy array containing the school enrollment data
        - school_index: as the index of the school in the list
        """
        # Print the school name and school cod, use f string.
        print(f"School Name: {self.school_names[school_index]}, School Code: {self.school_codes[school_index]}")
        # Print the mean enrollment for Grades 10
        # Take all the school_data (:), then choose first column as the grade 10 data (0).
        # Use nanmean to ignore the nan data, ground by floor, and ground to int.
        print(f"Mean enrollment for Grade 10: {int(np.floor(np.nanmean(school_data[:, 0])))}")

        # Print the mean enrollment for Grades 11.
        # Take all the school_data (:), then choose second column as the grade 11 data (1).
        # Use nanmean to ignore the nan data, ground by floor, and ground to int.
        print(f"Mean enrollment for Grade 11: {int(np.floor(np.nanmean(school_data[:, 1])))}")

        # Print the mean enrollment for Grades 12.
        # Take all the school_data (:), then choose third column as the grade 12 data (2).
        # Use nanmean to ignore the nan data, ground by floor, and ground to int.
        print(f"Mean enrollment for Grade 12: {int(np.floor(np.nanmean(school_data[:, 2])))}")

        # Print the highest enrollment for a single grade
        print(f"Highest enrollment for a single grade: {int(np.floor(np.nanmax(school_data)))}")
        # Print the lowest enrollment for a single grade
        print(f"Lowest enrollment for a single grade: {int(np.floor(np.nanmin(school_data)))}")

        # Use for loop to print total enrollment for each year
        for year in range(self.data.shape[0]):
            # Take all data that corresponding with year, then calculating the sum, ground floor, and ground int.
            # For each time count, plus the total count (year) with 2013, the result will be the year corresponding (e.g 2013 + 2 = 2015)
            print(f"Total enrollment for {2013 + year}: {int(np.floor(np.nansum(school_data[year, :])))}")

        # Print the total enrollment over 10 years from school_data, ground floor, then ground sum.
        print(f"Total ten year enrollment: {int(np.floor(np.nansum(school_data)))}")
        # Print the mean yearly enrollment over 10 years from school_data
        # Uses axis-1 to calculate sum the elements along each row horizontally, then calculating mean, ground floor, then ground sum.
        print(f"Mean total yearly enrollment over 10 years: {int(np.floor(np.nanmean(np.nansum(school_data, axis=1))))}")

        # Check for enrollments if there are any enrollment over 500 students
        # Count the total of enrollments in the school_data that over 500, if the total is 0, meaning true.
        if np.nansum(school_data > 500) == 0:
            # Print no enrollments over 500 if true.
            print("No enrollments over 500.")
        # If the total greater than 0, meaning false.
        else:
            # Calculate the median of the value that over 500, then ground floor and ground int.
            median_over_500 = int(np.floor(np.nanmedian(school_data[school_data > 500])))
            # Print the median value using f string.
            print(f"For all enrollments over 500, the median value was: {median_over_500}")

    def main(self):

        print("ENSF 692 School Enrollment Statistics")

        # Print Stage 1 requirements here

        # Print the shape of the data array. Uses the shape the print out the shape of an array
        print(f"Shape of full data array: {self.data.shape}")
        # Print the dimention of the data array. Uses the ndim to print out the dimentsions of an array.
        print(f"Dimensions of full data array: {self.data.ndim}")

        # Use the while loop to make sure the invalid input will not terminate program, and only break when the program running successfuly.
        while True:
            # Prompt for user input for the school name or school code.
            user_input = input("Please enter the high school name or school code: ")
            
            # Print Stage 2 requirements here

            print("\n***Requested School Statistics***\n")
            # Use try-except to make sure the user input the valid school code and school name.
            try:
                # Use isdigit() to check the input value is a string for a digit number.
                if user_input.isdigit():
                    # If the input is a number, convert it to int and find index in school_codes that match with the input value.
                    school_index = self.school_codes.index(int(user_input))
                else:
                    # If the input is not a number, but string
                    # Then find index of the school name in add_school_info that match with the input value.
                    school_index = self.school_codes.index(self.add_school_info[user_input])
                
                # Get the school data based on school_index
                school_data = self.data[:, school_index, :]
                # Call the method school_calculate to calculate the mean, sum, min, max, etc. as requests.
                self.school_calculate(school_data, school_index)
                # Exit the loop after print the result
                break
            # Handling the errors by ValueError for the invalid school code, KeyError for the invalid school name.
            except (ValueError, KeyError):
                # Handle errors when a valid school name or code is not found. Tell user to input the valid school name and code.
                print("You must enter a valid school name or code. Please try again.")

        # Print Stage 3 requirements here

        print("\n***General Statistics for All Schools***\n")
        # Print the mean enrollment in 2013. Use (0) as the 2013 is he first value in the array. Thne calculate mean, ground floor and int.
        print(f"Mean enrollment in 2013: {int(np.floor(np.nanmean(self.data[0])))}")
        # Print the mean enrollment in 2022. Use (-1) as the 2022 is he last value in the array. Then calculate mean, ground floor and int.
        print(f"Mean enrollment in 2022: {int(np.floor(np.nanmean(self.data[-1])))}")
        # Calculate the total graduating class of 2022. Use (-1) as the 2022 is he last value in the array
        # Take all value (:) from the grade 12 as the third column (2). Then calculate mean, ground floor and int.
        print(f"Total graduating class of 2022: {int(np.floor(np.nansum(self.data[-1, :, 2])))}")
        # Print the highest enrollment for a single grade.
        print(f"Highest enrollment for a single grade: {int(np.nanmax(self.data))}")
        # Print the lowest enrollment for a single grade.
        print(f"Lowest enrollment for a single grade: {int(np.nanmin(self.data))}")

if __name__ == '__main__':
    stats = SchoolData()
    stats.main()
