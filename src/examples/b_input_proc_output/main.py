import input_process_output

value = input("Enter value: ")
result = input_process_output.add_values(value, value)
print(result)

value = input("Enter value: ")
result = input_process_output.add_values(int(value), int(value))
print(result)

value = input("Enter value: ")
result = input_process_output.add_values(float(value), float(value))
print(result)

