# IEEE LED Arcade Workshop Part 2

To setup a virtualenv on in your project directory

```bash
python3 -m venv .venv
```

To activate the virtualenv to test your code

```bash
source .venv/bin/activate
```

To deactivate the virtualenv

```bash
deactivate
```

To run Flask program in Unix/Linux

```bash
chmod +x run_flask  # Do this only for the first run
./run_flask
```

To run Flask program in Windows

```bat
run_flask.bat
```

To initialize the database after writing the database schema

```bash
export FLASK_APP=flaskr
flask init-db
```

or in Windows

```bat
SET FLASK_APP=flaskr
flask init-db
```