"""
你想排序类型相同的对象，但是他们不支持原生的比较操作。
"""

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return f"User({self.user_id})"

def sort_user_demo(users):
    print(f"原始列表: {users}")

    # 使用 sorted() 排序
    print(f"使用 sorted() 排序: {sorted(users, key=lambda u: u.user_id)}")

    # 使用 list.sort() 排序
    users.sort(key=lambda u: u.user_id)
    print(f"使用 list.sort() 排序: {users}")

from operator import attrgetter

users_out = [User(23), User(3), User(99)]
print(f"原始列表: {users_out}")
print(f"使用 operator.attrgetter 排序: {sorted(users_out, key=attrgetter('user_id'))}")

sort_user_demo(users_out)