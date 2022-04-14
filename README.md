# Test-notebook

以下のコマンドでdocker imageを作成

```sh
docker pull pn8128/base-notebook-nbextension
cd init_password
docker run -v $(pwd):/home/jovyan/work/ -d -it --rm pn8128/base-notebook-nbextension python3 work/init.py
mv jupyter-config.yml ../
cd ..
docker build -t testnotebook .
```

その後作業したいディレクトリで以下を実行すればnotebookが使えるようになる。

```sh
docker run -p 8892:8888 -v $(pwd):/home/jovyan/work/ -d --name testnotebook testnotebook
```
