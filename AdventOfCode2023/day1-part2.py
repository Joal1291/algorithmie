import openfile

array = [
"two1nine",
"eightwothree",
"abcone2threexyz",
"xtwone3four",
"4nineeightseven2",
"zoneight234",
"7pqrstsixteen",
]

def sumNumberInAWord(array):
    concatDigit = ""
    result_to_return = 0

    for word in array:
        for char in word:
            if char.isdigit():
                concatDigit += char
        
        concatDigit = concatDigit[0] + concatDigit[-1:]
        result_to_return += int(concatDigit)
        concatDigit = ""
    
    print(result_to_return)

sumNumberInAWord(array)