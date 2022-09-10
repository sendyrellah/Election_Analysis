Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> type(3)
<class 'int'>
>>> type(2019)
<class 'int'>
>>> type(8374.84)
<class 'float'>
>>> type("test")
<class 'str'>
>>> type("39843")
<class 'str'>
>>> type("343.343")
<class 'str'>
>>> type(true)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
>>> help("keywords")

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not

>>> help("operators")
No Python documentation found for 'operators'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> help("arithmetic operators")
No Python documentation found for 'arithmetic operators'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> 5+2
7
>>> 8//5-3
-2
>>> 8/5-3
-1.4
>>> 8/5
1.6
>>> 1.6-3
-1.4
>>> 8+22*2-4
48
>>> 16-3/2+7-1
20.5
>>> 3**3%5
2
>>> 5+9*3/2-4
14.5
>>> counties=["Arapahoe","Denver","Jefferson"]
>>> counties = ["Arapahoe","Denver","Jefferson"]
>>> counties = ["Arapahoe","Denver","Jefferson"]
>>> python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'python' is not defined
>>> counties = ["Acounties = ["Arapahoe","Denver","Jefferson"]
  File "<stdin>", line 1
    counties = ["Acounties = ["Arapahoe","Denver","Jefferson"]
                                      ^
SyntaxError: invalid syntax
>>> counties = ["Arapahoe","Denver","Jefferson"]
>>> counties = ["Arapahoe","Denver","Jefferson"]
>>> counties
['Arapahoe', 'Denver', 'Jefferson']
>>> counties[0]
'Arapahoe'
>>> counties[1]
'Denver'
>>> len(counties)
3
>>> counties[0:2]
['Arapahoe', 'Denver']
>>> counties.append("El Paso")
>>> counties