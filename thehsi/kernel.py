class CallData:
    remote = ('127.0.0.1', 0)

class Kernel:
    def __init__(self, app_name: str, app_id: str):
        self.__callers__: dict = {}
        self.app_name: str = app_name
        self.app_id: str = app_id
    
    def callable(self, path: str, name: str):
        def callable_function(func: callable):
            def wrapper(call_data: CallData, args: list):
                return func(call_data, args)
            self.__callers__[f'{path.removeprefix("/")}/{name}'] = {
                'name': name,
                'path': path.removeprefix('/'),
                'function': wrapper,
                'application_id': self.app_id,
                'application_name': self.app_name
            }
            return wrapper
        return callable_function