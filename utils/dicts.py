def get_val(collection, key, default='git'):
    if collection:
        return collection[key]
    return default
