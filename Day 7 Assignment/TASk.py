
##Analyze and create samples for tuple characteristics

## 1. dynamic memory allocation

tpl_elements =(10,20,30,40,50,60,70,80,90) #tuple is an collection of data in ordered and unchangeable
print('before',tpl_elements) #before (10, 20, 30, 40, 50, 60, 70, 80, 90)

tpl_elements.append(20)
print('after append',tpl_elements) #AttributeError: 'tuple' object has no attribute 'append'

tpl_elements.insert(30)
print('after insert',tpl_elements) #AttributeError: 'tuple' object has no attribute 'insert'

tpl_elements.remove(60)
print('after remove',tpl_elements) #AttributeError: 'tuple' object has no attribute 'remove'

tpl_elements.pop(3)
print('after pop',tpl_elements) #AttributeError: 'tuple' object has no attribute 'pop'

## 2. data types

tpl_elements =(3003,200.0,'jeeva',True)
print('different datatypes are allowed',tpl_elements) # different datatypes are allowed (3003, 200.0, 'jeeva', True)

## 3. Duplication

tpl_elements =(100,200.0,30.03,'jeeva',100,30.03,'jack','jeeva')
print('duplication',tpl_elements) #duplication are allowed - duplication (100, 200.0, 30.03, 'jeeva', 100, 30.03, 'jack', 'jeeva')

## 4.index

tpl_elements =(3003,200.0,'jeeva',True)
index_result =tpl_elements[1]+tpl_elements[3]
print(index_result) #201.0  #it allows indexing. In this [1] is 200.0 and [3] is True it becomes 1. since bool derives from int

## 5.ordered

tpl = (10,20,30,40,50)
print('ordered collection',tpl) #ordered collection (10, 20, 30, 40, 50)

## 6.immutable

tpl = (10,20,30,40,50)
tpl[3] = 90   # TypeError: 'tuple' object does not support item assignment

## 7.slicing

tpl = (10,20,30,40,50,60,70,80,90)
print(tpl[-9:-3])   # (10, 20, 30, 40, 50, 60)
print(tpl[1:3])     # (20, 30)
print(tpl[-9:-2:2]) # (10,30,50,70)
