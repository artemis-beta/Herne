class singleton(type):
    _loaded = {}
    def __call__(app, *args, **kwargs):
        if app not in app._loaded:
            _super = super(singleton, app)
            app._loaded[app] = _super.__call__(*args, **kwargs)
        return app._loaded[app]

class app_run(object, metaclass=singleton):
    __apps__ = []
    def __add__(self, other):
        self.__apps__.append(other)
    def __iter__(self):
        for i in self.__apps__:
            yield i
    def __str__(self):
        return self.__apps__.__str__()
