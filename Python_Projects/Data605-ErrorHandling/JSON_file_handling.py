import json

# json.loads() - take a str
# json.load() - takes a file

# json.dumps() - creates formatted json str
# json.dump() - creates a json file

# loading and writing json files
# json.load

def json_load(json_file: str):
    """Load a json_file from this directory """
    try:
        with open(json_file) as file:
            json_data = json.load(file)
            return json_data
    except:
        print("Error occurred, check input.")

def json_create(json_data, file_name):
    """Creates a new json file under file_name using json_data"""
    try:
        with open(f"{file_name}.json", "w") as jsonfile:
            json.dump(json_data, jsonfile)
    except:
        print("Error occurred, check input.")

def json_convert_to_str(json_data):
    """Converts a json_data to a string"""
    return json.dumps(json_data)

def json_convert_to_dict(json_data):
    """Converts a json_data to a dictionary"""
    return json.loads(json_data)

def customer_selection(json_data, customer: int):
    """Selects a specific customer (1 or 2) from the json_data"""
    transformed_item = json_data["customers"][customer]
    return transformed_item

def key_customer_information(json_data):
    """Gives simple customer information, id, full_name, and what they ordered"""
    new_data = []
    for item in json_data["customers"]:
        new_item = {"customer_id" : item["customer_id"], "full_name" : item["first_name"] + " " + item["last_name"], "orders" : item["orders"]}
        new_data.append(new_item)
    return {"Key_customer_info" : new_data}

customer_data = json_load("customers.json")

print(customer_data)

single_customer_data = customer_selection(customer_data, 1)

print(single_customer_data)

customer_info = key_customer_information(customer_data)

json_create(customer_info, "customer_info")
