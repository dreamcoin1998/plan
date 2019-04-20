import plan.settings


def proxy():
    if plan.settings.USE_PROXY:
        # add your proxy here
        return {}
    else:
        return {}