import pandas as pd
import oracledb

def Connect20OracleDB(username,password):    
   connection = oracledb.connect(
       user = username,
       password = password,
       dsn = "cs-n-5194.ehealthsask.ca:1521/DWP")
   return connection

username = "rpanchal"
password = "Surat@2499"

connection = Connect20OracleDB(username, password)

cursor = connection.cursor()


pd.set_option('display.max_columns', None)

excelpath = "Q:/INFOPROD/HOSPITAL/REQUESTS/2025-26 Error Reports/2025-07/Provider Number 2025-07.xlsx"

idlist = ['MPID','Saskatoon','Yorkton','Internal','RQHR']
df = pd.read_excel(excelpath, sheet_name="no convert summary", skiprows=3)

facilitynum = df.columns[0]
#print("First column name:",first_column)
nonnullfacilitynum = df[facilitynum].dropna()

doctornumber = df.columns[2]
nonnulldoctornumber = df[doctornumber].dropna()

for x in df[facilitynum]:
     #print(x)
     if pd.notnull(x):
          cursor.execute("SELECT hosp_name FROM DW_COMOBJ.dim_hosp_num where hosp_num = " + str(x))
          result = cursor.fetchone()
          print(doctornumber[x])
          print(result)
     
cursor.close()
connection.close()



