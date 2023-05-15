from itertools import chain
d = {'A' : [1,2,3,4,5],'B':[2,1,3,2,5,4],'C':[8,6,5,6,7,6]}
res = list(sorted(set(chain(*d.values()))))
print(res)
print('----------------------------------------------------------------------')

d= {'A':5,'B':4,'C':3,'D':2,'E':1}
print(sum(d.values()))
print('----------------------------------------------------------------------')

dic1 = {2:'A',3:'B'}
dic2 = {5:'C',8:'D'}
print(dic1 | dic2)
print('----------------------------------------------------------------------')

l = [('A',5),('B',6),('C',7)]
print(dict(l))
print('----------------------------------------------------------------------')

print(list(dic1.items()) + list(dic2.items()))
print('----------------------------------------------------------------------')

from collections import OrderedDict
x = {'D':678,'A':6574,'C':978,'B':1235}
print(OrderedDict(dict(sorted(x.items()))))
print('----------------------------------------------------------------------')

from math import sqrt
def cal():
    numbers = eval(input("Enter the Numbers  : "))
    result_rel = []
    c = 50
    h = 30
    for i in numbers:
        result = int(sqrt(2*c*i/h))
        result_rel.append(result)
    print(result_rel)
cal()
print('----------------------------------------------------------------------')

import json

with open("soft25/Python/Keyphrase-generation/data.json") as f:
    intents = json.load(f)
print('----------------------------------------------------------------------')

def genarray():
    x = int(input('Enter the row value  : '))
    y = int(input("Enter the column value : "))
    
    outer_ind = []
    for i in range(x):
        outer_ind.insert(x,[])
        for j in range(y):
            outer_ind[i].append(j)
    print(outer_ind)
genarray()
print('----------------------------------------------------------------------')

def sort_string():
    in_str = input('Enter the string : ')
    out_string = ','.join(sorted(in_str.split(',')))
    print(out_string)
sort_string()
print('----------------------------------------------------------------------')

def uniq_word():
    text = input('Type_in : ')
    text_split = text.split(' ')
    
    word_lis = []
    for i in text_split:
        if i not in word_lis:
            word_lis.append(i)
    print(word_lis)
uniq_word()

print('----------------------------------------------------------------------')
    
phases = input('Type_in : ')
phases = list(phases)
L = 0
D = 0
for i in phases:
    if i.isalpha():
        L = L+1
    elif i.isdigit():
        D = D+1
    else:
        pass
print(L)
print(D)
print('----------------------------------------------------------------------')

x = 10.5456
print(x.abs())
print('----------------------------------------------------------------------')

def sqr_num(num):
    for i in range(0,num+1):
        print(i*i)

x = 3
y = sqr_num(x)

print(next(y))
print(next(y))
print(next(y))
print('----------------------------------------------------------------------')

class div_gen:
    def __init__(self,in_num):
        self.in_num = in_num
    def cal(self):
        for i in range(0,self.in_num+1):
            if i%7 == 0:
                yield i 
output = div_gen(100) 
for i in output.cal():
    print(i)
print('----------------------------------------------------------------------')

def frequency():
    string = input('Type in : ')
    frequency = {}
    for i in string.split(" "):
        if (frequency.get(i) == None):
            frequency[i] = 1
        else:
            frequency[i] += 1
    
    for i in sorted(frequency):
        print(f'{i} : {frequency[i]}',end = ' ')
frequency()
print('----------------------------------------------------------------------')

class person():
    def getGender():
        pass
class male(person):
    def getGender():
        print('Male')
class female(person):
    def getGender():
        print('Female')

male.getGender()
female.getGender()
print('----------------------------------------------------------------------')

def generatesen():
    verb = ['I','Love']
    subject = ['Play','you']
    obj = ['Cricket','Hockey']
    for i in verb:
        for j in subject:
            for k in obj:
                print(f'{i} {j} {k}')
generatesen()
print('----------------------------------------------------------------------')

string = b'hello world!hello world!hello world!hello world!'
import gzip
s = gzip.compress(string)
print(s)

t = gzip.decompress(s)
print(t)
print('----------------------------------------------------------------------')

from bisect import bisect_left
def Binarysearch(a,x):
    i = bisect_left(a, x)
    print(i)
    if i !=len(a) and a[i] == x:
        return i
    else:
        return -1
    
a = [1,6,4,2,3,9,8]
x = 3
res = Binarysearch(a, x)
print(res)
print('----------------------------------------------------------------------')

def show_num(in_num):
    for i in range(0,in_num+1):
        if i%5 == 0 and i%7 == 0:
            yield i
for i in show_num(100):
    print(i,end = ' ')
print('----------------------------------------------------------------------')

def even_num(in_num):
    for i in range(0,in_num+1):
        if i%2 == 0:
            yield i
for i in even_num(100):
    print(i,end=' ')
print('----------------------------------------------------------------------')

def febonaci(in_num):
    if in_num == 0:
        return 0
    elif in_num == 1:
        return 1
    else:
        return febonaci(in_num-1)+febonaci(in_num-2)
print([febonaci(x) for x in range(20)])
print('----------------------------------------------------------------------')

print([i for i in range(0,20)])
print('----------------------------------------------------------------------')

def g_mil():
    string = input('Type in : ')
    out_string = string.split('@')
    print('The name is :',out_string[0])
g_mil()
print('----------------------------------------------------------------------')

class shape:
    def area(self):
        return 0
class squre(shape):
    def __init__(self,in_num):
        self.in_num = in_num
    def cal(self):
        return self.in_num*self.in_num
s = squre(10)
print(s.cal())
print('----------------------------------------------------------------------')

from bisect import bisect_left
def find_num(a,x):
    i = bisect_left(a, x)
    print(i)
a = [1,2,3,4,5,6,7,8,9]
x = int(8)
res = find_num(a, x)
print(res)
print('----------------------------------------------------------------------')

for i in range(0,100):
    if i%5 ==0 and i%7==0:
        print(i)
print('----------------------------------------------------------------------')

def divshow(in_num):
    for i in range(0,in_num+1):
        if i%5 ==0 and i%7 == 0:
            print(i)
divshow(100)
print('----------------------------------------------------------------------')

def even_num(in_num):
    lis1 = []
    for i in range(0,in_num+1):
        if i%2 == 0:
            lis1.append(i)
    print(lis1)
even_num(100)
print('----------------------------------------------------------------------')

def evn_num(in_num):
    for i in range(0,in_num+1):
        if i%2 == 0:
            yield i
for i in evn_num(100):
    print(i,end=' ')
print('----------------------------------------------------------------------')

def showdiv_num(in_num):
    for i in range(0,in_num+1):
        if i%5==0 and i%7 == 0:
            yield i 
            
for i in showdiv_num(100):
    print(i)
print('----------------------------------------------------------------------')

def genFibnacci(in_num):
    if in_num == 0:
        return 0
    elif in_num == 1:
        return 1
    else:
        return genFibnacci(in_num-1)+genFibnacci(in_num-2)
print([genFibnacci(x) for x in range(20)])
print('----------------------------------------------------------------------')

class sqre:
    def area(self,length):
        return 0
class sqre():
    def __init__(self,length):
        self.length = length
    def area(self):
        return self.length*self.length
Sqre = sqre(10)
print(Sqre.area())
print('----------------------------------------------------------------------')

def stutterWord():
    in_string = input('Enter the word:')
    out_string = in_string.replace(in_string[0:2],((in_string[0:2]+'... ')*2)+ in_string[0:2])  +'?'
    print(f'{in_string} ➞ {out_string}')

for i in range(3):
    stutterWord()
print('----------------------------------------------------------------------')

def sutterword():
    in_string = input('Type_in : ')
    print(((in_string[0:2]+'...')*2)+'...'+in_string)
    out_string = in_string.replace(in_string[0:2],((in_string[0:2]+'...')*2)+ in_string[0:2])
    print(out_string)
sutterword()
print('----------------------------------------------------------------------')

import math
def radiantodegree():
    in_num = int(input('Enter the numbers : '))
    out_num = (180/math.pi)*in_num 
    print(out_num)
for i in range(0,3):
    radiantodegree()
print('----------------------------------------------------------------------')

def cruzon_number():
    in_num = int(input('Enter the number : '))
    if ((2**in_num)+1)%((2*in_num)+1) == 0:
        print(f'{in_num} is a cruzon_number')
    else:
        print(f'{in_num} its not a curzon number')
cruzon_number()
print('----------------------------------------------------------------------')

def binary():
    in_num = int(input('Enter the no : '))
    out_num = bin(in_num)
    print(out_num)
binary()
print('----------------------------------------------------------------------')

def eve_div(a,b,c): 
    lis_new = []
    for i in range(a,b+1):   
        if i%2 == 0:
            lis_new.append(i)
    print(lis_new)
    print(sum(lis_new))
eve_div(0,10,2)
print('----------------------------------------------------------------------')

x ='print(55)' 
print(eval(x)) 
print('----------------------------------------------------------------------')


def Reple_vow(char,string):
    voules = ['a','e','i','o','u','A','E','I','O','U']
    for i in voules:
        string = string.replace(i,char)
    return string
char = input('Type_the char: ')
string = input('Enter the String: ')
Reple_vow(char,string)
print('----------------------------------------------------------------------')

def factor(in_num):
    a = 1
    for i in range(1,in_num+1):
        y = i * a
        a=y
    print(y)
in_num = int(input("Enter the no of number : "))
factor(in_num)    
print('----------------------------------------------------------------------')

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
n = int(input('enter the number : '))
factorial(n)
print('----------------------------------------------------------------------')

string1 = input('Enter the string1 : ')
string2 = input('Enter the string2 : ')
if string1 == string2:
    print('The diffrence is zero : 0')
else:
    count = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            count = count+1
    print(count)
print('----------------------------------------------------------------------')

def dltr(n):
    lis_ne = []
    for i in n:
        if type(i) == int and i >= 0:
            lis_ne.append(i)
    print(lis_ne)
dltr([1,2,'t',8,'yt','j'])
dltr([123,'hjky',8,'ju',2,'09',9,8,'lo'])
print('----------------------------------------------------------------------')

def revrese(string):
    print(string[::-1])
str = input('Type in : ')
revrese(str)
print('----------------------------------------------------------------------')

first,*middle,last =[1,2,3,4,5,6,7,8]
print(first)
print(middle)
print(last)
print('----------------------------------------------------------------------')

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
in_num = int(input('enter the number : '))
factorial(in_num)
print('----------------------------------------------------------------------')

print(factorial(5))
print('----------------------------------------------------------------------')

def appnds(list1,num):
    list2 = []
    list3 = []
    for i in list1:
        if i == num:
            list3.append(i)
        else:
            list2.append(i)
    print(list3)
    print(list2)
    list2.extend(list3)
    return list2
appnds([4,56,6,78,54,3,2,1], 1)
print('----------------------------------------------------------------------')

def move_to_end(list,num):
    first_end = []
    second_end = []
    for ele in list:
        if ele == num:
            second_end.append(ele)
        else:
            first_end.append(ele)
    print(second_end)
    print(first_end)
    first_end.extend(second_end)
    return first_end
    
print(f'move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ {move_to_end([1, 3, 2, 4, 4, 1], 1)}')
print(f'move_to_end([7, 8, 9, 1, 2, 3, 4], 9) ➞ {move_to_end([7, 8, 9, 1, 2, 3, 4], 9)}')
print(f'move_to_end(["a", "a", "a", "b"], "a") ➞ {move_to_end(["a", "a", "a", "b"], "a")}')
l = [5,4,8,7,6,5,5,5,4]
print('----------------------------------------------------------------------')

list1 = [1,2,3,4]
list2 = [2,7]
list1.insert(2,7)
print(list1)
print('----------------------------------------------------------------------')

def  doul_str(string):
    out_string = ' '
    for i in string:
        print(i)
        out_string = out_string+ i*2
    return out_string
string = input('Type_in : ')
doul_str(string)
print('----------------------------------------------------------------------')

def doul_str(string):
    out_str = ' '
    for i in string:
        out_str = out_str+i*2
    return out_str
string = input('Type_in : ')
doul_str(string)
print('----------------------------------------------------------------------')

def reverse(stri):
    if type(stri) == bool:
        return not stri
    else:
        print('Boolien_Expected')
        
reverse(True)
reverse(False)
reverse(0)
print('----------------------------------------------------------------------')

num = int(input('Enter the numbers :  '))
new_lis = []
old_lis = []
list3 = []
for i in range(1,num+1):
    x = i+i
    old_lis.append(x)
    print(old_lis)
    for i in range(1,i+1):
        new_lis.append(old_lis[-1])
        list3.append(new_lis[-1]*2)
print(old_lis)
print(new_lis)
print(list3[-1])
print('----------------------------------------------------------------------')

initial_thickness = 1
fold_count = 5
thickness = initial_thickness
for i in range(1,fold_count+1):
    print(i)
    thickness = thickness*2
print(thickness)
print('----------------------------------------------------------------------')

def doul_stri(in_string):
    list_new= ' '
    for i in in_string:
       list_new = list_new+i*2
    print(list_new)
in_string = input('Type_in : ')
doul_stri(in_string)
print('----------------------------------------------------------------------')

def reverse(in_str):
    if type(in_str) == bool:
        return not in_str
    else:
        print('Boolien_expected')
#x = input('Type_in  : ')
reverse(True)
print('----------------------------------------------------------------------')

def fold_pap(in_num):
    initial_dim = 1
    x = initial_dim
    for i in range(1,in_num+1):
        x = x*2
    return x
in_num = int(input('Enter the no of fold  : '))
fold_pap(in_num)
print('----------------------------------------------------------------------')

def numbr(in_string):
    new_lis = []
    for i in range(len(in_string)):
        if in_string[i].isupper():
            new_lis.append(i)
    print(new_lis)
in_string = input('Type_in  : ')
numbr(in_string)
print('----------------------------------------------------------------------')

def numbr(in_string):
    new_lis1 = []
    for i in in_string:
        if i.isupper():
            new_lis1.append(in_string.index(i))
        print(new_lis1)
in_string = input('Type_in : ')
numbr(in_string)
print('----------------------------------------------------------------------')

def eve_num(in_num):
    new_lis = []
    for i in range(1,in_num+1):
        if i%2 == 0:
            new_lis.append(i)
    print(new_lis)
    
for i in range(0,3):
    in_num = int(input('Enter the in_num: '))
    x = eve_num(in_num)
    print(x)
print('----------------------------------------------------------------------')

def filtre(in_input):
    lis_new = []
    for i in in_input:
        if type(i) == int:
            lis_new.append(i)
    print(lis_new)
            
in_input = eval(input('Enter the input : '))
filtre(in_input)
print('----------------------------------------------------------------------')

def add_ind(in_list):
    new_lis = []
    for i in range(len(in_list)):
        j = in_list[i]+i
        new_lis.append(j)
    print(new_lis)
in_list = eval(input('Enter the in_list : '))
add_ind(in_list)
print('----------------------------------------------------------------------')

def find_num(in_list):
    new_lis = []
    for i in range(len(in_list)):
        if i not in in_list:
            new_lis.append(i)
    print(new_lis)
in_list = eval(input('Enter the in_list : '))
find_num(in_list)
print('----------------------------------------------------------------------')            

def mere(in_list,num):
    if len(in_list) > 1:
        in_list.append(num)
        in_list.remove(in_list[0])
        print(in_list)
mere([4,5,6,7,8,9,10,11],2)
print('----------------------------------------------------------------------')

def budjet(dict):
    sum1 = 0
    for i in dict:
        sum1 = sum1+i["budget"]
    print(sum1)
budjet([
{ "name": "John", "age": 21, "budget": 23000 },
{ "name": "Steve", "age": 32, "budget": 40000 },
{ "name": "Martin", "age": 16, "budget": 2700 }
])
print('----------------------------------------------------------------------')

dict1 = {'name':"Moorthy.p",'Age':23,'Phone':54959590555}
print(dict1.keys())
print('----------------------------------------------------------------------')

dict1 = {'Name':'Mano','Age':26,'Phone':894305}
print(dict1.values())
print('----------------------------------------------------------------------')

def rev_wor(in_stri):
    x = ' '.join(sorted(in_string))
    print(x)
in_string = input('Type_in : ')
rev_wor(in_string)
print('----------------------------------------------------------------------')

def in_list1(in_list):
    new_lis = []
    for i in in_list:
        if type(i) == int:
            new_lis.append(i)
    print(new_lis)
in_list = eval(input('Enter the list value : '))
in_list1(in_list)
print('----------------------------------------------------------------------')

def boll_lis(lis1,lis2):
    if len(lis1) == len(lis2):
        for i in lis1:
            if i not in lis2:
                print('False')
            else:
                print('True')
    else:
        print('Len1 and Len2 must be same')
lis1 = eval(input('Enter the lis1 values : '))
lis2 = eval(input('Enter the lis2 values : '))
boll_lis(lis1,lis2)
print('----------------------------------------------------------------------')

def simon_says(l1,l2):
    if len(l1) == len(l2) and len(l1) >= 2 and len(l2) >= 2:
        if (l1[:-1]) == (l2[1:]):
            print(l1[:-1])
            print(l2[1:])
            print(f'{l1,l2} ➞ {True}')
        else:
            print(f'{l1,l2} ➞ {False}')
            

simon_says([1, 2], [5, 1])
simon_says([1, 2], [5, 5])
simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4])
simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3])        
print('----------------------------------------------------------------------')

def captr(in_list):
    new_lis = []
    for i in in_list:
        out_str = i.split(',')
        print(out_str)
        for j in out_str:
            for k in j:
                if k.isupper():
                    new_lis.append(k)
    print(new_lis)
captr(['Klaia','MAno','Bad','Perumanl'])
print('----------------------------------------------------------------------')

def sor_capt(in_lis):
    out_str = []
    for i in in_lis:
        out_str.append(i[0])
    print(out_str)
    y = ' '.join(out_str)
    print(y)
sor_capt(['Kalai','Mano','Ram','Jesus','Kajal'])
print('----------------------------------------------------------------------')

in_string = 'Alogorrtthimsw'
x = len(set(in_string))
print(x)
print('----------------------------------------------------------------------')

def isiso(in_str):
    ou_str = in_str.lower()
    if len(ou_str) == len(set(ou_str)):
        print('this is isogram')
    else:
        print('this is not isogram')
isiso('Algorthm')
print('----------------------------------------------------------------------')

in_num = eval(input('Enter the numbers : '))
print(len(in_num))
print(len(set(in_num)))
print(set(in_num))
print('----------------------------------------------------------------------')

def compr(in_string):
    for i in range(len(in_string)):
        x = ''.join(sorted(in_string))
        if x[i] == in_string[i]:
            print('True')
        else:
            print('False')
in_string = input('Type_in : ')
compr(in_string)
print('----------------------------------------------------------------------')

def compr(in_string):
    sort_in_string = ''.join(sorted(in_string))
    print(sort_in_string)
    if in_string == sort_in_string:
        print('True')
    else:
        print('False')
in_string = input('Type_in : ')
compr(in_string)
print('----------------------------------------------------------------------')

in_num = eval(input('Enter the numbers  : '))
print(in_num)
print(str(in_num)[::-1])
print('----------------------------------------------------------------------')

def com_num(in_num):
    if in_num == in_num[::-1]:
        print('True')
    else:
        print('False')
in_num =eval(input('Enter the numbers'))
com_num(in_num)
print('----------------------------------------------------------------------')

def mul_num(in_num):
    out_num = in_num.split(',')
    print(out_num)
    y =1
    for i in range(len(out_num)-1):
        if i == 0:
            x =int(out_num[i])*int(out_num[i+1])
            y = y+x
        else:
            y = y*int(out_num[i+1])
    print(y)
mul_num('1,8,2,2,2')     
print('----------------------------------------------------------------------')

in_num = [2,8,2]
y = 1
for i in in_num:
    y = y*i
print(y)
print('----------------------------------------------------------------------')

in_lis = ('1,2,3,4,5')
out_str = in_lis.split(',')
print(out_str)
y = 1
for i in out_str:
    i = int(i)
    y = y*i
print(y)
print('----------------------------------------------------------------------')

def sqr(in_num):
    for i in in_num:
        y =i**2
        print(y)
in_num = eval(input('Enter the numbers'))
sqr(in_num)
print('----------------------------------------------------------------------')

def sq_num(in_num):
    for i in str(in_num):
        i = int(i)
        y = i**2
        print(y)
in_num = int(input('Enter the number : '))
print(in_num)
sq_num(in_num)
print('----------------------------------------------------------------------')

in_num = int(input('Enter the in_num : '))
print(type(in_num))
for i in str(in_num):
    print(type(i),i)
print('----------------------------------------------------------------------')

def rem(in_num):
    x = sorted(set(in_num))
    print(x)

in_num = eval(input('Enter the numbers : '))
rem(in_num)
print('----------------------------------------------------------------------')

def men(in_numbers):
    men = sum(in_numbers)/len(in_numbers)
    print(men)
in_numbers = eval(input('Enter the nubers : '))
men(in_numbers)
print('----------------------------------------------------------------------')

def mul(in_num):
    new_lis = []
    for i in range(0,in_num+1):
        if i%4 == 0:
            new_lis.append(i*10)
        else:
            new_lis.append(i)
    print(new_lis)
in_num = int(input('Enter the numbers : '))
mul(in_num)
print('----------------------------------------------------------------------')

lis = [5,4,3,2,4,3,4,3,2,2,2,3,4,5,5,]
x = lis.count(4)
print(x)
print('----------------------------------------------------------------------')

def unique(in_num):
    for i in set(in_num):
        if in_num.count(i) == 1:
            print(i)
in_num = [2,3,3,4,4,1,1]
unique(in_num)
print('----------------------------------------------------------------------')

import math
class Rads:
    def __init__(self,in_num):
        self.in_num = in_num
    def rads(self):
        print(round(math.pi*self.in_num*self.in_num))
    def pre(self):
        print(round(2*math.pi*self.in_num))
obj = Rads(11)
obj.rads()
obj.pre()
print('----------------------------------------------------------------------')

def lis1(in_lis):
    return sorted(in_lis,key=len)
lis1(['Apple','Banana','Orange','Kiwi'])
print('----------------------------------------------------------------------')

def sqr(a,b,c):
    if (a*a + b*b) == c*c:
        print('True')
    elif (a*a + c*c) == b*b:
        print('True')
    elif (b*b + c*c) == a*a:
        print('True')
    else:
        print('False')
sqr(5,3,4)
print('----------------------------------------------------------------------')

def rept(a,b,c):
    if a==b==c:
        print(3)
    elif a==b or b==c or c==a:
        print(2)
    else:
        print(1)
rept(2,2,2)
print('----------------------------------------------------------------------')

def splt(dict):
    new_lis = []
    for key,values in dict.items():
        new_lis.append((key,values))
    print(new_lis)
splt({'name':'Moorthy','Age':24,'phone':987837577})
splt({'Name':'Kalai','Age':54,'Phone':8529856})    
print('----------------------------------------------------------------------')

def uppr(valu):
    out_dic = {}
    for i in valu:
        out_dic[i] = i.upper()
    print(out_dic)
uppr(['p','s'])
print('----------------------------------------------------------------------')

def vou_repl(lis,char):
    vou = ['a','e','i','o','u','A','E','I','O','U']
    out_string = ''
    for i in lis: 
        if i in vou:
            out_string = out_string+char
        else:
            out_string = out_string+i
    print(out_string)
char = input('Type_in : ')
vou_repl('apple banana orange',char)
print('----------------------------------------------------------------------')

def spl(in_input):
    values1 = []
    values2 = []
    for i in in_input:
        if type(i) == int or float or complex:
            values1.append(i)
        else:
            values2.append(i)
    print(values1)
    print(values2)
in_input = eval(input('Enter the values : '))
spl(in_input)
print('----------------------------------------------------------------------')   
    
x = 5
x + 1
print(x)   
print('----------------------------------------------------------------------')   
    
x = 'spam'+'spamspam'
print(x)

y = 'spam'
print(y*3)
print('----------------------------------------------------------------------')

k5j = 'Eggs'
print(k5j)    
print('----------------------------------------------------------------------')

l = [8,'k',9,'po','*',99.56,78.65]
for i in l:
    if type(i) == int:
        print(i)
    elif type(i) == float:
        print('Floate',i)
    else:
        print('String',i)
print('----------------------------------------------------------------------')

'i have'+ ' 99 ' +'Eggs'
print('----------------------------------------------------------------------')


x =not(5>4)
print(x)
print('----------------------------------------------------------------------')

print(True and True)
print(True and False)
print(False and True)
print(False and False)
print(True or False)
print(True or True)
print(False or True)
print(False or False)
print(not True)
print(not False)
print('----------------------------------------------------------------------')

(5>3) and 5==3
(5>3) and 5==5    
not(5>3)    
not(5>=9)
(True and True) and (True == False)
(not False) or (not True)
print('----------------------------------------------------------------------')

a = 10
if a ==9:
    print('True')
else:
    print('False')
print('----------------------------------------------------------------------')

spam = 10
if spam == 10:
    print('Spam1')
    if spam>15:
        print('it not a spam')
else:
    print('cam')
    print('Spam')
    print('Spam')
print('----------------------------------------------------------------------')

for i in range(1,11):
    if i == 3:
        pass
    print(i)
print('----------------------------------------------------------------------')

for i in range(0,10):
    print(i)

i = 1
while(i<=10):
    print(i)
    i = i+1
print('----------------------------------------------------------------------')

















