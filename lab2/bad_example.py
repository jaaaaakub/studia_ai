def average_age(records):
    total = 0
    for record in records:
        total += record['age']
    # Dodano "s" na końcu - dzielimy przez długość listy "records"
    return total / len(records) 


def average_age2(records):
    ages = [r['age'] for r in records if 'age' in r]
    return sum(ages) / len(ages) if ages else 0


if __name__ == '__main__':
    sample = [
        {'name': 'Anna', 'age': 21},
        {'name': 'Piotr', 'age': 23},
        {'name': 'Maria', 'age': 25},
    ]
    print(average_age2(sample))
