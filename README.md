# Test-notebook



Jupyter-config.ymlに

```python
from notebook.auth import passwd

my_password = "my_password"

hashed_password = passwd(passphrase=my_password, algorithm='sha256')

print(f"password: {hashed_password}")
```

の出力を入れる。
以下のコマンドでdocker imageを作成
```sh
docker build -t testnotebook .
```
その後作業したいディレクトリで以下を実行すればnotebookが使えるようになる。
```sh
docker run -p 8892:8888 -v $(pwd):/home/jovyan/work/ -d --name testnotebook testnotebook
```
