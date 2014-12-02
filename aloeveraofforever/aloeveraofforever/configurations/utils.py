from configurations.models import Configuration

def build_config_hash(filterString=None):
    config = {}
    for c in Configuration.objects.all():
        if (not filterString) or (filterString in c.name): 
            config[c.name] = str(c.value).rstrip()
    return config
