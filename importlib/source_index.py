import importlib.util

def import_source(module_name):

    module_file_path = module_name.__file__

    module_name = module_name.__name__
    print('v')
    print(module_name)
    print('v')
    module_spec = importlib.util.spec_from_file_location(module_name,module_file_path)
    print('b')
    print(module_spec)
    print('b')
    module = importlib.util.module_from_spec(module_spec)
    print('a')
    print(module)
    print('a')
    module_spec.loader.exec_module(module)

    print(dir(module))

    msg = "The {module_name} module has the following methods:{methods}"

    print(msg.format(module_name = module_name,methods = dir(module)))

if __name__ == "__main__":

    import logging

    import_source(logging)