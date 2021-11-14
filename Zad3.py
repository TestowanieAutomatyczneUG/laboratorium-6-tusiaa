class song:
    def write(self, a = "undefined", b = "undefined"):

        if (type(a) == int and a < 0) or (type(b) == int and b < 0):
            raise Exception("Should be greater than 0")
        if (type(a) == int and a > 12) or (type(b) == int and b > 12):
            raise Exception("Should be less than 13")
        if a != "undefined" and b != "undefined":
            if (type(a) != int or type(b) != int) and \
                (type(a) == bool or type(b) == bool or
                (int(a) != a and type(a) == float) or \
                (int(b) != b and type(b) == float) or \
                (int(a) != float(a) and a.isnumeric() == True) or \
                (int(b) != float(b) and b.isnumeric() == True)):
                raise Exception("Wrong type")
        if a != "undefined":
            if type(a) != int and ( type(a) == bool or \
                (int(a) != a and type(a) == float) or \
                (int(a) != float(a) and a.isnumeric() == True)):
                raise Exception("Wrong type")

        items = [
            "and a Partridge in a Pear Tree.",
            "two Turtle Doves, ", 
            "three French Hens, ",
            "four Calling Birds, ",
            "five Gold Rings, ",
            "six Geese-a-Laying, ",
            "seven Swans-a-Swimming, ",
            "eight Maids-a-Milking, ",
            "nine Ladies Dancing, ",
            "ten Lords-a-Leaping, ",
            "eleven Pipers Piping, ",
            "twelve Drummers Drumming, "
            ]
        numbers = ["first", "second", "third", "fourth", "fifth", "sixth",
        "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
        wynik = ""

        if a == "undefined":
            wynik = "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.\n"
            for i in range(1, 12):
                wynik = wynik + "On the " + numbers[i] + " day of Christmas my true love gave to me: "
                for j in range(i, -1, -1):
                    wynik = wynik + items[j]
                wynik = wynik + "\n"

        elif b == "undefined":
            a = int(a)
            if a == 0:
                wynik = ""
            elif a == 1:
                wynik = "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree."
            else:
                wynik = wynik + "On the " + numbers[a-1] + " day of Christmas my true love gave to me: "
                for j in range(a-1, -1, -1):
                    wynik = wynik + items[j]

        else:
            a = int(a)
            b = int(b)
            if a < b:
                if a <= 1:
                    wynik = "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.\n"
                for i in range(a-1, b):
                    wynik = wynik + "On the " + numbers[i] + " day of Christmas my true love gave to me: "
                    for j in range(i, -1, -1):
                        wynik = wynik + items[j]
                    wynik = wynik + "\n"
            else:
                if b <= 1:
                    wynik = "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.\n"
                for i in range(b-1, a):
                    wynik = wynik + "On the " + numbers[i] + " day of Christmas my true love gave to me: "
                    for j in range(i, -1, -1):
                        wynik = wynik + items[j]
                    wynik = wynik + "\n"

        return wynik