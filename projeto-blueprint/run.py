from app import create_app

app = create_app()

# 5. Executar o aplicativo (se o script for executado diretamente)
if __name__ == '__main__':
    app.run(debug=True)