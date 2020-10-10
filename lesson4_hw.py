# #ДЗ
# 1)-написать lambda функцию, которая находит среднее арифметическое значение входных аргументов, этих входных аргументов может быть сколько угодно

average = lambda *args: sum(args) / len(args)

# print(average(2,6,5,7,10))

# 2)-написать lambda функцию которая принимает строку и возвращает лист слов, при этом каждое слово это лист его букв:
# к примеру:
#  "Hello from owu"=> [['H', 'e', 'l', 'l', 'o'], ['f', 'r', 'o', 'm'], ['o', 'w', 'u']]


# str = input('Enter the text: ')
# print((lambda str: [list(symbol) for symbol in str.split()])(str))
 
# 3)создать два класса Owner и Pet(можете добавить еще свои поля):

# у владельца должны быть такие методы:
# -добавить питомца
# -удалить питомца
# -показать всех питомцев
# -показать питомцев по типу
class Owner:
    def __init__(self, name, age, city, pets=[]):
        self.name = name
        self.age = age
        self.city = city
        self.pets = pets

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)
    
    def add_pet(self, pet_name, pet_age, pet_animal_type):
        self.pets.append(Pet(pet_name, pet_age, pet_animal_type))

    def delete_pet(self, pets_index):
        del self.pets[pets_index]
    
    def show_all_pets(self):
            for i in range(len(self.pets)):
                print(i + 1, end='.')
                for o, p in self.pets[i].__dict__.items():
                    print(f'{o}: {p}', end=' ')
                print()

class Pet:
    def __init__(self, name, age, animal_type):
        self.name = name
        self.age = age
        self.animal_type = animal_type
    
    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)
        
# owner1 = Owner('Yulia', 24, 'Lviv', 'dog')
# pet1 = Pet('Nora', 8, 'dog')

# owner1.add_pet('Nika', 2, 'cat')
# owner1.delete_pet(0)
# owner1.show_all_pets()
# print(owner1, pet1)



# 4) создать реестр владельцев и питомцев + создать меню:
# -добавить владельца
# -удалить владельца
# -показать всех владельцев
# -показать всех владельцев и их питомцев
# -выбрать владельца:
#       -добавить питомца
#       -удалить питомца
#       -показать всех питомцев
#       -показать питомцев по типу ####

main_menu_text = '''Selecting owner menu:
1) add owner
2) remove owner
3) show all owners
4) show all owners with pets
5) choose owner:
0) exit
'''
owners_menu_text = '''Owner`s profile changing menu:
1) add pet
2) remove pet
3) show all pets
4) show all pets by type
0) exit'''
def sub_menu(owners, available_animal_types):

    while True:
        print('Select owner:')
        for index in range(len(owners)):
            print(f'{index} -- {owners[index].name}')
        current_owners_choice = owners[int(input(''))]
        if current_owners_choice in owners:
            print(owners_menu_text)
            pets_menu_choice = int(input('Choose an owner`s option:'))
            if pets_menu_choice == 1:
                name = str(input('Enter pet`s name:'))
                age = None
                while not age:
                    age = input_age()
                    for index in range(len(available_animal_types)):
                        print(f'{index} -- {available_animal_types[index]}')
                animal_type = available_animal_types[int(input('Enter the number of your pet`s type from this list:'))]
                if animal_type in available_animal_types:
                    current_owners_choice.pets.append(Pet(name, age, animal_type))
                else:
                    print('Your pet`s type doesn`t exist!')

            elif pets_menu_choice == 2:
                for i in range(len(current_owners_choice.pets)):
                    print(f'{i} -- {current_owners_choice.pets[i].name}')
                    chosen_pet = int(input('Choose pet to remove: '))
                    try:
                        current_owners_choice.pets.remove(current_owners_choice.pets[chosen_pet])
                    except:
                        print('Incorrect pet`s number!')
            elif pets_menu_choice == 3:
                print(f'Owner`s pets: {current_owners_choice.pets}')
            elif pets_menu_choice == 4:
                for item in current_owners_choice.pets:
                    print(f'Pet`s name {item.name}, Pet`s age: {item.age}, Pet`s type: {item.animal_type}')
            elif pets_menu_choice == 0:
                break

def input_age():
    try:
        return int(input('Enter your age:'))
    except ValueError:
        print('Oops! Field "Age" should be a numerical value.Try again')
        return None

def pets_and_owners_menu():
    owners = []
    pets = []
    available_animal_types = ['dog', 'cat', 'bird', 'rabbit', 'turtle', 'hamster', 'mouse', 'guinea pig', 'fish', 'reptile']

    while True:
        print(main_menu_text)
        choice_1= int(input('Choose an option:'))
        if choice_1 == 1:
            name = str(input('Enter your name:'))
            age = None
            while not age:
                age = input_age()
            city = str(input('Enter your city:'))
            
            owners.append(Owner(name, age, city))
        elif choice_1 == 2:
            for i in range(len(owners)):
                print(f'{i} -- {owners[i].name}')
            chosen_user = int(input('Choose owner: '))
            try:
                owners.remove(owners[chosen_user])
            except:
                print('Incorrect owner!')
        elif choice_1 == 3:
            for item in owners:
                print(f'Owner`s name {item.name}, Owner`s age: {item.age}, Owner`s city: {item.city}')
        
        elif choice_1 == 4:
            for item in owners:
                print(f'Owner`s name {item.name}, Owner`s age: {item.age}, Owner`s city: {item.city}, Owner`s pets: {item.pets}')

        elif choice_1 == 5:
            sub_menu(owners, available_animal_types)
        elif choice_1 == 0:
            break

pets_and_owners_menu()

                