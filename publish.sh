rm -rf dist
rm -rf build
rm -rf rdwebuiapi.egg-info
python3 setup.py bdist_wheel
twine upload dist/*
