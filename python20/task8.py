server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}
for i_key, i_value in server_data.items():
    print("\n", i_key)
    for i_elem, i_quantity in i_value.items():
        print("\t", i_elem, ":", i_quantity)
