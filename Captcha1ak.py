import random
from captcha.image import ImageCaptcha
lowercase = "qwertyuioplkjhgfdsazxcvbnm"
uppercase = "QWERTYUIOPKJHGFDSAZXCVBNM"
numb1 = "0123456789"
cap_img = uppercase + lowercase + numb1
length1 = random.randrange(5, 7)
random_captcha = " ".join(random.sample(cap_img, length1))
image = ImageCaptcha(width=500, height=200)
captcha_text = random_captcha
data = image.generate(captcha_text)
image.write(captcha_text, 'CAPTCHA.png')
print("Please add space between the characters")
input1 = input("Enter the Captcha\n")
if random_captcha == input1:
    print("True")
else:
    print("False")
