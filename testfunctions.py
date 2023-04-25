import re

# def validate_phone_number(client_subitted_phone_number):
#     if "(" in client_subitted_phone_number:
#         if '-' in client_subitted_phone_number:
#             return re.match(r"\(\d{3}\) \d{3}-\d{4}", client_subitted_phone_number)
#         else:
#             return re.match(r"\(\d{3}\)\d{3}\d{4}", client_subitted_phone_number)
#     else:
#         if '-' in client_subitted_phone_number:
#             return re.match(r"^\d{3}-\d{3}-\d{4}$", client_subitted_phone_number)
#         else:        
#             return re.match(r"^\\?[1-9][0-9]{7,14}$", client_subitted_phone_number)

def validate_phone_number(client_subitted_phone_number):
    phone_regex = '^\d{3}-\d{3}-\d{4}$'
    match = re.search(phone_regex, client_subitted_phone_number)
    return match
        
if __name__ == '__main__':
    if validate_phone_number('812-336-1189'):
        print('good jobbing')
    else:
        print('die forever')