import random
def out_blue(text):
    print("\033[34m{}\033[0m".format(text))
def out_red(text):
    print("\033[31m{}\033[0m".format(text))
def out_yellow(text):
    print("\033[33m{}\033[0m".format(text))
def out_green(text):
    print("\033[32m{}\033[0m".format(text))
def out_purple(text):
    print("\033[35m{}\033[0m".format(text))

out_yellow("\nУ сутінках, коли місто вже засинало, помічник, вдягнувши звичайний одяг та надійшовши до міста, рушив у свою небезпечну подорож. Його завдання було важливим – отримати таємне послання від шпигуна, який, прикритий маскою звичайного жителя, приховувався в цьому місті."+
    "\nМісто, освітлене вогнями вікон та вуличними фонарями, здавалося зовсім іншим світом у порівнянні з дикою природою, з якою він зазвичай стикався. Із зачепками вітру та переповненими вулицями, помічник знаходився в незнайомому середовищі, але його місія була надзвичайно важливою.\n"+
    "Його завданням було знайти шпигуна та промовити йому таємний код (Валар Маргуліс) для отримання послання \n"+
    "Після кількох днів слідкування він так і не знайшов таємного шпигуна ,тому він вирішив діяти на свій страх і ризик\n"+
    "Наш помічник ,переодягнувшись у звичайного жителя, вирушив на пошуки шпигуна на околицях міста")


SuccessMision=False
TryCounter=0
while SuccessMision==True or TryCounter<=5:
    TryCounter+=1
    RandomCitizen=random.randint(1,4)

    out_yellow(f"\nПідійшовши до {TryCounter} мешканця міста він промовив  ")
    SecretCode=input("\n-Привіт. Я сподіваюсь ти той кого я шукаю ,мій секретний код : ")
    if "Валар Маргуліс" in SecretCode and RandomCitizen==3:
        out_green("-Валар де Хейріс! \n-Хвала богам ти мене знайшов ,я вже почав хвилюватися щодо нашого звдання \n-Ось тримай, таємне послання. Тільки пам'ятай, бережи його як зіницю ока")
        out_yellow("\nПовертаючись до своєї бази, помічник знав, що ця подорож була дійсно небезпечною, але вона була варта зусиль.\nТаємне послання в руках команди,яке тепер дозволило розкрити важливі секрети та виправдати ризики, які він поклав на виконання цього завдання")
        SuccessMision=True
        break
    elif RandomCitizen==3:
        out_green("-Друже що ти таке мелеш?")
        print("-Вибач не бери в голову")  
    elif RandomCitizen==4:
        out_purple("-Друже що ти таке мелеш?")
        print("-Вибач не бери в голову")  
    else: 
        out_blue("-Друже що ти таке мелеш?")
        print("-Вибач не бери в голову")
else:
    print("\n-Хух, досить на сьогодні. Час залягти на дно ,щоб не привертати надто багато уваги")
    out_yellow("Помічник, щоб не викликати надто багато підозр, почав працювати у тіні...")
if (SuccessMision==False) :
    out_yellow("\nЗавдання виявилось надзвичайно не легким\nТому він вирішив спробувати знову вийти у світ")
    while SuccessMision==True or TryCounter<=10:
        TryCounter+=1
        RandomCitizen=random.randint(1,2)

        out_yellow(f"\n-Підійшовши до {TryCounter} мешканця міста він промовив секретний код: ")
        SecretCode=input("\nПривіт. Я сподіваюсь ти той кого я шукаю ,мій секретний код : ")
        if "Валар Маргуліс" in SecretCode and RandomCitizen==2:
            out_green("-Валар де Хейріс! \n-Хвала богам ти мене знайшов ,я вже почав хвилюватися щодо нашого звдання \n-Ось тримай, таємне послання. Тільки пам'ятай, бережи його як зіницю ока")
            out_yellow("\nПовертаючись до своєї бази, помічник знав, що ця подорож була дійсно небезпечною, але вона була варта зусиль.\nТаємне послання в руках команди,яке тепер дозволило розкрити важливі секрети та виправдати ризики, які він поклав на виконання цього завдання")
            SuccessMision==True
            break
            
        elif RandomCitizen==2:
            out_green("-Друже що ти таке мелеш?")
            print("-Вибач не бери в голову")  
        else: 
            out_blue("-Друже що ти таке мелеш?")
            print("-Вибач не бери в голову")
    else:
        out_yellow("\nЧас на виконання завдання швидко минав \nЙшли дні і ночі але все ж помічник не зміг знайти "+"\033[32m{}\033[0m".format("секретного шпигуна "))
        out_red("Завдання провалене!")


#Bool ="чоловіче" not in massage
#print(Bool)