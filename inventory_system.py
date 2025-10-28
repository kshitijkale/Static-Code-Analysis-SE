# import json
# import logging
# from datetime import datetime

# # Global variable
# stock_data = {}

# def addItem(item="default", qty=0, logs=[]):
#     if not item:
#         return
#     stock_data[item] = stock_data.get(item, 0) + qty
#     logs.append("%s: Added %d of %s" % (str(datetime.now()), qty, item))

# def removeItem(item, qty):
#     try:
#         stock_data[item] -= qty
#         if stock_data[item] <= 0:
#             del stock_data[item]
#     except:
#         pass

# def getQty(item):
#     return stock_data[item]

# def loadData(file="inventory.json"):
#     f = open(file, "r")
#     global stock_data
#     stock_data = json.loads(f.read())
#     f.close()

# def saveData(file="inventory.json"):
#     f = open(file, "w")
#     f.write(json.dumps(stock_data))
#     f.close()

# def printData():
#     print("Items Report")
#     for i in stock_data:
#         print(i, "->", stock_data[i])

# def checkLowItems(threshold=5):
#     result = []
#     for i in stock_data:
#         if stock_data[i] < threshold:
#             result.append(i)
#     return result

# def main():
#     addItem("apple", 10)
#     addItem("banana", -2)
#     addItem(123, "ten")  # invalid types, no check
#     removeItem("apple", 3)
#     removeItem("orange", 1)
#     print("Apple stock:", getQty("apple"))
#     print("Low items:", checkLowItems())
#     saveData()
#     loadData()
#     printData()
#     eval("print('eval used')")  # dangerous

# main()
#FIXED CODE :)
import json
from datetime import datetime
from typing import Dict, List, Optional

STOCK_DATA: Dict[str, int] = {}

def add_item(item: str = "default", qty: int = 0, logs: Optional[List[str]] = None) -> None:
    if not item:
        return
    if logs is None:
        logs = []
    STOCK_DATA[item] = STOCK_DATA.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")

def remove_item(item: str, qty: int) -> None:
    try:
        if item in STOCK_DATA:
            STOCK_DATA[item] -= qty
            if STOCK_DATA[item] <= 0:
                del STOCK_DATA[item]
    except KeyError:
        print(f"Item '{item}' not found in inventory")

def get_qty(item: str) -> int:
    return STOCK_DATA.get(item, 0)

def load_data(file: str = "inventory.json") -> None:
    global STOCK_DATA
    try:
        with open(file, "r", encoding="utf-8") as file_handle:
            STOCK_DATA = json.load(file_handle)
    except FileNotFoundError:
        print(f"File '{file}' not found. Starting with empty inventory.")
        STOCK_DATA = {}
    except json.JSONDecodeError:
        print(f"Invalid JSON in file '{file}'. Starting with empty inventory.")
        STOCK_DATA = {}

def save_data(file: str = "inventory.json") -> None:
    with open(file, "w", encoding="utf-8") as file_handle:
        json.dump(STOCK_DATA, file_handle, indent=2)

def print_data() -> None:
    print("Items Report")
    for item, quantity in STOCK_DATA.items():
        print(f"{item} -> {quantity}")

def check_low_items(threshold: int = 5) -> List[str]:
    result = []
    for item, quantity in STOCK_DATA.items():
        if quantity < threshold:
            result.append(item)
    return result

def main() -> None:
    add_item("apple", 10)
    add_item("banana", -2)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()

if __name__ == "__main__":
    main()
