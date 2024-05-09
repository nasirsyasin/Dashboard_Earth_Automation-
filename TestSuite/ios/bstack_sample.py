import pytest

from TestSuite.Test_Suite_Smoke import test_suite


@pytest.mark.usefixtures('setWebdriver')
class TestSample:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(TestSample, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        pass

    run = test_suite()
    run.i_allow_app()
    run.test_login()
    run.test_AllowNotify()
    run.test_tooltips()
    run.test_trackAction()
    run.test_compost()
    run.test_ewaste()
    run.mixpanel_export()
    run.compost_verify()
    run.ewaste_verify()
