# Flask-File-Transfer-App

## HOW TO

### 1. Make sure you have Docker and Docker Compose installed
### 2. Create .env file in the same file as the docker-compose.yml. It should look like this:

DEBUG=True \
USERNAME=something \
SECRET_KEY=your_secret_key \
POSTGRES_DB=your_db_name \
POSTGRES_USER=your_username_for_postgres \
POSTGRES_PASSWORD=your_password_for_postgres \
DATABASE_HOST=localhost
DATABASE_PORT=5432 

### 3. Go in the docker-compose.yml folder and run `docker compose up --build` and here you are! Also, add `-d` if you want to run it in the background.

### To access your containers shell, run:
`docker exec -it container_name bash`