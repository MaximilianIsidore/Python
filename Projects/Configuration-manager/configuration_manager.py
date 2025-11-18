def add_setting(setting, new_setting):
    key = new_setting[0].lower()
    value = new_setting[1].lower()
    
    # Check if key already exists (case-insensitive)
    existing_keys = [k.lower() for k in setting]
    if key in existing_keys:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    setting[key] = value
    return (setting, f"Setting '{key}' added with value '{value}' successfully!")

def update_setting(setting, new_setting):
    key = new_setting[0].lower()
    value = new_setting[1].lower()
    
    # Check if key exists (case-insensitive)
    found_key = None
    for k in setting:
        if k.lower() == key:
            found_key = k
            break
    
    if not found_key:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    
    # Update the value
    setting[found_key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"

def delete_setting(setting, del_key):
    key = del_key.lower()
    found_key = None
    for k in setting:
        if k.lower() == key:
            found_key = k
            break
    
    if not found_key:
        return "Setting not found!"
    
    del setting[found_key]
    return f"Setting '{key}' deleted successfully!"

def view_settings(setting):
    if not setting:
        return "No settings available."
    
    res = "Current User Settings:\n"
    for k, v in setting.items():
        res += f"{k.capitalize()}: {v}\n"
    
    return res



test_settings = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}

print(add_setting(test_settings, ('data', 'ON')))
print(update_setting(test_settings, ('Data', 'off')))
print(delete_setting(test_settings, 'data'))
print(view_settings(test_settings))
print(add_setting({'theme': 'light'}, ('volume', 'high')))