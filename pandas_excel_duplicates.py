import pandas as pd

gophish = "gophish_import.csv"

report1c = pd.read_excel('report_1c.xlsx')
vip = pd.read_excel('vip.xlsx')
report1c_df = pd.DataFrame(report1c, columns=['Name', 'Email', 'Позиция'])
vip_df = pd.DataFrame(vip,columns=['Name','Позиция'])

#Удаление дупликатов
foo_df = report1c_df.drop_duplicates(subset=['Email'])
#Добавление в таблицу випов и удаление дубликатов полностью
gophish_df = pd.concat([foo_df,vip_df]).drop_duplicates(subset=['Name','Позиция'],keep=False)
gophish_df.to_csv('gophish_import.csv',sep=',',encoding='utf-8',index=False,header=False)



