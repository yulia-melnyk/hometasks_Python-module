
# #ДЗ
#  Створити клас rectangle
# 1) об'єкт приймає два параметри - дві сторони х у
# 2) описати методи арифметичні
#   + сума площин двок об'єктів
#   - різниця площин
# 3) логічні оператори:
#   == повертає true якщо рівні по площині
# №   != якщо не рівні
#   >, < відповідно
# 4) len() - сума сторін

class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def square(self):
        return self.x * self.y
    
    def summ_of_squares(self, other):
        return self.square() + other.square()

    def difference_of_squares(self, other):
        return self.square() - other.square()

    def __eq__(self, other):
    
        if self.square() == other.square():
            return True
        else:
            return False

    def __ne__(self, other):
        if self.square() != other.square():
            return True
        else:
            return False

    def __gt__(self, other):
        if self.square() > other.square():
            return True
        else:
            return False
    
    def __lt__(self, other):
        if self.square() < other.square():
            return True
        else:
            return False
    
    def __len__(self):
        return self.x + self.y

rectangle1 = Rectangle(3,5)
rectangle2 = Rectangle(4,5)

print('Summary square is: ', rectangle1.summ_of_squares(rectangle2))
print('Difference between squares is: ', rectangle1.difference_of_squares(rectangle2))
print('Two squares are equal: ', rectangle1 == rectangle2)
print('Two squares are not equal: ', rectangle1 != rectangle2)
print('Square of the 1st object is greater than square of the 2nd object: ', rectangle1 > rectangle2)
print('Square of the 1st object is less than square of the 2nd object: ', rectangle1 != rectangle2)
print('Summ of 2 sides is: ', len(rectangle1))

# ######################################################################

# 1)Створити пустий list 
# 2)Створити клас Letter
# 3) створити змінну класу __count.
# 4) при створенні об'єкта має створюватись змінна об'єкта(пропертя) __text, для цієї змінної мають бути гетер і сетер
# 5) при створені об'єкта __count має збільшуватися на 1
# 6) має бути метод(метод класу) для виводу __сount
# 7) має бути метод який записує в наш ліст текст з нашої змінної __text

text_value = []

class Letter:
    __count = 0

    def __init__(self):
        self.__text = ''
        Letter.__count += 1

    @property
    def new_text(self):
        return self.__text

    @new_text.setter
    def new_text(self, text):
        self.__text = text

    def save_text(self, list):
        text_value.append(self.__text)

    @classmethod
    def show_count(cls):
        print('Total number of objects: ', cls.__count)


letter = Letter()
letter.new_text = str(input('Place text here: '))
print(letter.new_text)
letter.save_text(text_value)
Letter.show_count()
print(text_value)

letter1 = Letter()
letter1.new_text = str(input('Place text here: '))
print(letter1.new_text)
letter1.save_text(text_value)
Letter.show_count()
print(text_value)

