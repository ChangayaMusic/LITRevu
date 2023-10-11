from django import template
import importlib


register = template.Library()

@register.filter(name='instanceof')
def instanceof(instance, class_name):
    try:
        class_name = class_name.split('.')  # Split the class name into a list of its components
        module_name = '.'.join(class_name[:-1])  # Join the components except the last one (the class name)
        class_name = class_name[-1]  # Get the last component (the class name)

        # Import the module dynamically using the module name
        module = importlib.import_module(module_name)

        # Get the class by its name within the imported module
        class_type = getattr(module, class_name)

        return isinstance(instance, class_type)
    except (ImportError, AttributeError, ValueError) as e:
        return False

