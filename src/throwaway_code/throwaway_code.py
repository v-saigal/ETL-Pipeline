transactions = [{"size":"large", "name":"choco", "price":2.90},{"size":"large", "name":"choco", "price":2.90}, {"size":"regular", "name":"choco", "price":2.90}, {"size":"large", "name":"choco", "price":2.95}]

store = []


for trans in transactions:
    in_store = False
    for item in store:
        if trans["size"] == item["size"] and trans["name"] == item["name"] and item["price"] == trans["price"]:
            in_store = True
            break
        else:
            continue
    if in_store == False:
        store.append(trans)
    else:
        continue
    
print(store)