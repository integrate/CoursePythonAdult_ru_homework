set base_dir=%~dp0..\..

call scripts\remove_all.bat


pip install -e %base_dir%\pygame_wrap1
pip install -e %base_dir%\thread_signals
pip install -e %base_dir%\wrap_py
pip install -e %base_dir%\wrap_mENdRU
pip install -e %base_dir%\wrap_data_source
pip install -e %base_dir%\wds_files_CoursePythonAdult_1
pip install -e %base_dir%\CoursePythonAdult_ru