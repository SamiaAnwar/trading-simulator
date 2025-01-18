from app import create_app
from model import create_model
app = create_app()
selected_features = create_model()
if __name__ == "__main__":
    app.run(debug=True)