from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config['JSON_AS_ASCII'] = False

"""
Создание моделей
"""


class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    foundation_year = db.Column(db.Integer, nullable=False)
    web_site = db.Column(db.String)
    is_opening = db.Column(db.Boolean, nullable=False)


db.create_all()

"""
Запись данных
"""
restaurant = []

restaurant.append(Restaurant(name="Paloma Cantina",
                              address="Садовая 8/7",
                              description="Ресторан с простой мексиканской едой",
                              foundation_year=2018,
                              is_opening=True))
restaurant.append(Restaurant(name="Birch",
                              address="Кирочная д.3",
                              description="European food with Asian influence",
                              foundation_year=2015,
                              web_site="http://birchrest.com/",
                              is_opening=True))
restaurant.append(Restaurant(name="Harvest",
                              address="Пр. Добролюбова, 11",
                              description="Ресторан с особым отношением к овощам и философией ответственного потребления от @duoband",
                              foundation_year=2015,
                              web_site="https://harvestduo.ru/",
                              is_opening=True))

db.session.add_all(restaurant)
db.session.commit()


"""
 Просмотр записей
"""

restaurants = db.session.query(Restaurant).all()
for restaurant in restaurants:
    print(restaurant.name)


app.run(debug=True)