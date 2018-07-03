label minigame:
    python:
        inventory = Inventory()
        for i in range(0,15):
            inventory.add_item(Item("caja" + str(i), "images/Inventario/inventario_UIBOX.png", "Sólo es una caja"))
        c = 0
        for i in inventory.my_items:
            print(inventory.my_items[c].name)
            print(inventory.my_items[c].image)
            print(inventory.my_items[c].description)
            c+=1
        ui.add(InventoryDisplayable())
        ui.interact(suppress_overlay=True, suppress_underlay=True)
