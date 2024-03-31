#
def add_inventory(inventory, widget_name, quantity):
    if widget_name in inventory:
        inventory[widget_name] += quantity
    else:
        inventory[widget_name] = quantity

def remove_inventory_widget(inventory, widget_name):
    if widget_name in inventory:
        del inventory[widget_name]
        return "Record deleted"
    else:
        return "Item not found"