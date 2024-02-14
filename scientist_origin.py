import csv
with open('scientist.csv',encoding='windows-1251') as csvfile:
    reader = csv.reader(csvfile,delimiter='#',quotechar='"')
    a = []
    print('Разработчиками Аллопуринола были такие люди (результаты выведите в порядке возрастания даты):')
    for i in reader:
        s = str(i)
        s = s.split(';')
        if 'Аллопуринол' in s:
                
                print('ФИО ученого',s[0],'-','Дата создания',s[2])
    print('Оригинальный рецепт принадлежит:','Желнеронов Георгий Тимофеевич') 
    


    
    