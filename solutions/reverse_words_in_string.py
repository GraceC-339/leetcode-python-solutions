
# def reverseWords( s: str) -> str:
#     # split into a list without white space => ['the', 'sky', 'is', 'blue']
#     s=s.strip()
#     words_list = [word.strip() for word in s.split(' ')]

#     # reverse the order
#     words_list = words_list[::-1]
#     print(words_list)

#     # concateneated by a single space
#     return ' '.join(words_list)

# s = " the sky is blue "
# print(reverseWords(s))

# two pointer - fast and slow pointer => to remove the unwanted space
# use fast pointer to traverse the whole string array
# slow pointer to collect the elements we want 
# space complexity - O(1)

def reverseWords( s:str) -> str:
    words = list(s)
    print(words)

    fast, slow = 0,0

    while fast < len(s):
        if words[fast] != ' ':
            words[slow] = words[fast]
            fast += 1
            slow += 1
        
