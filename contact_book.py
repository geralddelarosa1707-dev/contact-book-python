print("Welcome to Contact Book!")

contact_book = {}

options = {
  1: "Add Contact",
  2: "Delete Contact",
  3: "Search Contact",
  4: "View All Contacts",
  5: "Update Contact",
  6: "Exit"
}

def display_options(options):
  print("\n------Options------")
  for num, option in options.items():
    print(f"{num}. {option}")
  print("-------------------")

def display_contacts(contact_book):
  print("\n------Contacts------")
  for name, number in sorted(contact_book.items()):
    print(f"Name: {name.title()}, Number: {number}")
  print("--------------------")

def validate_name():
  name = input("Enter name: ").strip().lower()
  
  return name if name else None
  
def get_valid_number():
  number_input = input("Enter number: ").strip()
  clean_number = number_input.replace(" ", "")

  if not clean_number.isdigit():
    return None
    
  return number_input
  
def normalize_number(number):
  return number.replace(" ", "")
  
def number_exists(contact_book, number, exclude_name=None):
  for stored_name, stored_number in contact_book.items():
    if stored_name != exclude_name and normalize_number(number) == normalize_number(stored_number):
        return True
  return False
            
def can_add_contact(contact_book, name):
  return name not in contact_book

def can_delete_contact(contact_book, name):
  return name in contact_book

def can_update_contact(contact_book, name):
  return name in contact_book

def main():
  while True:
    display_options(options)
    
    try:
      ask_user_option = int(input("\nWhat do you want to do? (1-6): "))
    except ValueError:
      print("\nPlease enter only a number.")
      continue
  
    if ask_user_option == 1:
      print("\n-----Add Contact-----")
      
      name = validate_name()

      if not name:
        print("\nPlease enter a valid name.")
        continue
      
      number = get_valid_number()
      
      if not number:
        print("\nPlease enter a valid number (digits and spaces only).")
        continue
      
      if number_exists(contact_book, number):
        print("\nNumber already exists!")
        continue
        
      if not can_add_contact(contact_book, name):
        print("\nContact already exists!")
        continue
      else:
        contact_book[name] = number
        print("\nContact added successfully!")
        display_contacts(contact_book)
  
    elif ask_user_option == 2:
      print("\n-----Delete Contact-----")
      
      name = validate_name()

      if not name:
        print("\nPlease enter a valid name.")
        continue
      
      if can_delete_contact(contact_book, name):
        confirm = input(f"Are you sure you want to delete {name.title()}? (y/n): ")

        if confirm.lower() != "y":
          print("\nDeletion cancelled.")
          continue
        else:
          del contact_book[name]
          print("\nContact deleted successfully!")
      else:
        print("\nContact not found!")
      display_contacts(contact_book)
        
    elif ask_user_option == 3:
      print("\n-----Search Contact-----")
      
      name = validate_name()

      if not name:
        print("\nPlease enter a valid name.")
        continue

      found = False

      for stored_name, number in contact_book.items():
        if stored_name.startswith(name):
          print(f"\nName: {stored_name.title()}, Number: {number}")
          found = True
          
      if not found:
        print("\nContact not found!")
  
    elif ask_user_option == 4:
      if not contact_book:
        print("\nNo contacts found!")
        continue
      else:
        display_contacts(contact_book)
  
    elif ask_user_option == 5:
      print("\n-----Update Contact-----")
      
      name = validate_name()

      if not name:
        print("\nPlease enter a valid name.")
        continue
      
      if can_update_contact(contact_book, name):
        number = get_valid_number()
        
        if not number:
          print("\nPlease enter a valid number (digits and spaces only).")
          continue
      
        if number_exists(contact_book, number, name):
          print("\nNumber already exists!")
          continue
          
        contact_book[name] = number
        print("\nContact updated successfully!")
      else:
        print("\nContact not found!")
      display_contacts(contact_book)
  
    elif ask_user_option == 6:
      print("\nExiting Contact Book...")
      print("Thank you for using Contact Book!")
      break
  
    else:
      print("\nInvalid option. Please try again.")
      
if __name__ == "__main__":
  main()