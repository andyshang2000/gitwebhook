from flask import render_template
from hook import hook

import os


@hook.route('/')
def index():
    return render_template('hook/index.html')


@hook.route('/<user>/<repo>')
def githook(user, repo):
    path = '%(user)s/%(repo)s' % {'user': user, 'repo': repo}
    if not os.path.exists(path):
        os.system("git clone https://github.com/%(path)s.git git/%(path)s" % {'path': path})
    else:
        os.system("cd git/%(path)s && git pull" % {'path': path})
    return "ok"
