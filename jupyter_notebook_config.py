
# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from jupyter_core.paths import jupyter_data_dir
import subprocess
import os
import errno
import stat
import yaml
with open("/etc/jupyter/jupyter-config.yml", "r") as yml:
    config = yaml.safe_load(yml)
c = get_config()  # noqa: F821
c.NotebookApp.ip = "0.0.0.0"
c.NotebookApp.open_browser = False
c.NotebookApp.port = 8888
c.NotebookApp.notebook_dir = "/home/jovyan/work"
if config.get("password") is not None:
    c.NotebookApp.password = config["password"]
if config.get("token") is not None:
    c.NotebookApp.password = config["token"]

# https://github.com/jupyter/notebook/issues/3130
c.FileContentsManager.delete_to_trash = False

# Generate a self-signed certificate
if "GEN_CERT" in os.environ:
    dir_name = jupyter_data_dir()
    pem_file = os.path.join(dir_name, "notebook.pem")
    try:
        os.makedirs(dir_name)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(dir_name):
            pass
        else:
            raise

    # Generate an openssl.cnf file to set the distinguished name
    cnf_file = os.path.join(os.getenv("CONDA_DIR", "/usr/lib"), "ssl", "openssl.cnf")
    if not os.path.isfile(cnf_file):
        with open(cnf_file, "w") as fh:
            fh.write(
                """\
[req]
distinguished_name = req_distinguished_name
[req_distinguished_name]
"""
            )

    # Generate a certificate if one doesn't exist on disk
    subprocess.check_call(
        [
            "openssl",
            "req",
            "-new",
            "-newkey=rsa:2048",
            "-days=365",
            "-nodes",
            "-x509",
            "-subj=/C=XX/ST=XX/L=XX/O=generated/CN=generated",
            f"-keyout={pem_file}",
            f"-out={pem_file}",
        ]
    )
    # Restrict access to the file
    os.chmod(pem_file, stat.S_IRUSR | stat.S_IWUSR)
    c.NotebookApp.certfile = pem_file

# Change default umask for all subprocesses of the notebook server if set in
# the environment
if "NB_UMASK" in os.environ:
    os.umask(int(os.environ["NB_UMASK"], 8))
