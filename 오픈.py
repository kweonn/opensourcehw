def sum_and_difference(a, b):
    return a + b, a - b

def multiply(a, b):
    return a * b  # 원래 곱셈 기능으로 수정

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"  # 0으로 나누는것은 불가
    return a / b

# User input for two integers
a = int(input("첫번째 정수를 입력해주세요: "))
b = int(input("두번째 정수를 입력해주세요: "))


sum_value, diff_value = sum_and_difference(a, b)

mult_value = multiply(a, b)
div_value = divide(a, b)

# Output results
print(f"{a}와 {b}를 더한 값은: {sum_value}")
print(f"{a}에서 {b}를 뺀 값은: {diff_value}")
print(f"{a}와 {b}를 곱한 값은: {mult_value}")
print(f"{a}를 {b}로 나눈 값은: {div_value}")
