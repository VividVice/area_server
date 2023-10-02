from modules.config.config import Config
from modules.login.login import Login, Register
from modules.database.DB import DataBaseOpps as DB

if __name__ == '__main__':
    config = Config()
    DB.CreateDb()
    config.AddResource(Login, '/login')
    config.AddResource(Register, '/register')
    config.Run()
