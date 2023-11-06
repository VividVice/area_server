
class UnknowService(Exception):
    def __init__(self, service_name):
        self.service_name = service_name

    def __str__(self):
        return f"Unknow service: {self.service_name}"

class FailedExecution(Exception):
    def __init__(self, service_name):
        self.service_name = service_name

    def __str__(self):
        return f"Failed to execute service: {self.service_name}"

class UnknowUser(Exception):
    """Raise when a user is not found in the database."""
    def __init__(self, username) -> None:
        self.username = username

    def __str__(self) -> str:
        return f'User {self.username} is not found in the database.'

class InvalideAREA(Exception):
    """"Raise when there are invalide parameters for action or reaction in AREA during setup."""
    def __init__(self, service_name, invalide_params) -> None:
        self.service_name = service_name
        self.invalide_params = invalide_params

    def __str__(self) -> str:
        return f'Invalide parameters for {self.service_name} service: {self.invalide_params}'

class AuthCompromisedError(Exception):
    """Raise when the user's authentication is compromised."""
    def __init__(self, username, service) -> None:
        self.username = username
        self.service = service

    def __str__(self) -> str:
        return f'User {self.username}\'s authentication for {self.service} is compromised.'