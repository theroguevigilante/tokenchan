tokenchan - a simple flask api, which helps to create unique tokens for easter, eggs on a static site.

the process looks something like this
you send a request -> it generate a token -> provides the token as text output

setup:
    1st -> using uv:
        1. clone the repo

        2. create a venv using ``` uv venv ```
            activate the venv ``` source .venv/bin/activate ```

        3. install flask ``` uv pip install flask ```

        4. add your secret key in main.py
            in case, you don't have a secret key you can generate a random one using,
                ``` python -c 'import secrets; print(secrets.token_hex())' ```

        5. run the flask app using ``` flask --app main.py run ```


if you have any query, contact me.
