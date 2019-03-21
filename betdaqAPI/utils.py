def clean_locals(params):
    """Delete all self and empty elements in dict"""
    return dict((k, v) for k, v in params.items() if v is not None and k != 'self')