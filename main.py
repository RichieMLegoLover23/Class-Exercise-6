#1
# Ask the user for their first name, last name, and age
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")

# Open a file in write mode and write the user's information to the file
with open("user_info.txt", "w") as file:
    file.write(f"First Name: {first_name}\n")
    file.write(f"Last Name: {last_name}\n")
    file.write(f"Age: {age}\n")

# Open the file in read mode and read the contents of the file
with open("user_info.txt", "r") as file:
    contents = file.read()

# Print the contents of the file to the console
print("User Information:")
print(contents)








#2
# Open the file
file = open("example.txt", "r")

# Read each line and print it
for line in file:
    print(line)

# Close the file
file.close()














#3
# Prompt the user to enter the salary
salary = int(input("Enter the salary: "))

# Prompt the user to enter the number of days of sales
num_sales_days = int(input("Enter the number of days of sales: "))

# Initialize the total sales and the commission
total_sales = 0
commission = 0

# Loop through each day of sales
for i in range(num_sales_days):
    # Prompt the user to enter the sales for this day
    sales = int(input("Enter the sales for day {}: ".format(i+1)))
    
    # Add the sales to the total sales
    total_sales += sales
    
# Check if the total sales are greater than 1000
if total_sales > 1000:
    # Calculate the commission (10% of the salary)
    commission = 0.1 * salary
    
# Calculate the final salary (salary plus commission)
final_salary = salary + commission

# Print out the final salary
print("Final salary: {}".format(final_salary))




























#4
# Open the file in read mode
file = open("example.txt", "r")

# Read the contents of the file
content = file.read()

# Print the contents of the file
print(content)

# Close the file
file.close()
























#5
# Prompt the user to enter the address information
address = input("Enter the address: ")
city = input("Enter the city: ")
state = input("Enter the state: ")
zip_code = input("Enter the zip code: ")

# Concatenate the information into a single string
info = "{}\n{}, {} {}".format(address, city, state, zip_code)

# Open the file in write mode
with open("address.txt", "w") as file:
    # Write the information to the file
    file.write(info)

# Print a message indicating that the information was saved
print("Address information saved to address.txt.")


























#6
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton


class NumberCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Create the labels and input fields for the numbers
        self.num1_label = QLabel(self)
        self.num1_label.setText('Enter number 1:')
        self.num1_label.move(20, 20)

        self.num1_input = QLineEdit(self)
        self.num1_input.move(150, 20)

        self.num2_label = QLabel(self)
        self.num2_label.setText('Enter number 2:')
        self.num2_label.move(20, 50)

        self.num2_input = QLineEdit(self)
        self.num2_input.move(150, 50)

        self.num3_label = QLabel(self)
        self.num3_label.setText('Enter number 3:')
        self.num3_label.move(20, 80)

        self.num3_input = QLineEdit(self)
        self.num3_input.move(150, 80)

        # Create the button to calculate the total and average
        self.calculate_button = QPushButton('Calculate', self)
        self.calculate_button.move(20, 120)
        self.calculate_button.clicked.connect(self.calculate)

        # Create the label to display the results
        self.result_label = QLabel(self)
        self.result_label.move(20, 160)

        # Set the size and title of the window
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Number Calculator')
        self.show()

    def calculate(self):
        # Get the input values
        num1 = float(self.num1_input.text())
        num2 = float(self.num2_input.text())
        num3 = float(self.num3_input.text())

        # Calculate the total and average
        total = num1 + num2 + num3
        average = total / 3

        # Write the results to a text file
        with open('results.txt', 'w') as file:
            file.write('Total: {}\n'.format(total))
            file.write('Average: {}'.format(average))

        # Display the results in the result_label
        self.result_label.setText('Total: {}\nAverage: {}'.format(total, average))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = NumberCalculator()
    sys.exit(app.exec_())




































#7
# Define a function to calculate the letter grade
def calculate_letter_grade(average_grade):
    if average_grade >= 90:
        return 'A'
    elif average_grade >= 80:
        return 'B'
    elif average_grade >= 70:
        return 'C'
    elif average_grade >= 60:
        return 'D'
    else:
        return 'F'


# Main program
while True:
    # Ask the user to enter their full name
    full_name = input('Enter your full name (or "q" to quit): ')
    if full_name == 'q':
        break

    try:
        # Ask the user to enter their midterm and final grades
        midterm_grade = float(input('Enter your midterm grade: '))
        final_grade = float(input('Enter your final grade: '))

        # Calculate the average grade and letter grade
        average_grade = (midterm_grade + final_grade) / 2
        letter_grade = calculate_letter_grade(average_grade)

        # Write the results to a text file
        with open('grades.txt', 'a') as file:
            file.write('{}\t{}\t{}\t{}\n'.format(full_name, midterm_grade, final_grade, letter_grade))

        # Read the contents of the file and display them
        with open('grades.txt', 'r') as file:
            contents = file.read()
            print(contents)

    except ValueError:
        print('Invalid input, please enter a number for your grades.')
































#8
import random

# Generate 10 random numbers from 1 to 10
random_numbers = [random.randint(1, 10) for _ in range(10)]

# Write the random numbers to a text file
with open('random_numbers.txt', 'w') as file:
    for number in random_numbers:
        file.write(str(number) + '\n')

# Read the contents of the file and display them
with open('random_numbers.txt', 'r') as file:
    contents = file.read()
    print(contents)
