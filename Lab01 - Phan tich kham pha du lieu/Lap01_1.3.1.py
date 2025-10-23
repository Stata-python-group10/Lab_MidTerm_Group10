#=====================================================
# PHẦN 3: PHÂN TÍCH ĐƠN BIẾN VÀ HAI BIẾN
#=====================================================
import numpy as np

# Vá tạm để Sweetviz hoạt động với NumPy 2.x
if not hasattr(np, "VisibleDeprecationWarning"):
    class VisibleDeprecationWarning(Warning):
        pass
    np.VisibleDeprecationWarning = VisibleDeprecationWarning

import pandas as pd
import sweetviz as sv

data = pd.read_csv(r"E:\Download\marketing_campaign.csv", encoding='ISO-8859-1')
data.columns = data.columns.str.strip()

report = sv.analyze([data, "marketing_campaign"], target_feat='Response')
report.show_html('report.html')