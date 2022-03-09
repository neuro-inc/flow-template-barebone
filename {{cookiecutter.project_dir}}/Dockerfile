FROM {{ cookiecutter.base_image }}

COPY requirements.txt requirements.txt
RUN pip install --progress-bar=off -U --no-cache-dir -r requirements.txt