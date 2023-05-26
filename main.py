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
            f"{sys.executable} -m pip install pip install git+https://{st.secrets['github_token']}@github.com/almeidava93/icpc_annotation.git",
        ],
        shell=True,
    )

    # wait for subprocess to install package before running your actual code below
    time.sleep(sleep_time)
    # remove the installing dependency warning
    dependency_warning.empty()

def auth():
    st.text_input('Please, give us your access code...', type='password', key='password')

    if st.session_state['password'] != '':
        if st.session_state['password'] == st.secrets['password']:
            return True
        else:
            st.warning('Wrong access code. Please try again or talk to your provider.')

if auth():
    annotation.app()

