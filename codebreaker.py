
from dataclasses import replace
from itertools import count
from tkinter.tix import WINDOW
from xml.dom.pulldom import CHARACTERS
from pprint import pprint

# capitalletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# letters = "abcdefghijklmnopqrstuvwxyz"
# numbers = "0123456789"
print("")
print(''''
╭━━━╮╭━━━╮╭━━━╮╱╱╱╱╭╮╱╱╭━━╮╱╱╱╱╱╱╱╱╭╮
┃╭━╮┃┃╭━╮┃┃╭━╮┃╱╱╱╱┃┃╱╱┃╭╮┃╱╱╱╱╱╱╱╱┃┃
┃┃╱┃┃┃┃╱┃┃┃┃╱╰╋━━┳━╯┣━━┫╰╯╰┳━┳━━┳━━┫┃╭┳━━┳━╮
┃╰━╯┃┃╰━╯┃┃┃╱╭┫╭╮┃╭╮┃┃━┫╭━╮┃╭┫┃━┫╭╮┃╰╯┫┃━┫╭╯
┃╭━╮┣┫╭━╮┃┃╰━╯┃╰╯┃╰╯┃┃━┫╰━╯┃┃┃┃━┫╭╮┃╭╮┫┃━┫┃
╰╯╱╰┻┻╯╱╰╯╰━━━┻━━┻━━┻━━┻━━━┻╯╰━━┻╯╰┻╯╰┻━━┻╯' ''')
code = input("whats the coded word you want to break")
# e = len()
# #if statment
# #oo = a    
# h= o
# # p=r

code = code.replace("oo","a")
code = code.replace("fl","w")
code = code.replace("a","u")
code = code.replace("h","o")
code = code.replace("p", "r")
code = code.replace("a","u")
alphabets = digits = special = 0

for i in range(len(code)):
    if(code[i].isalpha()):
        alphabets = alphabets + 1
    elif(code[i].isdigit()):
        digits = digits + 1
    else:
        special = special + 1

    if alphabets >= 5:
      code = code.replace("e", "f")
      # code = code.replace("r","r")

print("\nTotal Number of Alphabets in this code :  ", alphabets, code)
print("Total Number of Digits in this code :  ", digits, code)
print("Total Number of Special Characters in this code :  ", special, code)
#ord()
#sort()
#number each alphabet then sort a=1
 #len function
 # 
def myFunc(e):
   return len(e) 
A = 1
B = 2
code = code
print(len(code))
#last_char = sample_str[-1]
#done 
print('Debuged: ', code)
if len(code) == 8:
  code = last_char = code[-1] ,code[-7], code[-8] , ".", code[-2],  code[-3] ,code[-4], code[-5] , code[-1], code[-8]
  print("821 765481")
  print (code)
  print("use translator to find the write wording")

  #done
if len(code) == 7:
  code = last_char = code[-1] ,code[-6], code[-7] , ".", code[-2],  code[-3] ,code[-4],".",code[-5] , code[-1], code[-6]
  print("721 654 372")
  print (code)
  print("use translator to find the write wording")

#done
if len(code) == 6:
  code = last_char = code[-1] ,code[-5], code[-6] , ".", code[-2],  code[-3] ,code[-4], code[-1], code[-5]
  print("621 543 62")
  print (code)
#done
if len(code) == 2:
  code = last_char = code[-1] ,code[-1], code[-2] 
  print("221")
  print (code)
  print("use translator to find the write wording")

#done

if len(code) == 5:
  code = last_char = code[-1] ,code[-4], code[-5] , code[-2],  code[-3] ,code[-4]
  print("521 432")
  print (code)
  print("use translator to find the write wording")

#done

if len(code) == 4:
  code = last_char = code[-1] ,code[-3], code[-4] , code[-2],  code[-3] ,code[-4], code[-1] 
  print("4213214")
  print (code)
  print("use translator to find the write wording")

#done

if len(code) == 3:
  print("321")
  if len(code) == 3:
     code = last_char = code[-1] , code[-2] , code[-3]
     print(code)
     print("use translator to find the write wording")


                   
                   
#test
#you=wow
#are = are
#to = too
#your = royuoyr
#mirroe = i regret
#more = eom(end of message) ruma
#than = notes
#you = wow