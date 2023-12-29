# blueprint/routes/commodity_routes
from flask import Blueprint, jsonify, request
from models.models import db, commodity

bp_commodity = Blueprint('commodity', __name__, url_prefix='/commodity')


# 添加数据
@bp_commodity.route('/add', methods=['POST'])
def add_commodity():
    try:
        form_data = request.get_json()

        new_commodity = commodity(
            name=form_data.get('name', ''),
            price=form_data.get('price', ''),
            type=form_data.get('type', ''),
        )

        db.session.add(new_commodity)
        db.session.commit()

        return {'state': 0, 'msg': '添加成功'}
    except Exception as e:
        print(f"Error: {str(e)}")
        db.session.rollback()
        return {'state': 1, 'msg': '添加失败'}


@bp_commodity.route('/commodity', methods=['GET'])
def get_commodity():
    try:
        commodity_list = commodity.query.all()

        commodity_data = [
            {
                'id': commodity.id,
                'name': commodity.name,
                'price': commodity.price,
                'type': commodity.type,
            }
            for commodity in commodity_list
        ]

        return jsonify(commodity_data)
    except Exception as e:
        print(f"Exception: {str(e)}")
        return jsonify({'error': 'Failed to fetch commodity data'}), 500
