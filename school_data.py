import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

class SchoolData:
    """
    Lớp SchoolData lưu trữ và xử lý dữ liệu nhập học của các trường trung học
    The SchoolData class stores and processes enrollment data for high schools
    """
    
    def __init__(self):
        """
        Khởi tạo lớp với dữ liệu nhập học và thông tin về các trường
        Initializes the class with enrollment data and school information
        """
        self.data = np.array([
            year_2013, year_2014, year_2015, year_2016, year_2017,
            year_2018, year_2019, year_2020, year_2021, year_2022
        ]).reshape(10, 20, 3)
        
        self.school_names = [
            "Centennial High School", "Robert Thirsk School", "Louise Dean School", "Queen Elizabeth High School", "Forest Lawn High School",
            "Crescent Heights High School", "Western Canada High School", "Central Memorial High School", "James Fowler High School",
            "Ernest Manning High School", "William Aberhart High School", "National Sport School", "Henry Wise Wood High School", 
            "Bowness High School", "Lord Beaverbrook High School", "Jack James High School", "Sir Winston Churchill High School", 
            "Dr. E. P. Scarlett High School", "John G Diefenbaker High School", "Lester B. Pearson High School"
        ]
        
        self.school_codes = [
            1224, 1679, 9626, 9806, 9813, 9815, 9816, 9823, 9825, 
            9826, 9829, 9830, 9836, 9847, 9850, 9856, 9857, 9858, 
            9860, 9865
        ]
        
        # Tạo từ điển school_name_to_code mà không dùng zip
        # Create the school_name_to_code dictionary without using zip
        self.school_name_to_code = {}
        for i in range(len(self.school_names)):
            self.school_name_to_code[self.school_names[i]] = self.school_codes[i]

    def print_school_stats(self, school_data, school_index):
        """
        In thống kê nhập học cho một trường cụ thể
        Prints enrollment statistics for a specific school
        
        Parameters:
        - school_data: numpy array chứa dữ liệu nhập học của trường / numpy array containing the school's enrollment data
        - school_index: int, chỉ số của trường trong danh sách / int, the index of the school in the list
        """
        print(f"School Name: {self.school_names[school_index]}, School Code: {self.school_codes[school_index]}")
        print(f"Mean enrollment for Grade 10: {int(np.floor(np.nanmean(school_data[:, 0])))}")
        print(f"Mean enrollment for Grade 11: {int(np.floor(np.nanmean(school_data[:, 1])))}")
        print(f"Mean enrollment for Grade 12: {int(np.floor(np.nanmean(school_data[:, 2])))}")
        print(f"Highest enrollment for a single grade: {int(np.floor(np.nanmax(school_data)))}")
        print(f"Lowest enrollment for a single grade: {int(np.floor(np.nanmin(school_data)))}")

        # In tổng số học sinh nhập học từng năm / Print total enrollment for each year
        for year in range(self.data.shape[0]):
            print(f"Total enrollment for {2013 + year}: {int(np.floor(np.nansum(school_data[year, :])))}")

        print(f"Total ten year enrollment: {int(np.floor(np.nansum(school_data)))}")
        print(f"Mean total yearly enrollment over 10 years: {int(np.floor(np.nanmean(np.nansum(school_data, axis=1))))}")

        over_500 = school_data[school_data > 500]
        if over_500.size == 0:
            print("No enrollments over 500.")
        else:
            print(f"For all enrollments over 500, the median value was: {int(np.floor(np.nanmedian(over_500)))}")

    def main(self):
        """
        Hàm chính của chương trình, xử lý đầu vào người dùng và in các thống kê
        Main function of the program, handles user input and prints statistics
        """
        print("ENSF 692 School Enrollment Statistics")
        print(f"Shape of full data array: {self.data.shape}")
        print(f"Dimensions of full data array: {self.data.ndim}")

        while True:
            user_input = input("Please enter the high school name or school code: ")
            print(f"User input: {user_input}")  # Kiểm tra input của người dùng / Check user input
            try:
                print("\n***Requested School Statistics***\n")
                if user_input.isdigit():
                    # Nếu user_input là số, chuyển đổi sang int và tìm index trong school_codes
                    # If user_input is a number, convert to int and find index in school_codes
                    school_index = self.school_codes.index(int(user_input))
                else:
                    # Nếu user_input không phải là số, tìm index của tên trường trong school_name_to_code
                    # If user_input is not a number, find index of the school name in school_name_to_code
                    school_index = self.school_codes.index(self.school_name_to_code[user_input])
                
                # Lấy dữ liệu của trường dựa trên school_index
                # Get the school's data based on school_index
                school_data = self.data[:, school_index, :]
                self.print_school_stats(school_data, school_index)
                break
            except (ValueError, KeyError):
                print("You must enter a valid school name or code. Please try again.")

        print("\n***General Statistics for All Schools***\n")
        print(f"Mean enrollment in 2013: {int(np.floor(np.nanmean(self.data[0])))}")
        print(f"Mean enrollment in 2022: {int(np.floor(np.nanmean(self.data[-1])))}")
        print(f"Total graduating class of 2022: {int(np.floor(np.nansum(self.data[-1, :, 2])))}")
        print(f"Highest enrollment for a single grade: {int(np.nanmax(self.data))}")
        print(f"Lowest enrollment for a single grade: {int(np.nanmin(self.data))}")

if __name__ == '__main__':
    stats = SchoolData()
    stats.main()
