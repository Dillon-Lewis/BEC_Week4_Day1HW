def happy(mood):
    print("Thats amazing to hear! Keep it up!")

def sad(mood):
    helping = input("I'm sorry to hear that, do you want to talk about it at all?\n").title()
    if helping == "Yes":
        print("Well I am all ears so lets chat <3")
    elif helping == 'No':
        print("I am always here if you need anything!")
        return
    
def excited(mood):
    print('Thats awesome I am so happy for you!!')

def anxious(mood):
    print("I am so sorry to hear that, keep your head up and breath! You are stronger then the anxiety")
    