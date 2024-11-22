names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

def search_name(search_term):
    if search_term in names:
        return f"{search_term} found in the list."
    else:
        return f"{search_term} not found in the list."

print(search_name("Sam"))

user_input = input("Enter a name to search for: ")
print(search_name(user_input))