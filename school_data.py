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

# Data from 2013 to 2022 / Dữ liệu đăng ký nhập học từ 2013 đến 2022
data = np.array([
    year_2013, year_2014, year_2015, year_2016, year_2017,
    year_2018, year_2019, year_2020, year_2021, year_2022
])

# Ensure the array is 3-dimensional with 10 years, 20 schools, 3 grades / Đảm bảo mảng là 3 chiều với 10 năm, 20 trường học, 3 lớp
data = data.reshape(10, 20, 3)

# List of school names / Danh sách tên trường học
school_names = [
    "Centennial High School", "Robert Thirsk School", "Louise Dean School", "Queen Elizabeth High School", "Forest Lawn High School",
    "Crescent Heights High School", "Western Canada High School", "Central Memorial High School", "James Fowler High School",
    "Ernest Manning High School", "William Aberhart High School", "National Sport School", "Henry Wise Wood High School", 
    "Bowness High School", "Lord Beaverbrook High School", "Jack James High School", "Sir Winston Churchill High School", 
    "Dr. E. P. Scarlett High School", "John G Diefenbaker High School", "Lester B. Pearson High School"
]

# List of school codes / Danh sách mã trường học
school_codes = [
    1224, 1679, 9626, 9806, 9813, 9815, 9816, 9823, 9825, 
    9826, 9829, 9830, 9836, 9847, 9850, 9856, 9857, 9858, 
    9860, 9865
]

# Dictionary mapping school names to codes / Dictionary ánh xạ từ tên trường thành mã trường
school_name_to_code = {name: code for name, code in zip(school_names, school_codes)}

# You may add your own additional classes, functions, variables, etc.

def school_statistics(school_identifier):
    """
    Compute and print statistics for a specific school.
    Tính toán và in thống kê cho một trường học cụ thể.

    :param school_identifier: School name or code. / Tên hoặc mã số trường học.
    :raises ValueError: If the school name or code is invalid. / Nếu tên hoặc mã trường không hợp lệ.
    """
    # Determine the index of the school based on code or name / Xác định chỉ mục của trường học dựa trên mã hoặc tên trường
    if isinstance(school_identifier, int):  # Check if the identifier is an integer / Kiểm tra nếu định danh là số nguyên
        try:
            school_index = school_codes.index(school_identifier)  # Find the index of the school code / Tìm chỉ mục của mã trường
        except ValueError:
            raise ValueError("You must enter a valid school name or code. / Bạn phải nhập tên hoặc mã trường hợp lệ.")
    elif isinstance(school_identifier, str):  # Check if the identifier is a string / Kiểm tra nếu định danh là chuỗi
        try:
            school_code = school_name_to_code[school_identifier]  # Map school name to code / Ánh xạ tên trường thành mã trường
            school_index = school_codes.index(school_code)  # Find the index of the school code / Tìm chỉ mục của mã trường
        except KeyError:
            raise ValueError("You must enter a valid school name or code. / Bạn phải nhập tên hoặc mã trường hợp lệ.")
    else:
        raise ValueError("You must enter a valid school name or code. / Bạn phải nhập tên hoặc mã trường hợp lệ.")

    # Retrieve school data based on index / Lấy dữ liệu của trường học dựa trên chỉ mục
    school_data = data[:, school_index, :]

    # Print school information and statistics / In thông tin trường học và các thống kê
    print(f"School Name: {school_names[school_index]}, School Code: {school_codes[school_index]}")
    print(f"Mean enrollment for Grade 10: {int(np.floor(school_data[:, 0].mean()))}")
    print(f"Mean enrollment for Grade 11: {int(np.floor(school_data[:, 1].mean()))}")
    print(f"Mean enrollment for Grade 12: {int(np.floor(school_data[:, 2].mean()))}")
    print(f"Highest enrollment for a single grade: {int(school_data.max())}")
    print(f"Lowest enrollment for a single grade: {int(school_data.min())}")

    # Calculate and print total enrollment per year / Tính toán và in tổng số đăng ký hàng năm
    for year in range(data.shape[0]):  # Loop through each year / Lặp qua từng năm
        total_enrollment = int(np.floor(np.nansum(school_data[year, :])))  # Calculate total enrollment for the year / Tính tổng số đăng ký cho năm
        print(f"Total enrollment for {2013 + year}: {total_enrollment}")

    # Calculate and print total enrollment over ten years / Tính toán và in tổng số đăng ký trong mười năm
    total_ten_year = int(np.floor(np.nansum(school_data)))
    print(f"Total ten year enrollment: {total_ten_year}")

    # Calculate and print mean total yearly enrollment / Tính toán và in tổng số đăng ký trung bình hàng năm
    mean_total_yearly = int(np.floor(np.nanmean(np.nansum(school_data, axis=1))))
    print(f"Mean total yearly enrollment over 10 years: {mean_total_yearly}")

    # Check and print the median value of enrollments > 500 / Kiểm tra và in giá trị trung vị của các đăng ký > 500
    over_500 = school_data[school_data > 500]
    if over_500.size == 0:
        print("No enrollments over 500. / Không có đăng ký nào trên 500.")
    else:
        print(f"For all enrollments over 500, the median value was: {int(np.floor(np.median(over_500)))}")

def general_statistics():
    """
    Compute and print general statistics for all schools.
    Tính toán và in thống kê chung cho tất cả các trường học.
    """
    print(f"Mean enrollment in 2013: {int(np.floor(np.nanmean(data[0])))}")
    print(f"Mean enrollment in 2022: {int(np.floor(np.nanmean(data[-1])))}")
    total_graduating_2022 = int(np.floor(np.nansum(data[-1, :, 2])))
    print(f"Total graduating class of 2022: {total_graduating_2022}")
    print(f"Highest enrollment for a single grade: {int(np.nanmax(data))}")
    print(f"Lowest enrollment for a single grade: {int(np.nanmin(data))}")

def main():
    """
    Main program to compute and print school enrollment statistics.
    Chương trình chính để tính toán và in thống kê nhập học của các trường học.
    """
    print("ENSF 692 School Enrollment Statistics")

    # Print Stage 1 requirements here
    # Stage 1: Array creation and print shape and dimensions / Tạo mảng và in hình dạng và kích thước của mảng 3 chiều
    print(f"Shape of full data array: {data.shape}")
    print(f"Dimensions of full data array: {data.ndim}")

    # Get user input and compute statistics for the specific school / Nhận đầu vào từ người dùng và tính toán thống kê cho trường học cụ thể
    while True:
        user_input = input("Please enter the high school name or school code: / Vui lòng nhập tên trường hoặc mã trường: ")
        try:
            print("\n***Requested School Statistics***\n")  # Print heading for requested school statistics / In tiêu đề cho thống kê trường học được yêu cầu
            if user_input.isdigit():  # Check if input is a digit / Kiểm tra nếu đầu vào là số
                school_code = int(user_input)  # Convert input to integer / Chuyển đầu vào thành số nguyên
                school_statistics(school_code)  # Compute statistics for the school / Tính toán thống kê cho trường học
            else:
                school_statistics(user_input)  # Compute statistics for the school name / Tính toán thống kê cho tên trường học
            break
        except ValueError as e:
            print(e)  # Print error message / In thông báo lỗi

    # Print general statistics for all schools / In thống kê chung cho tất cả các trường học
    print("\n***General Statistics for All Schools***\n")
    general_statistics()

if __name__ == '__main__':
    main()
