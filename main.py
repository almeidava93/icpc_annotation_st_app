import subprocess
import sys
import streamlit as st
import time

try:
    from icpc_annotation import annotation

# This block executes only on the first run when your package isn't installed
except ModuleNotFoundError as e:
    sleep_time = 30
    dependency_warning = st.warning(
        f"Installing dependencies, this takes {sleep_time} seconds."
    )
    subprocess.Popen(
        [
            f"{sys.executable} -m git clone https://oauth2:{st.secrets['github_token']}@github.com/almeidava93/icpc_annotation_st_app.git",
        ],
        shell=True,
    )

    # wait for subprocess to install package before running your actual code below
    time.sleep(sleep_time)
    # remove the installing dependency warning
    dependency_warning.empty()

annotation.app()