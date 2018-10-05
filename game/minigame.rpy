label minigame:
    python:
        inventory = Inventory()
        for i in range(0,15):
            inventory.add_item(Item("caja" + 'Paco', "images/Inventario/pepe.png", "Caja " + str(i+1)))
        ui.add(InventoryDisplayable(inventory))
        ui.interact(suppress_overlay=True, suppress_underlay=True)
