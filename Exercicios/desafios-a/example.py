user = User.query.filter_by(email=email).first()  
if user and user.is_active:  
    user.last_login = datetime.utcnow()  
    db.session.commit()
