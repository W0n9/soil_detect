#%%
import time
content = {'device_id': 'sdfs'}
payload = [
    '005', 'WORLDFUL', content['device_id'],
    time.strftime("%Y-%m-%d %H:%M", time.localtime()), '494C,8F7D'
]
# %%
