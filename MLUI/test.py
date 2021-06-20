from MLAPI import Api
import pandas as pd

cnt_month = Api.predict(pd.DataFrame(data={"ID": [0, 3], "shop_id": [4, 25], "item_id": [5037, 253]}), is_path=False)
print(cnt_month.head())