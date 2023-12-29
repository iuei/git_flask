# import jwt
# from datetime import datetime, timedelta
# from flask import current_app
#
#
# def generate_token(user_instance):
#     # 设置令牌有效期（示例为1小时）
#     expiration_time = datetime.utcnow() + timedelta(hours=1)
#
#     # 构建令牌的 payload
#     payload = {
#         'user_id': user_instance.id,
#         'username': user_instance.username,
#         'exp': expiration_time
#     }
#
#     # 使用 secret key 对 payload 进行签名生成令牌
#     token = jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')
#
#     return token.decode('utf-8')  # 将 bytes 转为字符串
