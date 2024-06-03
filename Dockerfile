FROM python:3.12


RUN apt-get update && apt-get install -y curl build-essential

ENV POETRY_VERSION=1.8.3
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN export PATH="$HOME/.local/bin:$PATH"
ENV PATH="/root/.local/bin:$PATH"


WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

COPY . .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable

# Run app.py when the container launches
CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]

#test to see if changes for poetry work