import tkinter as tk
from random import shuffle
from random import randint

f=open(u"questions.txt",'r') #достать вопросы из файла
arr=f.readlines()
f.close()
ray=[]
h=0
for i in range(0,len(arr),5):
    ray.append([])
    for j in range(4):
        ray[h].append(arr[i+j])
        ray[h][j]=ray[h][j][:-1]
    h=h+1
arr.clear()

for i in range(len(ray)): #перемешивание ответов
    arr.append([])
    for j in range(1,4):
        arr[i].append(ray[i][j])
    shuffle(arr[i])
    ray[i][1]=arr[i][0]
    ray[i][2]=arr[i][1]
    ray[i][3]=arr[i][2]

frs=[]
snd=[]
thrd=[]
for i in ray: #перемешивание вопросов
    b=randint(1,3)
    if b==1:
        frs.append(i)
    if b==2:
        snd.append(i)
    if b==3:
        thrd.append(i)

num_questions=len(frs)+len(snd)+len(thrd)
que=frs+snd+thrd

answer=[] #список номеров верных ответов
for q in que:
    for w in q:
        if w[-1]=="@":
            answer.append(q.index(w))
quest=[]
i=1
for n in range(num_questions):
    que[n][0]=str(i)+"."+que[n][0] #нумерация вопросов
    for j in range(len(que[n])):
        if que[n][j][-1]=="@":  #убрать метку правильного ответа
            que[n][j]=que[n][j][:-1]
    quest.append((que[n], answer[n]))
    for j in range(1,4):
        quest[n][0][j]=str(j)+")"+quest[n][0][j] #нумерация вариантов ответов
    i+=1

numdom=len(quest)
user=[]
score=0
num=0
def d1():
    global num, score, entry
    if num==numdom: 
        entry.pack_forget()
        die.destroy()
        text['bg']='bisque'
        text['height']=12
        text.delete("1.0",tk.END)
        for i in range(len(user)): #вывод результатов тестирования
            user[i]=quest[i][0][0]+" "+user[i]+"\n"
            text.insert(tk.END,user[i])
            
        score=round(score/num*100,2)
        button['text']=f"Процент выполнения: {score}%\n Нажмите,чтобы закрыть это окно"
        button['command']=game_over
        button.pack()
        root.focus()
        return
    if num==0:
        answer_widget()
    text['height']=7
    text['bg']='bisque'
    text['width']=56
    text.delete("1.0",tk.END)
    text.insert("1.0",'\n'.join(quest[num][0])+"\n\nВыберите правильный ответ:")
    button.pack_forget()
    num+=1

def game_over(): #функция закрытия графического интерфейса
    root.destroy()

def answer_widget(): #функция обработки ввода пользователя
    global entry
    entry=tk.Entry(root,textvariable=solution,width=3,bg="gold",font="Arial 20")
    entry.pack()
    entry.bind("<Return>", lambda x: check())
    entry.focus()

def empty_textbox(): #функция очистки текстового поля
    solution.set("")
    d1()

def check(): #функция проверки введённого ответа
    global n, score
    text.delete("1.0",tk.END)
    if solution.get()==str(quest[num-1][1]):
        user.append("|  +")#список ответов пользователя
        text.insert(tk.END, "Верно!")
        score+=1
        text['bg']="green"
    else:
        user.append("|  -")#список ответов пользователя
        text.insert(tk.END,"Ошибка!")
        text['bg']="red"
    
    sc="\nПравильных ответов: "+str(score)+"\n"
    label['text']=sc
    text.after(800,empty_textbox)

root=tk.Tk()
root.title("Богданов М.Д. 19-ИЭ-1")

heading="""Тест по дисциплине: программирование
Название темы: структуры данных, словари в Python,
операции со словарями и методы словарей"""
label=tk.Label(root,text=heading,font="Arial 18",justify="left")
label.pack()

rules="""Отвечайте на вопросы

Нажмите на кнопку ниже чтобы начать
Вы увидите вопрос
Введите вариант ответа и нажмите Enter
"""
text=tk.Text(root,height=6,width=56,font="Arial 20")
text.insert("1.0",rules)
text.pack()

die=tk.Button(root,height=1,width=3,text="X",command=game_over,bg="tomato",font="Arial 12")
die.place(x=0,y=0)

button=tk.Button(root,text="Нажмите, чтобы начать",bg="grey87",command=d1,font="Arial 18")
button.pack()

solution=tk.StringVar()

root.mainloop()
