# Function to calculate the sum, difference, multiplication, and division of two integers
def sum_and_difference(a, b):
    return a + b, a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"  # Zero division error handling
    return a / b

# User input for two integers
a = int(input("첫번째 정수를 입력해주세요: "))
b = int(input("두번째 정수를 입력해주세요: "))

# Calculating sum and difference
sum_value, diff_value = sum_and_difference(a, b)
# Calculating multiplication and division
mult_value = multiply(a, b)
div_value = divide(a, b)

# Output results
print(f"{a}와 {b}를 더한 값은: {sum_value}")
print(f"{a}에서 {b}를 뺀 값은: {diff_value}")
print(f"{a}와 {b}를 곱한 값은: {mult_value}")
print(f"{a}를 {b}로 나눈 값은: {div_value}")
