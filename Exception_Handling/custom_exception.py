from typing import Any

class HardwareError(Exception):
    def __init__(self, message:str, value: Any) -> None:
        super().__init__(message) #let exception store the message via [super().__init__(message)]
        self.message = message
        self.value = value

    def __str__(self) -> str:
        return f'{self.message} (Value: {self.value})'
    
try:
    raise HardwareError(message="Laptop is too hot", value=101)
except HardwareError as e:
    print(e.args)
