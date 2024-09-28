import findspark
findspark.init()
#Tugas 1: Buat DataFrame sederhana di Spark dan eksplorasi beberapa fungsi dasar yang tersedia
# Contoh membuat DataFrame sederhana dan operasi dasar
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('HandsOnPertemuan6').getOrCreate()
data = [('James', 'Sales', 3000),
        ('Michael', 'Sales', 4600),
        ('Robert', 'Sales', 4100),
        ('Maria', 'Finance', 3000)]
columns = ['EmployeeName', 'Department', 'Salary']

df = spark.createDataFrame(data, schema=columns)
df.show()

print("="*100,"\n")

#Tugas 2: Gunakan operasi filter, select, groupBy untuk mengekstrak informasi dari data, 
#serta lakukan agregasi data untuk mendapatkan insight tentang dataset menggunakan perintah seperti mean, max, sum.
df.select('EmployeeName', 'Salary').show()
df.filter(df['Salary'] > 3000).show()
df.groupBy('Department').avg('Salary').show()
df.groupBy('Department').count().show()
df.groupBy('Department').sum('Salary').show()
df.groupBy('Department').max('Salary').show()

print("="*100,"\n")

#Tugas 3: Eksplorasi bagaimana mengolah tipe data kompleks dalam Spark DataFrames
df = df.withColumn('SalaryBonus', df['Salary'] * 0.1)
df = df.withColumn('TotalCompensation', df['Salary'] + df['SalaryBonus'])
df.show()

print("="*100,"\n")

#Tugas 4: Implementasikan window function untuk menghitung running totals atau rangkings.
from pyspark.sql.window import Window
from pyspark.sql import functions as F

windowSpec = Window.partitionBy('Department').orderBy('Salary')
df.withColumn('Rank', F.rank().over(windowSpec)).show()