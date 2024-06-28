def obj_as_prop(name: str, model, kwarg_key='pk'):
    def prop(instance):
        under_name = f'_{name}'
        if hasattr(instance, under_name) and getattr(instance, under_name) is not None:
            pass
        else:
            obj_id = instance.kwargs.get(kwarg_key)
            setattr(instance, under_name, model.objects.get(pk=obj_id))
        return getattr(instance, under_name)

    def decorator(cls):
        setattr(cls, name, property(prop))
        return cls

    return decorator
