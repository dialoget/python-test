# python-test
python-test.dialoget.com - test repository 


## init
```bash
pip install --upgrade pip
pip install requests
pip install behave
pip install setuptools
pip install git+https://github.com/dialoget/python.git
chmod +x test.sh
```

## Start testing
with one bash script
```bash
./test.sh
```

or each script in command line

```bash
cd test/dialoget 
python3 update_repo_on_github.py
python3 update_repo_on_github2.py
python3 create_repo_on_org_github.py
```
