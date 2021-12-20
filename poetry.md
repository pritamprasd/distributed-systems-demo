curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

poetry add pendulum
poetry add pendulum@^2.0.5
poetry add git+ssh://git@github.com/sdispater/pendulum.git#develop
poetry add ./my-package/
poetry add ../my-package/dist/my-package-0.1.0.tar.gz
poetry add ../my-package/dist/my_package-0.1.0.whl

poetry remove pendulum

poetry run python your_script.py  # executes the given command inside the project’s virtualenv
poetry run pytest 

poetry shell
poetry check #  structure of the pyproject.toml

poetry install
poetry install --no-dev
poetry install --remove-untracked
poetry install --no-root # skip self installation

poetry build  -> sdist and wheel both :D:D:D:D:D

poetry publish
poetry publish -r my-repository

poetry show

poetry new my-package
poetry new my-folder --name my-package
poetry new --src my-package   # <-- use dis -->

poetry cache list


source "$( poetry env list --full-path | grep Activated | cut -d' ' -f1 )/bin/activate"