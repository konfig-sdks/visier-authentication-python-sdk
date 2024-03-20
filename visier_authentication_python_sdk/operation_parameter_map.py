operation_parameter_map = {
    '/v1/admin/visierSecureToken-POST': {
        'parameters': [
            {
                'name': 'username'
            },
            {
                'name': 'password'
            },
        ]
    },
    '/v1/auth/oauth2/authorize-GET': {
        'parameters': [
            {
                'name': 'response_type'
            },
            {
                'name': 'client_id'
            },
            {
                'name': 'redirect_uri'
            },
            {
                'name': 'scope'
            },
        ]
    },
    '/v1/auth/oauth2/token-POST': {
        'parameters': [
            {
                'name': 'grant_type'
            },
            {
                'name': 'client_id'
            },
            {
                'name': 'redirect_uri'
            },
            {
                'name': 'code'
            },
            {
                'name': 'username'
            },
            {
                'name': 'password'
            },
            {
                'name': 'asid_token'
            },
        ]
    },
    '/v1/admin/visierSecureTicket-POST': {
        'parameters': [
            {
                'name': 'username'
            },
            {
                'name': 'password'
            },
        ]
    },
};