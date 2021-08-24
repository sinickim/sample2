Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tip = ['과일', '사과', '참외', '수박', '사과']
>>> tip
['과일', '사과', '참외', '수박', '사과']
>>> tip.append
<built-in method append of list object at 0x0000027C2972AB40>
>>> tip.append('수박')
>>> tip
['과일', '사과', '참외', '수박', '사과', '수박']
>>> tip.sort
<built-in method sort of list object at 0x0000027C2972AB40>
>>> tip.sort()
>>> tip
['과일', '사과', '사과', '수박', '수박', '참외']
>>> tip.count('사과')
2
>>> del append[2]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    del append[2]
NameError: name 'append' is not defined
>>> del tip[2]
>>> tip
['과일', '사과', '수박', '수박', '참외']
>>> tip [1:4]
['사과', '수박', '수박']
>>> tip
['과일', '사과', '수박', '수박', '참외']
>>> sin = [2, 2 ,3, 4]
>>> tip.extend(sin)
>>> tip
['과일', '사과', '수박', '수박', '참외', 2, 2, 3, 4]
>>> del tip[5:9]
>>> tip
['과일', '사과', '수박', '수박', '참외']
>>> tip[0] = '사회'
>>> tip
['사회', '사과', '수박', '수박', '참외']
>>> tip.sort()
>>> tip
['사과', '사회', '수박', '수박', '참외']
>>> tip.append('교육')
>>> tip
['사과', '사회', '수박', '수박', '참외', '교육']
>>> print("saddas")
saddas
>>> print('Hello world!')
Hello world!
>>> for(int i = 0; i < 10; i = i+3)
SyntaxError: invalid syntax
>>> tip[0]
'사과'
>>> 