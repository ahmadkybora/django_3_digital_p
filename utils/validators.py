from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

class PhoneNumberValidator(RegexValidator):
    regex = '^98(9[0-3,9]\d{8}|[1-9]\d{9}$'
    message = _('Phone')
    code = 'invalid phone'

class SKUVlidator(RegexValidator):
    regex = '^[a-zA-Z0-9\-\_]{6-20}$'
    message = _('SKU')
    code = 'Invalid Sku'

class UsernameValidator(RegexValidator):
    regex = '^[a-zA-Z][a-zA-Z0-9_\.]+$'
    message = _('Username')
    code = 'Invalid Username'

class PostalCodeValidator(RegexValidator):
    regex = '^[0-9]{10}$'
    message = _('Post')
    code = 'Invalid Post'

class IDNumber(RegexValidator):
    regex = '^[0-9]{10}$'
    message = _('IDNumber')
    code = 'Invalid IDNumber'

class IBanNumberValidator(RegexValidator):
    regex = '^[a-zA-Z]{2}[0-9]{2}[a-zA-Z0-9]{4}[0-9]{7}([a-zA-Z0-9]?){0,16}$'
    message = _('IBanNumber')
    code = 'Invalid IBanNumber'

class BankCardNumberValidator(RegexValidator):
    regex = '^[0-9]{16}$'
    message = _('bank Card')
    code = 'Invalid bank card'

validate_phone_number = PhoneNumberValidator()
validate_sku = SKUVlidator()
validate_username = UsernameValidator()
validate_postal_code = PostalCodeValidator()
validate_id_number = IDNumber()
validate_iban_number = IBanNumberValidator()
validate_bank_card_number = BankCardNumberValidator()
