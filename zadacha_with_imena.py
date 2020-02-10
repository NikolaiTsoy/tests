#open file, read it, раздели слова 
f= open('names.txt')
a = f.read()
b = a.split('","')

#Убрать кавычки в начале и конце (завершение разделения) 
a = b[0].split('"')
c = b[len(b)-1].split('"')
b[0] = a[1];
b[len(b)-1] = c[0] 
names_list = b






#Словарь перехода от букв к чиислам
abc = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17','r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x': '24', 'y':'25','z':'26'}






#Сортировка, придевение букв к нижнему регистру, подчсет суммы для каддого слова и общей суммыы 

names_sort = sorted(names_list)
names_int = []
for i in range(len(names_sort)):
  a = names_sort[i].lower()
  sum1 = 0
  for letter in a: 
    sum1 += int(abc[letter])
  sum_order = sum1 * (i+1)
  names_int.append(sum_order)
print(sum(names_int))














