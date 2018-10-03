#! /bin/python

def shift(letter,n):
        if ord(letter) + n > 127:
                A=ord(letter)+n
                B=A-127
                shifted_letter=chr((ord(letter) + n) - 127)
        else:
                shifted_letter=chr(ord(letter) + n)
        return(shifted_letter)
        
def join_string(list_string):
        string=''.join(list_string)
        return string

word=""

for y in range (0, 128):
        list=[]
        for x in range(len(word)):
                list.append(shift(word[x],y))
        print join_string(list)
