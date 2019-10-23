# Given: A string of length at most 10000 letters.
#
# Return: How many times any word occurred in string. Each letter case (upper or lower) in word matters. Lines in output can be in any order.
# Sample Dataset: We tried list and we tried dicts also we tried Zen
# Sample Output: and 1 We 1 tried 3 dicts 1 list 1 we 2 also 1 Zen 1
#
# Hints:
#
# To iterate over words in string you can split it by space:
# for word in str.split(' '): print(word)
# To have nice output of dictionary you can use .items() method:
# for key, value in dict.items(): print(key) print(value)

def count_occurance(stringval):
    dlist = {}
    for word in stringval.split(' '):
        if word in dlist:
            dlist[word] += 1
        else:
            dlist[word] = 1

    for key, value in dlist.items():
        print(key, value )


count_occurance('When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be')
