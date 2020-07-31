import codecs

f=codecs.open(r"C:\Users\anast\Documents\SAP\Intelligent RPA\Desktop Studio\iRPA\log\sample.txt","r", "utf_8_sig")
h=f.read()
print(h)
# exit()
# a="111395 МОСКВА ГОРОД УЛИЦА ЮНОСТИ 5/1 1 , ОГРН: 1077764250970, Дата присвоения ОГРН: 22.12.2007, ИНН: 7720057236, КПП: 772001050, Руководитель: Лещев К Э, Дата прекращения деятельности: 22.12.2007"
# aa=a.replace(', ',',')
# print(aa)
lst = h.split(", ОГРН:") #парсинг на адрес и все стальное
b=lst[1].split(", ") #парсинг всего остального на детали 
b[0]= "ОГРН:"+b[0]  #исправление первой записи
# print(b)

val = dict()
val['Адрес']  = lst[0]
for i in range(len(b)):
    key=b[i].split(":")[0]
    print(key)
    value=b[i].split(":")[1]
    print(value)
    val[key] = value

print(val)
# print(val.get('Дата прекращения деятельности'))