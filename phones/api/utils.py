

def filter_by_nationality(phone, country=None):
    if not country:
        country = phone.built

    if phone.nationality == country:
        return True
    return False