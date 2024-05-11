# Реализовать консольное приложение заметки, с сохранением, чтением, добавлением, редактированием и удалением заметок. 
# 1. Заметка должна содержать идентификатор, заголовок, тело заметки и дату/время создания или последнего изменения заметки. 
# 2. Сохранение заметок необходимо сделать в формате json или csv формат (разделение полей рекомендуется делать через точку с запятой). 
# 3. Реализацию пользовательского интерфейса студент может делать как ему удобнее, можно делать как параметры запуска программы
# (команда, данные), можно делать как запрос команды с консоли и последующим вводом данных, как-то ещё, на усмотрение студента.
import pandas as pd
import csv
import os  
from datetime import datetime, date, time

   
def interface(file_name):
    col = ['id','title','note','date']
    if os.path.exists(file_name):
        df = pd.read_csv(file_name)
    else: df = pd.DataFrame(columns=col)

    var = 0
    while var != 6:
        print(
            '1. add note\n'
            '2. read notes\n'
            '3. delete note\n'
            '4. edit note\n'
            '5. save note\n'
            '6. exit'
        )
        var = input('input command: ')
        while var not in ('1','2','3','4','5','6'):
            print('incorrect input command')
            var = input('input command: ')
        match var:
            case '1':
                df = add_Note(df)
            case '2':
                df = read_Notes(df)
            case '3':
                df = delete_Note(df)
            case '4':
                df = edit_Note(df)
            case '5':
                df = save_Notes(df, file_name)        
            case '6':
                return print('end')

def add_Note(df):
    now = datetime.now()
    title = input("input title: ")
    note = input("input note: ")
    apnote = pd.Series({
        'id': len(df)+1,
        'title': title,
        'note': note,
        'date': "{}.{}.{}  {}:{}".format(now.day, now.month, now.year, now.hour, now.minute)
    })
    df.loc[len(df)] = apnote
    return df
    

def read_Notes(df):   
    print(df.head())
    print()
    return df

def delete_Note(df):
    inp = input("Input line id to delete: ")
    df.drop(df.loc[df["id"] == int(inp)].index, inplace=True)
    return df

def edit_Note(df):
    now = datetime.now()
    inp = input("Input line id to edit: ")
    title = input("input title: ")
    note = input("input note: ")
    df.loc[(df["id"] == int(inp))] = [int(inp), title, note, "{}.{}.{}  {}:{}".format(now.day, now.month, now.year, now.hour, now.minute)]
    return df

def save_Notes(df, file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
    df.to_csv(file_name, index=False)
    print("Saved.")
    return df

if __name__ == '__main__':
    interface("notefile.csv")