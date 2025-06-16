def make_new_item():
  response = requests.post('http://server.com/items', json={'name': input('Enter new item name: ')})
  if response.status_code == 201:
    print("Item created successfully")