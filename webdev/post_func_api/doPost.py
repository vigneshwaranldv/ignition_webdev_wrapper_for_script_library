## WebDev ##
## name: post_func_api

def doPost(request, session):
    import system
    import sys
    logger_name = '<webdev-name-or-unique-identifiable-name>'
    try:
        if 'postData' not in request: raise Exception('Invalid or No Payload sent for function call')

        request_payload = request['postData']
        # log as info with this details 'request_payload'
        # if execute_func_args_kwargs function is inside package/sub-package/module etc.. use FQN
        func_result = func_api_interface.execute_func_args_kwargs(request_payload)
        
        return {'json':system.util.jsonEncode(func_result)}
    except:
        error_message = str(sys.exc_info())
        # log as error - error_message
        return None
