roman_num = {
    "A" : 1,
    "B" : 5,
    "Z" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "R" : 1000
}

input_cal = "RCRZCAB"
total = 0
count = 0

while count <= len(input_cal) - 1:
    next = 1 if count + 1 <= len(input_cal) - 1 else 0
    if roman_num[input_cal[count]] < roman_num[input_cal[count + next]]:      
        total = total + (roman_num[input_cal[count + next]] - roman_num[input_cal[count]])
        count+=1
    else :
        total+=roman_num[input_cal[count]]
    count+=1
    
print(total)
