# IMPORTANT CONCEPT ON DECORATORS
# 1. When the module is first run, decorator gets executed and prints 'Entering the decorator' 
# 2. It also returns a reference to wrapper_singleton
# 3. Decorator on a class means the decorator is a wrapper over the class
# 4. Only when class instance is created(i.e. a callable is made) the actual wrapper_singleton method is called
# 5. First time this is one, therefore it goes ahead and creates an instance of the class it is wrapping. It now stores state by holding the instance of class
# 6. Next time the class instance is created, again only the callable(wrapper_singleton) is invoked .
# 7. This time it finds the instance, as the state was stored while creating an instance for the first time
# 8. Returns the same object with the same hash
# 9. These are STATEFUL DECORATORS

import functools

def singleton(cls):
    """Make a class a Singleton class (only one instance)"""
    print('Entering the decorator')
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
        	print('Creating instance of the class')
        	wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    
    wrapper_singleton.instance = None
    print(f'{wrapper_singleton.instance}')
    return wrapper_singleton



@singleton
class TheOne:
    pass



if __name__ == '__main__':
	f = TheOne()
	print(f'Id of first instance {id(f)}')
	'''
	s = TheOne()
	print(f'Id of first instance {id(s)}')

	'''