# blueprint/routes/user_routes
from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash
from models.models import db, user_list

bp_user = Blueprint('user', __name__, url_prefix='/user')


# 用户登录
@bp_user.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        user = user_list.query.filter_by(username=username).first()

        if user and user.check_password(password):
            return jsonify({"message": "登录成功", "user_info": {"username": user.username}})
        else:
            return jsonify({"message": "登录失败", "error": "用户名或密码无效"}), 401
    except Exception as e:
        print(f"登录过程中错误: {e}")
        return jsonify({"message": "登录失败，发生错误.", "error": str(e)}), 500


# 注册
@bp_user.route('/register', methods=['POST'])
def register():
    try:
        form_data = request.get_json()
        username = form_data.get('username', '')
        password = form_data.get('password', '')
        cell = form_data.get('cell', '')

        existing_user = user_list.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({'state': -1, 'msg': '用户名已存在'})

        hashed_password = generate_password_hash(password)

        new_user = user_list(
            username=username,
            password=hashed_password,
            cell=cell,
        )

        db.session.add(new_user)
        db.session.commit()

        return {'state': 0, 'msg': '注册成功'}
    except Exception as e:
        print(f"Error: {str(e)}")
        db.session.rollback()
        error_message = str(e) if str(e) else '未知错误'
        return {'state': -1, 'msg': f'Operation failed: {error_message}'}


# 加载用户信息
@bp_user.route('/user', methods=['GET'])
def get_users():
    try:
        users = user_list.query.all()

        user_data = [
            {
                'id': user.id,
                'username': user.username,
                'cell': user.cell,
                'sex': user.sex,
                'address': user.address
            }
            for user in users
        ]

        return jsonify(user_data)
    except Exception as e:
        return jsonify({'error': '获取用户列表失败'}), 500
