word = "supercalifragilisticexpialidocious"
for c in word:
    print(c)
print("*" * 50)
idx  = 0
while idx < len(word):
    print(word[idx])
    idx += 1
print("*" * 100)
n=100
while n<140:
    n+=2
    print(n)
print("*" * 1000)
for I in range(100,142,2):
    print (I)
print("*" * 100)
value = input("enter pass :")
word = "hello"
while value != word:
    value = input("enter pass :")
    if value == word:
        print("Thank you")
  
print("*" * 100)
for letter in "supercalifragilisticexpialidious":
    if letter == 'c':
        break
    print(letter)
print("*" * 100)
for letter in "supercalifragilisticexpialidious":
    if letter == 'aeiou':
        continue
    print(letter)