import os
# os.system("mode con:cols=[whatever you want] lines=[whatever you want]")

os.system('color fa')

mytxt = """Hello how are you this is good for me today i'm going to my home.
my home peepliye"""
print(mytxt)
print("\n")
print("Enter the text which you want to find:")
search_txt = input()
if search_txt in mytxt:
    print("yes")
else:
    print("no")

x = input("If you want to continue then press 'y':")
if x=='y':
    os.system('cls')
    os.system('python search_text.py')
else:
    os.system('exit')
