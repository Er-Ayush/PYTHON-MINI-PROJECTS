# this create a dictionary of key value pairs where key represents roman numeral and value represent decimal equivalent
roman_list = {
  "I":  1,
  "V":  5,
  "X": 10,
  "L": 50,
  "C": 100,
  "D": 500,
  "M": 1000,
}
# this function is used to convert a roman number to decimal
# it takesroman number and check the adjacent position ...and then rest you can see the logic
def convertion_function(roman_number):
    sum = 0
    for i in range(len(roman_number) - 1):
        left = roman_number[i]
        right = roman_number[i + 1]
        if roman_list[left] < roman_list[right]:
            sum -= roman_list[left]
        else:
            sum += roman_list[left]
    sum += roman_list[roman_number[-1]]
    print(sum)
 

#  taking input
roman_number=input("enter roman string:")

# function call
convertion_function(roman_number)
