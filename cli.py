import requests

BASE_URL = "http://127.0.0.1:5000"

while True:
    print("\n1.View Inventory")
    print("2.Add Product")
    print("3.Update Stock")
    print("4.Delete Product")
    print("5.Find on API")
    print("6.Exit")

    choice = input("Choose: ")

    if choice == "1":
        r = requests.get(f"{BASE_URL}/inventory")
        print(r.json())

    elif choice == "2":
        name = input("Name: ")
        brand = input("Brand: ")
        price = int(input("Price: "))
        stock = int(input("Stock: "))
        barcode = input("Barcode: ")

        payload = {
            "product_name": name,
            "brands": brand,
            "price": price,
            "stock": stock,
            "barcode": barcode
        }

        r = requests.post(f"{BASE_URL}/inventory", json=payload)
        print(r.json())

    elif choice == "3":
        id = input("ID: ")
        stock = input("New Stock: ")

        r = requests.patch(f"{BASE_URL}/inventory/{id}", json={"stock": stock})
        print(r.json())

    elif choice == "4":
        id = input("ID: ")
        r = requests.delete(f"{BASE_URL}/inventory/{id}")
        print(r.json())

    elif choice == "5":
        code = input("Barcode: ")
        r = requests.get(f"{BASE_URL}/search/{code}")
        print(r.json())

    elif choice == "6":
        break