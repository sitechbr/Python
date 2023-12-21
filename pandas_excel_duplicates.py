import pandas as pd
from pathlib import Path

gophish = "gophish_import.csv"

report1c = pd.read_excel('report_1c.xlsx',dtype=str)
vip = pd.read_excel('vip.xlsx',dtype=str)
report1c_df = pd.DataFrame(report1c, columns=['Организация','Сотрудник', 'Адрес электронной почты', 'Должность'])
report1c_df.columns=['First Name','Last Name','Email','Position']

vip_df = pd.DataFrame(vip,columns=['ФИО','Должность'])
vip_df.columns=['Last Name','Position']
vip_list = vip_df['Last Name'].unique()



#Удаление дупликатов
foo_df = report1c_df.drop_duplicates(subset=['Email'])

#Добавление в таблицу випов и удаление дубликатов полностью
#gophish_df = pd.concat([foo_df,vip_df]).drop_duplicates(subset=['Last Name','Position'],keep=False).dropna(subset=['Email'])
#Удаление випов по списку
gophish_df = foo_df[~foo_df['Last Name'].isin(vip_list)]
gophish_df.to_csv(gophish,sep=',',encoding='utf-8',index=False)

print(str(Path.cwd())+'/'+gophish)
