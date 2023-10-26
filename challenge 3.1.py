def linear_search_product_list(productList, targetProduct):
    indices = []
    for index, product in enumerate(productList):
        if product == targetProduct:
            indices.append(index)
    return indices

# Example usage:
products = ["shoes", "boot", "loafes", "shoes", "sandal", "shoes"]
target = "shoes"
target2 = "apple"
result = linear_search_product_list(products, target)
print(result)