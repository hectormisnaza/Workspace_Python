friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print('Hi ', friend)


color = "Green"
thing = "Hope"
print(color + " is the color of " + thing)

semana = 7
dia = 24
minutos = 60
segundos = 60
print(semana * dia * minutos * segundos)

disk_size = 16*1024*1024*1024
sector_size = 512
sector_amount = disk_size * sector_amount

print(sector_amount)

# REPLACE THIS STARTER CODE WITH YOUR FUNCTION
june_days = 30
print("June has " + str(june_days) + " days.")
july_days = 31
print("July has " + str(july_days) + " days.")

def month_days(month, days):
    print(month + " has " + str(days) + " days.")
month_days("June", 30)
month_days("July", 31)