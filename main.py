table = int(input("Enter the number: "))
fileName = "output.txt"
with open(fileName, "w") as file:
    file.write(f"Multiplication Table of {table}\n")
    for i in range(10):
        file.write(f"{table} X {i} = {table*i}\n")
print(f"Multiplication table of {table} printed to {fileName}")