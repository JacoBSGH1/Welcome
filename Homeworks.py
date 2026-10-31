# 12.10
'''
def check_if_valid_email(email):
    is_valid = False
    if email.find('@') != -1:
        at = email.find('@')
        if email.find(' ') == -1:
            if email.find('.', at+1) != -1:
                is_valid = True
    return is_valid
print(check_if_valid_email('123gmail.com')) # False, lack of @
print(check_if_valid_email('12 3@gmail.com')) # False, space in address
print(check_if_valid_email('12.3@gmailcom')) # False, lack of . in domain
print(check_if_valid_email('123@gmail.com')) # True
'''
# 19.10
# done in files/file_csv_read and folder_operations





