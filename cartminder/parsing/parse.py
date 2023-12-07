import ndjson

with open('../knowledge/products.ndjson', encoding='utf-8') as f:
    products = ndjson.load(f)

with open('../knowledge/categories.ndjson', encoding='utf-8') as f:
    categories = ndjson.load(f)

with open('../knowledge/measurements.ndjson', encoding='utf-8') as f:
    measurements = ndjson.load(f)


print(products)
print(categories)
print(measurements)



# product, quantity, measurement 
# OR
# quantity, measurement, product

"""
for each product:
    or_(
        or_(product.aliases) quantity or(product.measurements.aliases),
        ...
    )
"""
