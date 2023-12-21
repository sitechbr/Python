import pandas as pd
from pathlib import Path

gophish = "DropBox.csv"
export_file="Education.csv"

report1c = pd.read_excel('report_1c.xlsx',dtype=str)
gophish_df = pd.read_csv(gophish,delimiter=',')
gophish_df = pd.DataFrame(gophish_df,columns=['status','email'])
gophish_df = gophish_df[(gophish_df.status == 'Clicked Link') | (gophish_df.status == 'Submitted Data')]
gophish_df.columns = ['status','E-mail']
#print(gophish_df)

report1c_df = pd.DataFrame(report1c, columns=['Сотрудник','Табельный номер', 'Подразделение', 'Должность','Адрес электронной почты','Код','Табельный номер'])
report1c_df.columns=['Сотрудник ФИО','Табельный номер','Подразделение','Должность','E-mail','Код ЕСС','ЕСС']
report1c_df= report1c_df.drop_duplicates(subset=['E-mail'])
report1c_df['E-mail'] = report1c_df['E-mail'].str.lower()
#rint(report1c_df)
result_df=pd.merge(gophish_df,report1c_df,on='E-mail',how='left')
#
#print(result_df)


#'Сотрудник ФИО'	'Табельный номер' 'Подразделение'	'Должность'	'E-mail'	'Код ЕСС'	'Категория работника'	'ЕСС'


#Удаление дупликатов
#foo_df = report1c_df.drop_duplicates(subset=['Email'])

#Добавление в таблицу випов и удаление дубликатов полностью
#gophish_df = pd.concat([foo_df,vip_df]).drop_duplicates(subset=['Last Name','Position'],keep=False).dropna(subset=['Email'])
#Удаление випов по списку
#gophish_df = foo_df[~foo_df['Last Name'].isin(vip_list)]
result_df.to_csv(export_file,sep=',',encoding='utf-8')

print(str(Path.cwd())+'/'+export_file)
