  # Sales Records Analysis 
  # ### Author: Jordan Worrobah
  # ### Exercise 2.E Using functions for analyzing data 
  # This notebook analyzes a small sales dataset using Python functions. 
  # Each function takes the full dataset as its first argument

sales_data = [
('Laptop', 'East', 1200.00),
('Phone', 'West', 850.00),
('Tablet', 'East', 400.00),
('Monitor', 'South', 650.00),
('Keyboard', 'West', 75.00),
('Laptop', 'South', 1150.00),
('Phone', 'East', 900.00),
('Tablet', 'West', 425.00),
('Monitor', 'East', 680.00),
('Keyboard', 'South', 80.00),
('Laptop', 'West', 1300.00),
('Phone', 'West', 820.00),
]

## Lab 1. Total sales by region

def region_total(data, region):
    return sum(amount for _, r, amount in data if r == region)

print(f"East Region Count: {region_total(sales_data, 'East'):.2f}") 
print(f"West Region Count: {region_total(sales_data, 'West'):.2f}") 
print(f"South Region Count: {region_total(sales_data, 'South'):.2f}")
print(f'North Region average: {region_total(sales_data, "North"):.2f}')
print("\n")

## Lab 2. Count of sales by region
def region_count(data, region):
    return sum(1 for _, r, amount in data if r == region)

print(f"East Region Count: {region_count(sales_data, 'East'):.2f}")
print(f"West Region Count: {region_count(sales_data, 'West'):.2f}")
print(f"South Region Count: {region_count(sales_data, 'South'):.2f}")
print(f'North Region average: {region_count(sales_data, "North"):.2f}')
print("\n")

## Lab 3. Average sale amount by region
def region_average(data, region):
    count = region_count(data, region)
    if count == 0:
        return 0
    return region_total(data, region) / count

print(f'East Region average: {region_average(sales_data, "East"):.2f}')
print(f'West Region average: {region_average(sales_data, "West"):.2f}')
print(f'South Region average: {region_average(sales_data, "South"):.2f}')
print(f'North Region average: {region_average(sales_data, "North"):.2f}')

## Lab 4. Filter by sale amount
def sales_above(data, threshold):
    return [record for record in data if record[2] > threshold]

print("These are the records performing above $500:\n")

above_500 = sales_above(sales_data, 500)

for record in above_500:
    print(record)
    print()


def sales_below(data, threshold):
    return [record for record in data if record[2] < threshold]

below_500 = sales_below(sales_data, 500)

print("These are the records performing below $500:\n")

for record in below_500:
    print(record)
    print()

## Lab 5. Top and bottom sale

def top_sale(data):
    max_record = max(data, key=lambda record: record[2])
    return max_record

print(top_sale(sales_data))

def bottom_sale(data):
    min_record = min(data, key=lambda record: record[2])
    return min_record

print(bottom_sale(sales_data))

print()

top_product, top_region, top_amount = top_sale(sales_data)

bottom_product, bottom_region, bottom_amount = bottom_sale(sales_data)

print(f"Top Sale: {top_product} in the {top_region} region for ${top_amount:.2f}")
print()

print(f"Bottom Sale: {bottom_product} in the {bottom_region} region for ${bottom_amount:.2f}")
print()

## Lab 6. Apply a discount

def apply_discount(data, discount_pct):

    return list(
        map(
            lambda s: (s[0], s[1], s[2] * (1 - discount_pct)),
            data
        )
    )


discounted_sales = apply_discount(sales_data, 0.15)


print("Original Records:")

for record in sales_data[:3]:
    print(record)


print("\n")


print("Discounted Records:")

for record in discounted_sales[:3]:
    print(record)

## Lab 7. Unique Regions

def unique_regions(data):

    return sorted(
        set(region for _, region, amount in data)
    )

print(unique_regions(sales_data))

## Lab 8. Region Summary

def region_summary(data, region):

    region_records = [record for record in data if record[1] == region]

    total = region_total(data, region)
    count = region_count(data, region)
    average = region_average(data, region)

    if count == 0:
        print(f"=== {region} Region ===")
        print("Records: 0")
        print("No sales records found for this region.")
        return

    top = top_sale(region_records)

    product = top[0]
    amount = top[2]

    print(f"=== {region} Region ===")
    print(f"Records: {count}")
    print(f"Total Sales: ${total:,.2f}")
    print(f"Average Sale: ${average:,.2f}")
    print(f"Top Sale: {product} — ${amount:,.2f}")



region_summary(sales_data, "East")
print()

region_summary(sales_data, "West")
print()

region_summary(sales_data, "South")
print()

region_summary(sales_data, "North")

## Lab 9. Region Summary Loop

for region in unique_regions(sales_data):

    region_summary(sales_data, region)

    print()