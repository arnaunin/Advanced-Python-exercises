import functools

@functools.lru_cache(maxsize=None)
def calculate_shipping_costs(destination, distance, weight):
    shipping_cost = 5 + distance * 0.1 + weight * 0.2
    return shipping_cost

destination = "Barcelona"
distance = 250
weight = 8

total_shipping_cost = calculate_shipping_costs(destination, distance, weight)
print(f"Total shiping cost to {destination} is {total_shipping_cost} $")