"""
function_name: execute_func_args_kwargs
input_parameter: a dict payload that has keys for function name to execute with keys [args and kwargs] passed

author: Vigneshwaran Pandian

param_name: func_payload_dict
param_type: python dict
param_schema: {
                'func_name': '<FUNCTION_NAME>',
                'func_args': [arg_1, arg_2, .....arg_n],
                'func_kwargs':{'arg_name_1':arg_1, 'arg_name_2':arg_2, .....'arg_name_n':arg_n}
            }

Example:
# a function to call = package_1.sub_package_2.module_3.func_name(param_1)
# this can be called in 2 ways as args(arguments) or kwargs(keyword-args)
1. package_1.sub_package_2.module_3.func_name(param_val_1)
2. package_1.sub_package_2.module_3.func_name(param_1=param_val_1)

for #1 => the , args = [param_val_1] and kwargs = {}
for #2 => the , args = [] and kwargs = {param_1:param_val_1}

this function can handle both the scenarios:
example usage #1:
func_payload_dict = {
                        'func_name':'package_1.sub_package_2.module_3.func_name', 
                        'func_args':[param_val_1]
                    }
--OR--
example usage #2:
func_payload_dict = {
                        'func_name':'package_1.sub_package_2.module_3.func_name', 
                        'func_kwargs':{'param_1':param_val_1}
                    }

"""

import sys
logger_name = "execute_func_main"

def execute_func_args_kwargs(func_payload_dict):
    """ This function takes the func_payload_dict, which contains the functiona name and params for child/function-to-execute"""
    try:
        func_path = func_payload_dict.get('func_name')
        args = func_payload_dict.get('func_args',[])
        kwargs = func_payload_dict.get('func_kwargs',{})

        func_pack_path_parts = func_path.split('.')
        current_obj = globals()

        for f_pack in func_pack_path_parts[:-1]:
            if isinstance(current_obj, dict) or 'stringmap' in str(type(current_obj)).lower():
                current_obj = current_obj.get(f_pack)
            else:
                current_obj = getattr(current_obj, f_pack)
        
        func = getattr(current_obj, func_pack_path_parts[-1])
        
        return func(*args, **kwargs)
    except:
        error_message = ''
        if func_path: error_message = str(func_path)+'|'+str(args)+'|'+str(kwargs)

        error_message += str(sys.exc_info())
        # log the error with logger_name and error_message
        return None
