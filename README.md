# Email Sender
  Build docker container using this command:
  ```
   docker build -t mailer .
  ```
  Run command:
  ```
   docker run -t -p 8080:80 mailer
  ```

## Testing code

  ```
   pytest tests/test.py
  ```

## Pull from Dockerhub

 ```
   docker pull algalyq/mailer
  ```
