#Python program that accepts a 10 digit mobile number, and find the digits which are absent in a given mobile number

mobile = input('Please enter a mobile number: ' )
all = '0123456789'
print('Missing digits are ', set(all) - set(mobile))