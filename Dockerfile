FROM pn8128/base-notebook-nbextension

COPY jupyter_notebook_config.py  jupyter-config.yml /etc/jupyter/
RUN sed -re "s/c.NotebookApp/c.ServerApp/g" \
    /etc/jupyter/jupyter_notebook_config.py > /etc/jupyter/jupyter_server_config.py && \
    fix-permissions /etc/jupyter/
WORKDIR "/home/jovyan/work"
