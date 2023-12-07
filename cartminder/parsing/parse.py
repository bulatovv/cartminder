import ndjson

with open('../knowledge/products.ndjson', encoding='utf-8') as f:
    products = ndjson.load(f)


with open('../knowledge/measurements.ndjson', encoding='utf-8') as f:
    measurements = ndjson.load(f)

from yargy import Parser, rule
from yargy.interpretation import fact, attribute
from yargy.predicates import dictionary


Integer = fact('Integer', ['value'])

# Russian numeral dictionary mapping
numbers_dict = {
    'ноль': 0,
    'один': 1,
    'два': 2,
    'три': 3,
    'четыре': 4,
    'пять': 5,
    'шесть': 6,
    'семь': 7,
    'восемь': 8,
    'девять': 9,
    'десять': 10,
    'одиннадцать': 11,
    'двенадцать': 12,
    'тринадцать': 13,
    'четырнадцать': 14,
    'пятнадцать': 15,
    'шестнадцать': 16,
    'семнадцать': 17,
    'восемнадцать': 18,
    'девятнадцать': 19,
    'двадцать': 20,
    'тридцать': 30,
    'сорок': 40,
    'пятьдесят': 50,
    'шестьдесят': 60,
    'семьдесят': 70,
    'восемьдесят': 80,
    'девяносто': 90,
    'сто': 100,
    'двести': 200,
    'триста': 300,
    'четыреста': 400,
    'пятьсот': 500,
    'шестьсот': 600,
    'семьсот': 700,
    'восемьсот': 800,
    'девятьсот': 900,
    'тысяча': 1000,
    'миллион': 1000000,
}



# Create a rule to extract integer values from Russian numerals
integer_rule = rule(
    dictionary(numbers_dict.keys()).repeatable()
).interpretation(Integer.value)

parser = Parser(integer_rule)

text = "десять тысяч сто семьдесят два"
result = parser.extract(text)
print([match.fact for match in result])


products_dict = [alias for product in products for alias in product['aliases']]

print(products_dict)
