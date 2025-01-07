FROM python:3.11-slim AS build
WORKDIR /src
COPY requirements.txt /src
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.9-slim
WORKDIR /src
COPY --from=build /usr/local /usr/local
COPY . /src
MAINTAINER Aleksey Zinovjev alexz04tab2@gmail.com
ENV APP_VERSION="1.0"
RUN useradd -ms /bin/bash user
USER user
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
