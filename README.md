# Test-notebook



Jupyter-config.ymlに

```python
from notebook.auth import passwd

my_password = "my_password"

hashed_password = passwd(passphrase=my_password, algorithm='sha256')

print(f"password: {hashed_password}")
```

の出力を入れる。