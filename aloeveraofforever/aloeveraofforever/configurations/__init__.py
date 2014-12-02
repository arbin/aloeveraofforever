from models import Configuration

class AVFSettings(object):
    def __getitem__(self, key):
        config = Configuration.objects.filter(name=str(key))
        if config.exists():
            return config.get().value
        return None

    def __setitem__(self, key, value):
        config, created = Configuration.objects.get_or_create(name=str(key))
        config.value = str(value)
        config.save()

    def __delitem__(self, key):
        config = Configuration.objects.filter(name=str(key))
        if config.exists():
            config.delete()

settings = AVFSettings()