# -*- coding: utf-8 -*-
"""

@author: Алина
"""

import pandas as pd
import datetime as dt
df = pd.read_csv('parse.csv')
df2 = df
name = df['Name']
new_name = []
"""Группировка вакансий по названию"""
for i in name:
    if (i.lower().find('рекрутер')!=-1 or i.lower().find('recruiter')!=-1 or 
        i.lower().find('recrutier')!=-1):
        new_name.append('IT-рекрутер')
    elif i.lower().find('архитектор')!=-1 or i.lower().find('architect')!=-1:
        new_name.append('IT Архитектор')
    elif i.lower().find('координатор')!=-1:
        new_name.append('Координатор')
    elif ((i.lower().find('проект')!=-1 or i.lower().find('project')!=-1) and 
         (i.lower().find('менеджер')!=-1 or i.lower().find('manager')!=-1)
         or i.lower().find('руководитель')!=-1 or 
         i.lower().find('lead')!=-1 or
         i.lower().find('админ')!=-1 or i.lower().find('admin')!=-1 ):
        new_name.append('Project manager')
    elif i.lower().find('делопроизводитель')!=-1:
        new_name.append('Делопроизводитель')
    elif i.lower().find('стажер')!=-1 or i.lower().find('стажёр')!=-1:
        new_name.append('Стажёр')    
    elif (i.lower().find('ресечер')!=-1 or i.lower().find('ресёчер')!=-1
        or i.lower().find('researcher')!=-1 or i.lower().find('ресерчер')!=-1):
        new_name.append('Ресечер')
    elif i.lower().find('заместитель')!=-1:
        new_name.append('Заместитель руководителя')
    elif ((i.lower().find('админ')!=-1 or i.lower().find('administrator')!=-1)
        and (i.lower().find('системный')!=-1 or i.lower().find('system')!=-1)
        or (i.find('Cистемный')!=-1)):
        new_name.append('Системный администратор')
    elif i.lower().find('frontend')!=-1 or i.lower().find('front-end')!=-1:
        new_name.append('Frontend - developer')
    elif i.lower().find('backend')!=-1 or i.lower().find('back-end')!=-1:
        new_name.append('Backend - developer')
    elif ((i.lower().find('продукт')!=-1 or
           i.lower().find('product')!=-1 or i.lower().find('продакт')!=-1) and 
         (i.lower().find('менеджер')!=-1 or i.lower().find('manager')!=-1)):
        new_name.append('Product manager')
    elif (i.lower().find('ассистент')!=-1 or i.lower().find('помощник')!=-1 or 
          i.lower().find('assistant')!=-1):
        new_name.append('Ассистент')
    elif i.lower().find('эксперт')!=-1:
        new_name.append('IT Эксперт')
    elif i.lower().find('экономист')!=-1:
        new_name.append('IT Экономист')
    elif i.lower().find('писатель')!=-1:
        new_name.append('Технический писатель')
    elif i.lower().find('редактор')!=-1:
        new_name.append('Редактор')    
    elif i.lower().find('преподаватель')!=-1 or i.lower().find('куратор')!=-1:
        new_name.append('Преподаватель')
    elif ((i.lower().find('продаж')!=-1 or i.lower().find('sale')!=-1) and 
         (i.lower().find('менеджер')!=-1 or i.lower().find('manager')!=-1
          or i.lower().find('специалист')!=-1 or
          i.lower().find('specialist')!=-1 or 
          i.lower().find('консультант')!=-1 or
          i.lower().find('consultant')!=-1)):
        new_name.append('Sales manager')
    elif i.lower().find('юрис')!=-1 or i.lower().find('lawyer')!=-1:
        new_name.append('IT Юрист')
    elif i.lower().find('журналист')!=-1:
        new_name.append('IT журналист')
    elif i.lower().find('дизайнер')!=-1:
        new_name.append('UI/UX Дизайнер')
    elif i.lower().find('аналитик')!=-1 or i.lower().find('analyst')!=-1:
        new_name.append('IT Аналитик')
    elif i.lower().find('hr')!=-1 or i.lower().find('персонал')!=-1:
        new_name.append('HR manager')
    elif i.lower().find('developer')!=-1 or i.lower().find('разработчик')!=-1:
        if (i.lower().find('java')!=-1):
            new_name.append('Java developer')
        elif (i.lower().find('react')!=-1):
            new_name.append('React developer')
        elif ((i.lower().find('.net')!=-1) or (i.lower().find('c#')!=-1)):
            new_name.append('C# developer')
        else:
            new_name.append('IT Developer')
    elif i.lower().find('консультант')!=-1 or i.lower().find('consultant')!=-1:
        new_name.append('IT консультант')
    elif (i.lower().find('маркетолог')!=-1 or i.lower().find('smm')!=-1
          or i.lower().find('продвижение')!=-1
          or i.lower().find('маркетинг')!=-1):
        new_name.append('SMM')
    elif (i.lower().find('директор')!=-1 or i.lower().find('начальник')!=-1 or 
          i.lower().find('head')!=-1 or i.lower().find('director')!=-1):
        new_name.append('IT Директор')
    elif i.lower().find('инженер')!=-1 or i.lower().find('engineer')!=-1:
        new_name.append('IT Инженер')
    elif (i.lower().find('специалист')!=-1 or i.lower().find('cпециалист')!=-1 
          or i.lower().find('specialist')!=-1):
        new_name.append('IT Специалист')
    elif i.lower().find('програм')!=-1:
        new_name.append('Программист')
    elif i.lower().find('audit')!=-1:
        new_name.append('IT Аудитор')
    elif i.lower().find('продавец')!=-1:
        new_name.append('Продавец сайтов')
    elif i.lower().find('manager')!=-1 or i.lower().find('менеджер')!=-1:
        new_name.append('IT manager')
    elif (i.lower().find('бизнес')!=-1 or i.lower().find('партнёр')!=-1 or 
          i.lower().find('partner')!=-1 or 
          i.lower().find('business')!=-1):
        new_name.append('IT партнёр')
    else:
        new_name.append(i)
print(f'Было уникальных вакансий {len(set(name))} стало {len(set(new_name))}')
df2['Name'] = new_name
df2['Day_from_pars'] = [None]*len(df2)

""" Заполнение пропусков по ЗП вместо пустых, добавление нового признака - количествово дней после парсинга """
for idx,row in df2.iterrows():
    if pd.isna(row['MinSalary']):
        fr_salary = df2.loc[(df2['Name'] == row['Name']) & 
                            (df2['City'] == row['City'])]['MinSalary'].mean()
        if not pd.isna(fr_salary):
            fr_salary = int(fr_salary)
        df2.at[idx, 'MinSalary'] = fr_salary
    if pd.isna(row['MaxSalary']):
        MaxSalary = df2.loc[(df2['Name'] == row['Name']) & 
                            (df2['City'] == row['City'])]['MaxSalary'].mean()
        if not pd.isna(MaxSalary):
            MaxSalary = int(MaxSalary)
        df2.at[idx,'MaxSalary'] = MaxSalary
    delta = dt.date.today() - dt.datetime.strptime(row['Date'].split('T')[0],
                                                   "%Y-%m-%d").date()
    df2.at[idx,'Day_from_pars'] = int(str(delta).split()[0])

df2['Expirience'] = df2['Expirience'].fillna('Нет опыта')
df2['Employment'] = df2['Employment'].fillna('Любой тип')

df2.to_csv('new.csv')