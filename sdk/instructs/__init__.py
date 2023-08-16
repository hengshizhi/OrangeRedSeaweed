def check_instructions(instructions, instruction_table, dependency_table):
    '''Judging the rationality of instructions
    instructions :instruction set
    instruction_table :Supported Instruction Tables
    dependency_table :Instruction Dependency Table
    '''
    invalid_instructions = []
    for i in range(len(instructions)):
        if isinstance(instructions, dict):
            instruction = instructions[i]['instruction_name']
        else:
            instruction = instructions[i]
        if instruction not in instruction_table:
            invalid_instructions.append(instruction)
        else:
            dependencies = dependency_table.get(instruction, []) 
            for dependency in dependencies:
                if dependency not in instructions[:i]:
                    invalid_instructions.append(instruction)
                    break
    return invalid_instructions
class instruction_parameters():
    def __init__(self,instruction_parameters_data:dict|None) -> None:
        self.parameters = instruction_parameters_data
    def get(self,parameter_name:str) -> str|bool|None:
        '''
        If False is return, then parameter not found \n
        If None is return, then No parameters used, parameters not found \n
        '''
        try:
            return self.parameters.get(parameter_name)
        except KeyError:
            return False
            raise KeyError(f'parameter not found:{parameter_name}')
        except AttributeError:
            return None
            raise AttributeError(f"No parameters used, parameters not found:'{parameter_name}'")
class Execution:
    def __init__(self,instruction,instruction_name_list:list,instruction_func_list:list,global_parameters:dict):
        '''Responsible for parsing each instruction'''
        self.instruction = instruction
        self.instruction_name_list = instruction_name_list
        self.instruction_func_list = instruction_func_list
        self.global_parameters = global_parameters # global's parameters
    def extract_command(self):
        if isinstance(self.instruction, dict):
            self.instruction_name = self.instruction['instruction_name']
            self.instruction_parameters = instruction_parameters(self.instruction['instruction_parameters'])
        else:
            self.instruction_name = self.instruction
            self.instruction_parameters = instruction_parameters(instruction_parameters_data=None)
        if type(self.global_parameters) == dict: # add global's parameters
            self.instruction_parameters.parameters.update(self.global_parameters)
    def execute(self):
        '''Execute the instruction'''
        try:
            self. extract_command()
            if self.instruction_name in self.instruction_name_list:
                # Call the corresponding method based on the instruction name
                if isinstance(self.instruction_func_list, list):
                    result = self.instruction_func_list[self.instruction_name_list.index(self.instruction_name)](self.instruction_parameters)
                else:
                    # Extract functions from modules through strings
                    result = getattr(self.instruction_func_list, self.instruction_name)(self.instruction_parameters)
                return result
            else:
                raise ValueError(f"Invalid instruction: {self. instruction_name}")
        except Exception as e:
            # Handle the error appropriately
            ep = f"Error executing instruction: {e}"
            return ep

    def _execute_example_instruction(self, parameters):
        # Implement the logic for executing the "example_instruction" here
        # Use the parameters as needed
        # Return the result of the execution
        pass

def run(instruction_set: list,
        instruction_name_list:list,
        instruction_func_list:list|object,
        dependency_table:dict={},
        global_parameters:dict|None = None) -> list:
    '''This function is a function that utilizes the instruction set to operate on another
    Parameters:
        instruction_set: Instruction set, which is a list of dictionaries:
        >>> instruction_set = [{'instruction_name': "<instruction_name>", <instruct_parameters>...}]
        >>> instruction_name_list = [<instruct1>,<instruct2>,...]
        >>> instruction_func_list = [<instruct_func1>,<instruct_func2>,...]
        >>> global_parameters = {'other':<other:obj>}
        >>> # instruction_func_list = module_name # Extract functions from modules through strings
        >>> dependency_table = {<instruct1>:[<instruct2>,<instruct3>],...} 
        >>> # Instructions: dependent instructions of instructions (Need to execute an instruction dependent instruction first)
        >>> def instruct_func1(parameters:dict({'parameters':value})|None):
        >>>     return <execution_results>
    Usage method:
        >>> run(instruction_set,instruction_name_list,instruction_func_list,dependency_table,global_parameters)
    '''
    if not dependency_table == {} :

        invalid_instructions = check_instructions(instruction_set,instruction_name_list,dependency_table)

        if invalid_instructions:
            e = 'The following instructions have dependency issues: '
            for invalid_instruction in invalid_instructions:
                e += f'"{invalid_instruction}",'
            raise ValueError(e)

    # Define a helper function for executing a single instruction
    def execute_instruction(instruction):
        executor = Execution(instruction,instruction_name_list,instruction_func_list,global_parameters)
        return executor.execute()

    # Execute instructions synchronously
    results = []
    for instruction_index in range(len(instruction_set)):
        results.append(execute_instruction(instruction_set[instruction_index]))

    return results

def mod_js():
    from fileApi.file import New as file
    f = file('.\sdk\instructs\\')
    return f.openr('requests_instructs.js')