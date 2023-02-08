class sbi:
    b_name = 'SBI'
    loc = 'basavangudi'


print('--------befrore object creation---------')
print(sbi.b_name)
print(sbi.loc)

print()

sbi_banglore = sbi
print('---------after one object is created -------')
print(sbi_banglore.b_name)
print(sbi_banglore.loc)

print()
sbi_banglore.b_name = 'SBI Banglore'
sbi_banglore.loc = 'banglore'
print('----------on changing the generic variable of class ---------')
print(sbi_banglore.b_name)
print(sbi_banglore.loc)
