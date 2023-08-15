

def filter_by_nationality(phone, country=None):
    if not country:
        country = phone.built.name

    if phone.nationality == country:
        return True
    return False