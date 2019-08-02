
#!/bin/bash
node ./spec/genApi.js
node ./spec/genDocs.js

deactivate
source venv/bin/activate

python bump_version.py

rm -rf iotery_embedded_python_sdk.egg-info/ && rm -rf build/ && rm -rf dist/ &&

python setup.py sdist bdist_wheel &&

python -m pip install --upgrade twine &&

python -m twine upload dist/*

git add .
git commit -m "doc update"
git push origin master