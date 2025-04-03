import json
from datetime import datetime

# Read the list of sales in the json file
with open("sales.json", 'r') as sales_json:
    # Save that list in a variable
    sales = json.load(sales_json)

# Main fuction
def analyze_sales(sales):
    
    # 1. Filter sales made in the last quarter of the year
    filtered_sales = [sale for sale in sales if datetime.strptime(sale['date'], "%Y-%m-%d").month >= 10]
    
    # 2. Select only sales of products with an amount greater than $500
    filtered_sales = [sale for sale in filtered_sales if sale['amount'] > 500]

    # 3. Group sales by buyer location
    grouped_sales = {}

    for sale in filtered_sales:
        location = sale['location']
        if location not in grouped_sales:
            grouped_sales[location] = []
        grouped_sales[location].append(sale)

    # 4. Calculate the average sales amount for each location
    average_amounts = {}

    for location, products in grouped_sales.items():
        average_amounts[location] = sum(product['amount'] for product in products) / len(products)
    
    # 5. Sort locations by average sales value in descending order. Uses lambda functions.
    sorted_locations = dict(sorted(average_amounts.items(), key=lambda x: x[1], reverse=True))

    # 6. Print the results
    for location, avg_amount in sorted_locations.items():
        print(f"Location: {location}, Average Sales Amount: ${avg_amount:.2f}")

analyze_sales(sales)
