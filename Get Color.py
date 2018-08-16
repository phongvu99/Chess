## Chess

def getcolor():
        color = ""
        x = True
        position_char_1 = ["A", "C", "E", "G"]
        position_char_2 = ["B", "D", "F", "H"]
        position_odd = [1, 3, 5, 7]
        position_even = [2, 4, 6, 8]
        position_char = raw_input("Input your position character: ")
        position_number = input("Input your character number: ")
        while x:
                if position_char in position_char_1:
                        if position_number in position_odd:
                                color = "Black"
                                x = False
                                return color
                        else:
                                color = "White"
                                x = False
                                return color
                else:
                        if position_number in position_odd:
                                color = "White"
                                x = False
                                return color
                        else:
                                color = "Black"
                                x = False
                                return color
