def swap(input1, input2):
  print("BEFORE swapping")
  print(f"input1: {input1}, input2: {input2}\n")

  #step 1: save the value of input2 into a temp variable
  temporary_variable = input2

  #step 2: overwrite the old value stored in input2 with value of input1
  input2 = input1

  #step 3: overwrite the old value stored in input1 with saved value in the temp variable
  input1 = temporary_variable

  print("AFTER swapping")
  print(f"input1: {input1}, input2: {input2}\n")

  return None

#example1
in1 = 12345
in2 = 67890
swap(in1, in2)

#for extra credit, if we do a print of in1 and in2 on this line in the code, 
#what are the values? are they still swapped? is this expected behavior?
print("RETURNING from calling/invoking swap function, do in1 and in2 stay swapped after returning from the swap function?")
print(f"in1: {in1}, in2: {in2}\n")
# we can use the 'global' keyword to make the scope of the variable global when we declare the variable, instead of local/lexical scope

#example2
in1 = "apple"
in2 = "orange"
swap(in1, in2)

#for python, since swapping is so common, they created a syntax shorcut
def swap2(input1, input2):
  return input2, input1

#example3
in1 = "Python"
in2 = "JavaScript"
print(f"before swap... in1: {in1}, in2: {in2}")
in1, in2 = swap(in1, in2)
print(f"after swap... in1: {in1}, in2: {in2}")





