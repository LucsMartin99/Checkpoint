#"Day in the Life"

welcome = input('Welcome to "A Day in the Life". Type "S" to start playing or "E" to exit ==> ')

while welcome == 'S' or welcome == 's':
    main_character = input("Name your character ==> ")
    print(f"A Day in the Life of {main_character}:")
    print(f"10:00 am - It is a cold Friday morning; {main_character} is sleeping peacefully when suddenly, they get a call from the office.")
    call_1 = input("A = Answer // R = Reject ==> " )
    if call_1 == 'A' or call_1 == 'a':
        print(f'"Good morning, {main_character}. It\'s Bob, remember? Your boss. Or at least, I was until you decided not to come to work this morning. You should have been here at 8. Don\'t bother coming now. You are fired!"')
        print(f"Damn it, {main_character}! You just lost your job. What are you going to do?")
        decision_1 = input("A = Go back to sleep // B = Go look for a new job ==> ")
        if decision_1 == 'A' or decision_1 == 'a':
            print('You died in your sleep. Maybe you deserved it. RIP.')
            welcome = input('Welcome to "A Day in the Life". Type "S" to start playing or "E" to exit ==> ')
        elif decision_1 == 'B' or decision_1 == 'b':
            print("Okay! New job, new life. Let's go get it!")
            print("3:00 pm - After a long morning, you some how managed to get two job interviews. Unfortunately, they are both at the same time. Which job are you trying to apply for?")
            decision_2 = input("A = Taxi Driver // B = Gardener ==> ")
            if decision_2 == "A" or decision_2 == "a":
                print("Okay, good luck!")
                print("6:00 pm - INTERVIEW")
                print(f"INTERVIEWER: So you are {main_character}, right? Let's get this over with.")
                print("INTERVIEWER: Do you have a driving license?")
                taxi_1 = input("A = Yes // B = No ==> ")
                if taxi_1 == "B" or taxi_1 == "b":
                    print("INTERVIEWER: Okay, we'll call you. Thanks for stopping by!")
                    enterview = False
                elif taxi_1 == "A" or taxi_1 == "a":
                    print("INTERVIEWER: Do you have your own car?")
                    taxi_2 = input("A = Yes(truth) // B = No(lie) ==> ")
                    if taxi_2 == "B" or taxi_2 == "b":
                        print("INTERVIEWER: Okay, we'll call you. Thanks for stopping by!")
                        enterview = False
                    elif taxi_2 == "A" or taxi_2 == "a":            
                        print("INTERVIEWER: Why would you like to work for our agency?")
                        taxi_3 = input("A = I just love the idea of driving around the city. // B = I need money, obviously. ==> ")
                        if taxi_3 == "A" or taxi_3 == "a":
                            print("INTERVIEWER: Okay, we'll call you. Thanks for stopping by!")
                            enterview = False
                        elif taxi_3 == "B" or taxi_3 == "b":
                            print("INTERVIEWER: Well, the money you can make here will depend on how many hours and the distance you drive. It is a minimum of 6 hours, and the agency keeps 20% of the gains.")
                            print("INTERVIEWER: I believe we have all we need. See you on Monday.")
                            enterview = True
            elif decision_2 == "B" or decision_2 == "b":
                print("Okay, good luck!")
                print("6:00 pm - INTERVIEW")
                print(f"INTERVIEWER: Hello, {main_character}, glad to meet you. My family and I really needed a gardener. Let's begin with the interview.")
                print("INTERVIEWER: Do you have a criminal record?")
                gardener_1 = input("A = Yes // B = No ==> ")
                if gardener_1 == "A" or gardener_1 == "a":
                    print("INTERVIEWER: Okay, we'll call you. Thanks for stopping by!")
                    enterview = False
                elif gardener_1 == "B" or gardener_1 == "b":
                    print("INTERVIEWER: Could you tell me what your weaknesses are?")
                    gardener_2 = input("A = I've had a shoulder injury since I was 20.  //  B = I work too hard ==> ")
                    if gardener_2 == "A" or gardener_2 == "a":
                        print("INTERVIEWER: Okay, we'll call you. Thanks for stopping by!")
                        enterview = False
                    elif gardener_2 == "B" or gardener_2 == "b":
                        print("INTERVIEWER: Sure you do!")
                        print("INTERVIEWER: Why do you want to work for me?")
                        gardener_3 = input("A = I don't know you, I just need your money.  //  B = It would be a great honor for me, sir. ==> ")
                        if gardener_3 == "A" or gardener_3 == "a":
                            print("INTERVIEWER: Okay, we'll call you. Thanks for stopping by!")
                            enterview = False
                        elif gardener_3 == "B" or gardener_3 == "b":
                            print("INTERVIEWER: I believe we have all we need. See you on Monday.")
                            enterview = True
            if enterview == False:
                print(f"7:00 pm - Well, {main_character}, there is no way you get that job. At least you tried, right? Let's go get a bite.")
            else:
                print(f"Well done, {main_character}! You got the job! Who said you were useless?")
                print("7:00 pm - You have the rest of the day off. What are you doing now?")
            decision_3 = input("A = Go home and relax // B = Hang out with buddy ==> ")
            if decision_3 == "A" or decision_3 == "a":
                print("I guess we call it a day then. Okay!")
                print(f"{main_character} got some food at the drive-thru and went home to relax after a long and disappointing day.")
                print("Thank you for playing! Come back anytime.")
                welcome = input('Welcome to "A Day in the Life". Type "S" to start playing or "E" to exit ==> ')
            elif decision_3 == "B" or decision_3 == "b":
                print("7:00 pm - Hanging out with your buddy sounds like a great idea!")
                print("You and your buddy decide to grab some drinks at a local bar.")
                print("10:00 pm - After a few drinks, you start feeling more relaxed and forget about the job interviews.")
                print("As you head home, you come across a mysterious alley. Do you want to explore it?")
                decision_4 = input("A = Explore the alley // B = Go straight home ==> ")
                if decision_4 == "A" or decision_4 == "a":
                    print("The alley is dimly lit, and you hear strange noises. Suddenly, you encounter a mysterious figure.")
                    print("This mysterious figure turns out to be a wizard who offers you a magical opportunity.")
                    print("He can either give you a chance to undo your bad day or grant you a mysterious power.")
                    decision_5 = input("A = Undo the bad day // B = Accept the mysterious power ==> ")
                    if decision_5 == "A" or decision_5 == "a":
                        print("The wizard waves his wand, and you find yourself back in bed at 10:00 am.")
                        print("It's a second chance! Make better decisions this time.")
                        welcome = input('Welcome to "A Day in the Life". Type "S" to start playing or "E" to exit ==> ')
                    elif decision_5 == "B" or decision_5 == "b":
                        print("You accept the mysterious power. The wizard grants you the ability to predict the future.")
                        print("With your newfound power, you navigate through life making better decisions.")
                        print("Congratulations! You've achieved a mystical ending.")
                        welcome = input('Welcome to "A Day in the Life". Type "S" to start playing or "E" to exit ==> ')
                elif decision_4 == "B" or decision_4 == "b":
                    print(f"You decide to go straight home and call it a day, {main_character}.")
                    print(f"{main_character} reflects on the events of the day and decides to make better choices tomorrow.")
                    print("Thank you for playing! Come back anytime.")
                    welcome = input('Welcome to "A Day in the Life". Type "S" to start playing or "E" to exit ==> ')                
        else:
            print("Is it too hard to choose A or B?")
    elif call_1 == 'R' or call_1 == 'r':
        print("12:00 pm - Dude! You should have been at work four hours ago! What is wrong with you?")
        print(f"{main_character} scrambles to get ready for work as quickly as possible and sprints to the car.")
        print(f"On your way to work, you notice there's been a crash on the highway, so you'll have to take the long way to work.")
        print(f"1:00 pm - There is your boss, he doesn't seem happy. You're probably screwed, but maybe you can try something.")
        decision_01 = input("A = Pretend not to see him and lock in your office // B = Apologize ==> ")
        if decision_01 == 'A' or decision_01 == 'a':
            print("You decide to avoid the awkward confrontation with your boss and head straight to your office.")
            print(f"Locked in your office, you browse social media, pretending to be busy. Productivity level: expert.")
            decision_02 = input("A = Take a long 'bathroom break' // B = Finally start working ==> ")
            if decision_02 == 'A' or decision_02 == 'a':
                print("You decide to take an extended 'bathroom break' to kill some time.")
                print(f"When you return, your boss gives you a disapproving look, but hey, you've mastered the art of office evasion.")
            elif decision_02 == 'B' or decision_02 == 'b':
                print("You finally decide to start working, proving that you can be productive when you want to be.")
                print(f"Your boss seems momentarily impressed. Maybe this day won't be a complete disaster after all.")
        elif decision_01 == 'B' or decision_01 == 'b':
            print(f"You take a deep breath and decide to apologize sincerely to your boss.")
            print(f"BOSS: {main_character}, this is becoming a habit. You need to get your act together!")
            decision_03 = input("A = Promise to improve // B = Blame the traffic ==> ")
            if decision_03 == 'A' or decision_03 == 'a':
                print(f"You promise your boss that you'll improve and become the model employee. Time to turn over a new leaf.")
                print("Let's see if you can keep this promise.")
            elif decision_03 == 'B' or decision_03 == 'b':
                print("You blame the traffic for your tardiness, hoping it'll be a good excuse.")
                print(f"BOSS: Traffic is not a valid excuse every day, {main_character}. This is your final warning!")
        print("4:00 pm - The workday finally ends, but your day is far from over.")
        print("6:00 pm - As you leave the office, you encounter a colleague who invites you to an after-work gathering at a nearby cafe.")
        decision_04 = input("A = Join them for a quick drink // B = Decline and head home ==> ")
        if decision_04 == 'A' or decision_04 == 'a':
            print("You decide to join your colleagues for a quick drink.")
            print("The gathering turns into an unexpectedly fun evening, and you lose track of time.")
            print(f"10:00 pm - You finally decide to head home, realizing you've had a much-needed break from the daily grind.")
            print("On your way home, you come across a stray kitten stuck in a tree. You hear it meowing for help.")
            decision_05 = input("A = Ignore the kitten and keep walking // B = Attempt to rescue the kitten ==> ")
            if decision_05 == 'A' or decision_05 == 'a':
                print("You decide to ignore the kitten and keep walking. It's just a cat, right?")
                print("The next day, you see a news report about a local superhero saving a kitten from a tree. You missed your chance to be a hero!")
            elif decision_05 == 'B' or decision_05 == 'b':
                print("You decide to attempt to rescue the kitten, channeling your inner superhero.")
                print("You climb the tree, grab the kitten, and safely bring it down.")
                print("As you walk away, a mysterious figure in the shadows applauds your heroic act.")
                print(f"The mysterious figure approaches you and reveals they are a talent scout for a superhero agency.")
                print("They offer you the chance to become a real-life superhero!")
                decision_06 = input("A = Accept the offer and become a superhero // B = Decline the offer ==> ")
                if decision_06 == 'A' or decision_06 == 'a':
                    print("You accept the offer and embark on a new career as a superhero.")
                    print(f"{main_character}, the unexpected hero, begins a life of crime-fighting and adventure.")
                    print("Congratulations! You've achieved a superhero ending.")
                elif decision_06 == 'B' or decision_06 == 'b':
                    print("You decline the offer, thinking being a superhero is too much responsibility.")
                    print("The mysterious figure disappears into the shadows, leaving you to continue your ordinary life.")
                    print("You missed the chance to become a superhero. Maybe next time!")
        elif decision_04 == 'B' or decision_04 == 'b':
            print("You decline the invitation and head straight home.")
            print(f"At home, you have a relaxing evening, catching up on your favorite TV shows.")
            print("8:00 pm - It's been a chill evening, and you're ready to call it a day.")
            print("While watching TV, you come across a news report about a local charity event in need of volunteers.")
            decision_07 = input("A = Ignore the charity event // B = Volunteer for the event ==> ")
            if decision_07 == 'A' or decision_07 == 'a':
                print("You decide to ignore the charity event and continue watching TV. There's always another time to help, right?")
                print("Little do you know, the charity event needed more volunteers, and your absence made a significant impact on its success.")
                print("The next day, your friends share stories about the great time they had at the charity event, and you're left feeling a bit left out.")
                welcome = input('Welcome to "A Day in the Life". Type "S" to start playing or "E" to exit ==> ')
            elif decision_07 == 'B' or decision_07 == 'b':
                print("You decide to volunteer for the charity event, embracing the opportunity to make a positive impact on your community.")
                print(f"At the event, you meet new people, make a difference, and even discover a hidden talent for organizing activities.")
                print("The local news covers the charity event, highlighting the selfless volunteers who made it successful.")
                print(f"{main_character}, the unsung hero, receives recognition for their contributions to the community.")
                welcome = input('Welcome to "A Day in the Life". Type "S" to start playing or "E" to exit ==> ')
if welcome == 'E' or welcome == 'e':
    print('Thanks for stopping by!')
else:
    print('Wrong input! You might want to reconsider your life choices.')
