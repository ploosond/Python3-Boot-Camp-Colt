def show_information(first_name="Colt", is_instructor=False):
    if first_name == "Colt" and is_instructor:
        return "Welcome back instructor Colt!"
    elif first_name == "Colt":
        return "I really thought you were an instructor...!"
    return (f"Hellow {first_name}!")

print(show_information())
print(show_information(is_instructor=True))
print(show_information("Molly"))