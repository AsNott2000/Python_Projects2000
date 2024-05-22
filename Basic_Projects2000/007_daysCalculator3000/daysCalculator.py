from datetime import date

firstDay = int(input("input first day: "))
firstMonth = int(input("input first month: "))
firstYear = int(input("input first year: "))

secondDay = int(input("input second day: "))
secondMonth = int(input("input second month: "))
secondYear = int(input("input second year: "))


firstDate = date(firstYear,firstMonth,firstDay)
secondDate = date(secondYear,secondMonth,secondDay)

print((secondDate - firstDate).days)