import openfile

filename = "day1_part2.txt"
exerciceArray = openfile.readFile(filename)

arraytest = [
"two1nine",
"eightwothree",
"abcone2threexyz",
"xtwone3four",
"4nineeightseven2",
"zoneight234",
"7pqrstsixteen",
]

def lookForDigit(dictNumbers, arrayNumber, way: bool, line):
    string = ""
    lineToLookFor = line if way else line[::-1]
    for char in lineToLookFor:
        if char.isdigit():
            return char
        else:
            if way:string += char
            else:string= char + string
            
            for number in arrayNumber:
                if number in string:
                    return str(dictNumbers[number])

def sumNumberInAWord(array):
    numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    arraynumber = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    concat = ""
    result = 0

    for line in array:
        concat += lookForDigit(numbers, arraynumber, True, line) + lookForDigit(numbers, arraynumber, False, line)
        result += int(concat)
        concat = ""

    print("res", result)

sumNumberInAWord(exerciceArray)