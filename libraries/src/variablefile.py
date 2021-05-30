def get_variables(enviroment):
    enviroment = enviroment.strip().lower()
    if enviroment == "prod":
        return prod()
    elif enviroment == "preprod":
        return preprod()
    elif enviroment == "test":
        return test()
    else:
        message = ('Could not match to predefined enviroments: Use prod, preprod, test')
        print (message)
        return prod()

def default_var():
    main_dictionary = {}
    # Add here variables
    return main_dictionary

def prod():
    main_dictionary = default_var()
    # Add here variables
    main_dictionary['STACKOVERFLOW_LOGIN_URL'] = 'https://stackoverflow.com/users/login'
    main_dictionary['STACKOVERFLOW_TEAMS_URL'] = 'https://stackoverflow.com/teams'
    main_dictionary['FOOBAR_URL'] = 'http://www.foobar.com/login'
    return main_dictionary

def preprod():
    main_dictionary = default_var()
    # Add here variables
    main_dictionary['STACKOVERFLOW_LOGIN_URL'] = None
    main_dictionary['STACKOVERFLOW_TEAMS_URL'] = None
    main_dictionary['FOOBAR_URL'] = None
    return main_dictionary

def test():
    main_dictionary = default_var()
    # Add here variables
    main_dictionary['STACKOVERFLOW_LOGIN_URL'] = None
    main_dictionary['STACKOVERFLOW_TEAMS_URL'] = None
    main_dictionary['FOOBAR_URL'] = None
    return main_dictionary
