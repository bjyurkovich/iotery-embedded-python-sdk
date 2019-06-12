deactivate

rm -rf iotery_python_server_sdk.egg-info/ && rm -rf build/ && rm -rf dist/ && rm -rf test_env/ &&

virtualenv test_env && source test_env/bin/activate &&

python setup.py sdist bdist_wheel &&

python -m pip install --upgrade twine &&

python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

