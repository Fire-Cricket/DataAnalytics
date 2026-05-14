# Jordan R. Worrobah
# 5/13/2026
# Sales Performance

sales_data = [ 
            ('Marcus Webb', 'East', 4250.00), 
              ('Priya Sharma', 'West', 5875.50), 
              ('DeShawn Carter', 'East', 3100.75), 
              ('LaTonya Rivers', 'South', 6420.00), 
              ('Bob Nguyen', 'West', 4980.25), 
              ]

totalSales = 0

for data in sales_data:
    name = data[0]
    region = data[1]
    sales = data[2]

    totalSales += sales

    if 5000 < sales:
        print(f"\n{name} {region} ${sales:.2f}")
        print(f"^Top performer!\n")
    else:
        print(f"{name} {region} ${sales:.2f}")

print(f"\nThese are the total sales: ${totalSales:.2f}\n")
