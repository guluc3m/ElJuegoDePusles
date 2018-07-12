label minigame:
    python:
        inventory = Inventory()
        for i in range(0,15):
            inventory.add_item(Item("caja" + str(i), "images/Inventario/inventario_UIBOX.png", "Sólo es una caja " + str(i)))
        ui.add(InventoryDisplayable(inventory))
        ui.interact(suppress_overlay=True, suppress_underlay=True)
