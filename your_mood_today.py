import feeling


def main():
    while True:
        mood = input("Hey friend! How are you feeling today??\n").title()
        if mood == "Happy":
            feeling.happy(mood)
            break
        elif mood == 'Sad':
            feeling.sad(mood)
            break
        elif mood == 'Excited':
            feeling.excited(mood)
            break
        elif mood == "Anxious":
            feeling.anxious(mood)
            break
        else:
            print('Lets try again with your feelings')
            continue

main()
