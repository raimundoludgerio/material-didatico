from flask import Flask, render_template
app = Flask(__name__)

@app.route('/activate_user/<int:id>', methods=['POST'])
def activate_user(id):
    user = User.query.get(id)
    if not user:
        return {"error": "User not found"}, 404
    if user.is_active:
        return {"message": "Already active"}, 400
    user.is_active = True
    db.session.commit()
    return {"message": "User activated"}, 200

@app.route('/activate_user/<int:id>', methods=['POST'])
def activate_user(id):
    use_case = ActivateUserUseCase(repository=UserSQLAlchemyRepository())
    result = use_case.execute(user_id=id)
    return result.to_json(), result.status_code


if __name__ == '__main__':
    app.run(debug=True)
