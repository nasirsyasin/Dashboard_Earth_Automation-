import pytest

from Pages.Mobile_pages.KillAndRelaunch import KillAndRelaunch


class AppRefresh:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(AppRefresh, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        pass

    @pytest.mark.csv
    def app_refresh(self):
        app = KillAndRelaunch()
        app.app_refresh()
