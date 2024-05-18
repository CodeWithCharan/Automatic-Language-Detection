# Automatic Language Detection

To access the application through FastAPI's Swagger UI: https://automatic-language-detection-app.onrender.com/docs

To access the application API endpoint, use [Postman](https://www.postman.com/) and paste the URL: https://automatic-language-detection-app.onrender.com/predict

## Docker

1. Pull the docker image:

    ```bash
    docker pull codewithcharan/language-detection-app:latest
    ```

2. Run the docker image:
    ```bash
    docker run -p 80:80 codewithcharan/language-detection-app:latest
    ```

3. Once the Docker container is running, the application will be accessible at:

- `http://localhost/docs`
- `http://127.0.0.1/docs`
- `YourIPv4Address/docs`

## Git

1. Clone the repository:

   ```bash
   git clone https://github.com/CodeWithCharan/Automatic-Language-Detection.git
   ```

2. Create a `virtual environment` (optional): [Virtual Environment Set Up](https://github.com/CodeWithCharan/virtual-env-setup)

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the main.py:

    ```bash
    cd app
    ```

    ```bash
    uvicorn main:app --reload
    ```

5. After running the app.py, it will be available at:

- `http://127.0.0.1:8000/docs`
- `http://localhost:8000/docs`

## OUTPUT SCREENS

In FastAPI's Swagger UI:

![Screenshot 2024-05-17 201718](https://github.com/CodeWithCharan/Automatic-Language-Detection/assets/106027109/a6139594-7b98-45f0-9e7b-954f15d790b3)

![Screenshot 2024-05-17 205230](https://github.com/CodeWithCharan/Automatic-Language-Detection/assets/106027109/90608b35-877b-483b-aa98-0e191341ba72)

In Postman:

![Screenshot 2024-05-17 210329](https://github.com/CodeWithCharan/Automatic-Language-Detection/assets/106027109/9f6b470a-246c-4c03-850e-3566aae9ad09)