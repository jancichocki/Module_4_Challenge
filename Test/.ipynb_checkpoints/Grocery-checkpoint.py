# Step 1: Create a grocery list for the apple pie ingredients
grocery_list = ["Water", "Butter", "Eggs", "Apples", "Cinnamon", "Sugar", "Milk"]

# Step 2: Find the first two items on Mike's grocery list
print("First two items:", grocery_list[:2])

# Step 3: Find the last five items on Mike's grocery list
print("Last five items:", grocery_list[-5:])

# Step 4: Find every other item, starting from the second item, on Mike's grocery list
print("Every other item starting from the second one:", grocery_list[1::2])

# Step 5: Add 'flour' to the grocery list
grocery_list.append("Flour")
print("Grocery list after adding flour:", grocery_list)

# Step 6: Change 'apples' to 'gala apples'
grocery_list[grocery_list.index("Apples")] = "Gala Apples"
print("Grocery list after changing apples to gala apples:", grocery_list)

# Step 7: Determine the total number of items on the grocery list
print("Total number of items:", len(grocery_list))

# Challenge
# Finding the index of gala apples
print("Index of gala apples:", grocery_list.index("Gala Apples"))

# Removing sugar from the grocery list
grocery_list.remove("Sugar")
print("Grocery list after removing sugar:", grocery_list)

# Removing water from the grocery list based on its index
grocery_list.pop(grocery_list.index("Water"))
print("Grocery list after removing water:", grocery_list)

# Removing the last item from the grocery list
grocery_list.pop()
print("Grocery list after removing the last item:", grocery_list)