import random

upper_char = chr(random.randint(65,90))
lower_char = chr(random.randint(97,122))

digit_one = random.randint(0,10)
digit_two = random.randint(11,20)

punc = chr(random.randint(91,96))

password = (upper_char + lower_char + str(digit_one) + str(digit_two) + punc)

print(''.join(random.sample(password,len(password))))
