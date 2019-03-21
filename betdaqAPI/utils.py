def clean_locals(params):
    """Delete all self and empty elements in dict"""
    return dict((k, v) for k, v in params.items() if v is not None and k != 'self')

def list_check(maybe_list):
    if maybe_list:
        return maybe_list if isinstance(maybe_list, list) else [maybe_list]
    else:
        return []