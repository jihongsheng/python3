# -*- coding: UTF-8 -*-
# 还有些时候，确定特定的值未包含在列表中很重要；在这种情况下，可使用关键字not in 。例如，
# 果有一个列表，其中包含被禁止在论坛上发表评论的用户，就可在允许用户提交评论前检查他是否被禁言：
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
# 此代码行明白易懂：如果user 的值未包含在列表banned_users 中，Python将返回True ，进而执行缩进的代码行。
if user not in banned_users:
    # 用户'marie'未包含在列表banned_users中，因此她将看到一条邀请她发表评论的消息：
    print(user.title() + ", you can post a_input response if you wish.")

