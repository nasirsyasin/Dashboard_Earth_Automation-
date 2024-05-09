from Utility.mobile_driver_setup import AppiumDriverSingleton


class KillAndRelaunch:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(KillAndRelaunch, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        pass

    def __init__(self):
        self.driver = AppiumDriverSingleton().get_driver

    def app_refresh(self):
        self.driver.close_app()
        self.driver.launch_app()
