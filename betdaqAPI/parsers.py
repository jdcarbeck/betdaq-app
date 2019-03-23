

def parse_sports(sport):
    return {'display_order': sport.get('DisplayOrder'),
            'sport_id': sport.get('Id'),
            'sport_name': sport.get('Name')}
