# import Flask Script object
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

import main
import models

# Init manager object via app object
manager = Manager(main.app)

# Init migrate object via app and db object
migrate = Migrate(main.app, models.db)

# Create some new commands
manager.add_command("server", Server(host='0.0.0.0', port=5000))
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()
