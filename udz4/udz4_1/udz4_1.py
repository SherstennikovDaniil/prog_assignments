import pandas

excelDataDF = pandas.read_excel("flowers.xlsx", sheet_name="winter")
print(excelDataDF)
