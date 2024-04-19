# Function to calculate the average of a list of numbers
def calculate_average(numbers):
    for number in numbers:
        total = 0                       # This line might be incorrect
        total += number
    average = total / len(numbers)
    return average

# Main function
def main():
    numbers = [5, 10, 15, 20, 25]  
    average = calculate_average(numbers)
    print("Average: ", average)
    print("Expected: 15.0")

main()