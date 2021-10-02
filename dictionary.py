alien_0 = {'color':'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

# country
country_codes = {'Finland': 'fi', 'South Africa': 'za','Nepal': 'np'}
print(country_codes)
print(len(country_codes))

if country_codes:
    print('country_codes is not empty')
else:
    print('country_codes is empty')

country_codes.clear()
if country_codes:
    print('country_codes is not empty')
else:
    print('country_codes is empty')

# Iterating through a Dictionary
days_per_month = {'January': 31, 'February': 28, 'March': 31}
print(days_per_month)

for month, days in days_per_month.items():
    print(f'{month} has {days} days')

# Using a dictionary to represent an instructor's grade book.
grade_book = {
'Susan': [92, 85, 100],
'Eduardo': [83, 95, 79],
'Azizi': [91, 89, 82],
'Pantipa': [97, 91, 92]
}
all_grades_total = 0
all_grades_count = 0
for name, grades in grade_book.items():
    total = sum(grades)
    print(f'Average for {name} is {total/len(grades):.2f}')
    all_grades_total += total
    all_grades_count += len(grades)
print(f"Class's average is: {all_grades_total / all_grades_count:.2f}")