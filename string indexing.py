# indexing = accessing element of sequence of sequence using [] (indexing operator )
#                          [start: end: step]

#[sart: End]
credit_number = "1234-5678-9012-3456"
last_digits = credit_number[-4:]
print(credit_number[0]) #[1]  [2] [another number]
print(credit_number[0:4]) # [start : end]
print(credit_number[4 : 9])  # 5= 1234- 9= 5678
print(credit_number[5:])
print(credit_number[-1])

#[:step] print every second charecter 
print(credit_number[: : 3])
print(f"XXXX-XXXX-XXXX-{last_digits}")
credit_number= credit_number[::-1] #reverse method 
print(credit_number)