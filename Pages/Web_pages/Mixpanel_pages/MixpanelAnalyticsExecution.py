import time
import pytest
from Pages.Web_pages.Mixpanel_pages.CompostEventsVerification import CompostEventsVerification
from Pages.Web_pages.Mixpanel_pages.EwasteEventsVerification import EwasteEventsVerification
from Pages.Web_pages.Mixpanel_pages.MixpanelExportEvents import MixpanelExportEvents


class MixpanelAnalyticsExecution:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MixpanelAnalyticsExecution, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        pass

    @staticmethod
    def export_events():
        mxp_events = MixpanelExportEvents()
        mxp_events.export_events()

    @staticmethod
    def compost_result():
        mxp_cmp = CompostEventsVerification()
        mxp_cmp.verify_compost_events()

    @staticmethod
    def ewaste_result():
        mxp_ew = EwasteEventsVerification()
        mxp_ew.verify_ewaste_events()

# if __name__ == "__main__":
#     verification = MixpanelAnalyticsExecution()
#     verification.export_events()
#     verification.compost_result()
#     verification.ewaste_result()
#     pytest.main()
