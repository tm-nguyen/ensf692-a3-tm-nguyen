
The City of Calgary publishes data on various demographics, include school enrollment. You are being asked to design a terminal-based application for computing and printing statistics based on given input.
Your application must meet the following design specifications:
* Your final output should match the given examples (screenshots included in the rubric)
* Stage 1: Array Creation
  1. Create a 3-dimensional array using the provided high school enrollment data. You must use a NumPy array, but you may choose how to arrange the size in each dimension.
  2. Print the shape and dimensions of the array.
* Stage 2: School Stats
  1. Prompt the user to enter either the name or numerical code of a school. If the name or code do not exist within the given data, raise a ValueError to print “You must enter a valid school name or code.”
  2. Calculate and print the answers for the following school-specific statistics, using the given output as a template.
    * The school name and school code
    * Mean enrollment for Grade 10 across all years
    * Mean enrollment for Grade 11 across all years
    * Mean enrollment for Grade 12 across all years
    * Highest enrollment for a single grade within the entire time period
    * Lowest enrollment for a single grade within the entire time period
    * Total enrollment for each year from 2013 to 2022
	* Total ten year enrollment
	* Mean total yearly enrollment over 10 years
    * Education planners want to better understand the impact of large-scale classes in high schools. Determine if any enrollment numbers were over 500. If not, print “No enrollments over 500.” If yes, print the median value of the >500 enrollments.
* Stage 3: General Stats
  1. Every run of your program should also calculate and print the answers for the following general statistics. These will be the same for every run.
    * The mean enrollment in 2013
    * The mean enrollment in 2022
    * Total graduating class of 2022 across all schools
    * Highest enrollment for a single grade within the entire time period (across all schools)
    * Lowest enrollment for a single grade within the entire time period (across all schools)
* All values should be printed as integers, and should be the final floor value of each calculation (e.g. 5/2 = 2, not 2.0 or 2.5)
* Your code should include and use at least one 3-dimensional NumPy array, at least one subarray view, at least four different NumPy computational functions, at least one masking operation, and at least one dictionary.
* Your code must follow the conventions discussed so far in the course (ClassNames, four spaces for indentations, spaces between variables/operators, comments throughout, etc.)
* All classes, methods, and functions must contain docstring documentation.
    1. For each class, include a functionality summary and describe any class and/or instance variables (do not include a separate docstring for \_\_init\_\_)
    2. For each method/function, include a functionality summary and describe parameters and return values (or specify if there are none)
    3. Main functions do not need a docstring but should be well-commented 
* Your code will be run by the TAs as your end user.
* FAQs about the assignment will be answered on the D2L discussion boards. Please check the boards for any clarifications before submitting.
* The grading rubric will be posted to D2L and includes example execution scenarios.
