it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))

it_companies.add('Twitter')
print(it_companies)

it_companies = {'Tesla', 'DELL', 'HP'}
new_comp = {'Tesla', 'DELL'}
it_companies.update(new_comp)
print(it_companies)

it_companies.pop()
print(it_companies)
print(it_companies <= new_comp)



