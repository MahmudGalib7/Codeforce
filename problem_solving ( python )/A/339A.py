input_str = input().strip()
numbers = input_str.split('+')
numbers = list(map(int, numbers))
numbers.sort()
output_str = "+".join(map(str, numbers))
print(output_str)
