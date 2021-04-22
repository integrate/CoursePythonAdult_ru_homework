set base_dir=%~dp0..\..

call scripts\remove_all.bat


pip install -e %base_dir%\wds_files_CoursePythonAdult_1
pip install -e %base_dir%\wrap_mENdRU

pip install CoursePythonAdult-ru==0.1.1 --no-cache-dir