import logging as logger, random, string


def generate_random_email_and_password(domain=None, email_prefix=None):

    logger.debug("Generating random email and password.")

    if domain == None:
        domain = 'omatest.com'
    if email_prefix == None:
        email_prefix = 'testuser'

    random_email_string = ''.join(random.choices(string.ascii_lowercase, k=10)) # k is length of string generated 

    email = f'{email_prefix}_{random_email_string}@{domain}'

    password = ''.join(random.choices(string.ascii_letters, k=20)) # k is length of string generated

    random_info = {'email': email, 'password': password}

    logger.debug(f'Randomly generated email and password: {random_info}')

    return random_info

def generate_random_name(length, prefix=None, suffix=None):

    logger.debug('Generating a random name.')

    random_name = ''.join(random.choices(string.ascii_lowercase, k=int(length))) # k is length of string generated 

    if prefix:
        random_name = prefix + random_name
    if suffix:
        random_name = random_name + suffix

    return random_name