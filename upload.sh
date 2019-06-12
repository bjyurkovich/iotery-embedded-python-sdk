

rm -rf iotery_embedded_python_sdk.egg-info/ && rm -rf build/ && rm -rf dist/ &&

virtualenv test_env && source test_env/bin/activate &&

python setup.py sdist bdist_wheel &&

python -m pip install --upgrade twine &&

python -m twine upload dist/*

