import re

def validate_card_number(card_number):
    # Comprovació bàsica del número de targeta (exemple: longitud i només números)
    if len(card_number) == 16 and card_number.isdigit():
        return True
    return False

def validate_expiration_date(expiration_date):
    # Comprovació bàsica de la data de caducitat
    today = datetime.date.today()
    if expiration_date > today:
        return True
    return False

def validate_cvc(cvc):
    # Comprovació bàsica del cvc
    if len(cvc) == 3 and cvc.isdigit():
        return True
    return False
