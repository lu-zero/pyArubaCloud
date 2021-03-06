class ValidationError(Exception):
    def __init__(self, message):
        super(ValidationError, self).__init__(message)


class OperationNotPermitted(Exception):
    def __init__(self, message):
        super(OperationNotPermitted, self).__init__(message)


class MalformedJsonRequest(Exception):
    def __init__(self, message):
        super(MalformedJsonRequest, self).__init__(message)