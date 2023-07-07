from sdk.other import Main as other
from InitialLoading import Cache

class Execution:
    instruction_name_list = ['example_instruction']

    def __init__(self, other: other, instruction):
        '''Responsible for parsing each instruction'''
        self.other = other
        self.instruction = instruction

    def extract_command(self):
        if isinstance(self.instruction, dict):
            self. instruction_name = self.instruction['instruction_name']
            self.instruction_parameters = self.instruction['instruction_parameters']
        else:
            self.instruction_name = self.instruction
            self.instruction_parameters = None
    def execute(self):
        '''Execute the instruction'''
        try:
            self. extract_command()
            if self.instruction_parameters in self.instruction_name_list:
                # Call the corresponding method based on the instruction name
                result = getattr(self, f'_execute_{self. instruction_name}')(self.instruction_parameters)
                return result
            else:
                raise ValueError(f"Invalid instruction: {self. instruction_name}")
        except Exception as e:
            # Handle the error appropriately
            ep = f"Error executing instruction: {e}"
            print(ep)
            return ep

    def _execute_example_instruction(self, parameters):
        # Implement the logic for executing the "example_instruction" here
        # Use the parameters as needed
        # Return the result of the execution
        pass

def operate(free_other_s_id: str, instruction_set: list) -> list:
    '''This function is a function that utilizes the instruction set to operate on another
    Parameters:
        free_other_s_id: The session ID of another, usually the cache name
        instruction_set: Instruction set, which is a list of dictionaries:
        [{'instruction_name': "<instruction_name>", <Other parameters of the instruction>...}]
    '''
    other_instance = Cache.GetCache(free_other_s_id).Pulling() # Get the other object from the cache instead of creating directly

    # Define a helper function for executing a single instruction
    def execute_instruction(instruction):
        executor = Execution(other=other_instance, instruction=instruction)
        return executor.execute()

    # Execute instructions synchronously
    results = [execute_instruction(instruction) for instruction in instruction_set]

    return results