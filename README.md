# python-fastapi-template


###  Run application by docker

1. Create file .env by format .env.template .

2. Run the following commands to run docker.
    ```
        docker-compose -f docker-compose.yml up --build
    ```

3. Migration database by alembic.
    ```
        docker exec -it {CONTAINER_ID_SCRAPE_MASTER} bash 
        alembic upgrade head 
    ```

4. Access http://localhost:8000/docs to view documentation api.



###  Run application

1. Set up mysql.
    ```
        docker run -d -p 3306:3306 -e="MYSQL_ROOT_PASSWORD=my_password" -e="MYSQL_DATABASE=my_database" mysql
    ```

2. Create file .env by format .env.template .

3. Install poetry (You can skip it if you already have it installed).
    ```
        pip install poetry
    ```

4. Config poetry.
    ```
        poetry config virtualenvs.in-project true
    ```

5. Install python 3.10.4 by pyenv (You can skip it if you already have it installed).


6. Install mysqlclient dependency (You can skip it if you already have it installed).
    ```
        sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
    ```

7. Run install requirement by poetry.
    ```
        poetry install
    ```

8. Activate Python Virtual Environment.
    ```
        source .venv/bin/activate
    ```

9. Migration database by alembic.
    ```
        alembic upgrade head
    ```

10. Run application.
    ```
        sh scripts/start.sh 
    ```

11. Access http://localhost:8000/docs to view documentation api.



###  Install python 3.10.4 by pyenv

1. Install all required prerequisite dependencies.
    ```
        sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \
        libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
        libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
    ```

2. Download and execute installation script.
    ```
        curl https://pyenv.run | bash
    ```

3. Add the following entries into your ~/.bashrc file.
    ```
        export PATH="$HOME/.pyenv/bin:$PATH"
        eval "$(pyenv init --path)"
        eval "$(pyenv virtualenv-init -)"
    ```

4. Restart your shell.
    ```
        exec $SHELL
    ```

5. Validate installation.
    ```
        pyenv --version
    ```

6. Validate installation.
    ```
        pyenv install 3.10.4
    ```

7. Set a specific version of Python global.
    ```
        pyenv global 3.10.4
    ```

8. Set poetry use python 3.10.4.
    ```
        poetry env use 3.10.4
    ```