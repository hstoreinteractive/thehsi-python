from os.path import exists, dirname
from thehsi import CallData, Kernel
from os import listdir

def is_module_valid(module):
    valid_chars: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_"
    return not bool(
        len(
            list(
                filter(
                    lambda x : x,
                    [not i in valid_chars for i in module]
                )
            )
        )
    )

def load_callers():
    file_root: str = ""
    file_root: str = str(
        dirname(
            __file__
        ).replace(
            "\\",
            "/"
        ) # Windows Support
    )

    file_path: str = ""
    file_path: str = __file__.replace(
        "\\",
        "/"
    )

    if not file_root in file_path:
        raise ValueError(
            "File directory is not in File path"
        )

    applications: list[str] = []
    applications: list[str] = list(
        listdir(
            f"{file_root}/applications/"
        )
    )

    callers: dict[dict] = {}

    for application in applications:
        if not is_module_valid(application):
            print(f"[WARNING]: Application '{application}' could not be loaded!\n  The application has an invalid name\n")
            continue
        if not exists(
            f'{file_root}/applications/{application}/__hmgr_caller__.py'
        ):
            continue
        application_caller = __import__(
            f'applications.{application}.__hmgr_caller__'
        )
        kernel: Kernel = application_caller.__hmgr_caller__.kernel
        if kernel.app_id != application:
            print(f"[WARNING]: Application '{application}' could not be loaded!\n  The application folder name must match the id\n")
            continue
        application_callers: dict = kernel.__callers__
        for caller_key in application_callers.keys():
            caller = application_callers[caller_key]
            callers[
                f"{caller['application_id']}:{caller_key}"
            ] = caller

    return callers

def call(callers: dict, caller_key: str, args: list = []):
    if not caller_key in callers:
        print(f"[ERROR]: Cannot Call '{caller_key}'\n  No such call\n")
        return
    call_data: CallData = CallData()
    caller: dict = callers[caller_key]
    func: callable = caller['function']
    return func(call_data, args)