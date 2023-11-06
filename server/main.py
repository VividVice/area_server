from modules.config.config import Config
from modules.config.info import AboutResource
from modules.database.DBsetup import CreateDb
from modules.endpoints.login import Login, Register, RefreshToken, UserInfo
from modules.endpoints.gitgub.github_Oauth import GitHubOauthAuthorization, GitHubOauthAccess
from modules.endpoints.serviceSubscription import Subscripe, Unsubscripe
from modules.endpoints.trello_endpoints.Trello_commands_1 import Trello_Access
from modules.endpoints.gitgub.github_endpoints import Github_Access
from modules.APIs.trello.TrelloWebhook import WebHookTrello, get_endpoint as trello_endpoint
from modules.endpoints.reaction_sub import Area_Sub
from modules.APIs.callr import Callr_Webhook
import apk_build
import get_areas
from modules.APIs.callr.Callr_Webhook import  WebHookCallr, get_endpoint as callr_endpoint
# from apscheduler.schedulers.background import BackgroundScheduler
# from trello import Trello, ChatGPT

if __name__ == '__main__':
    config = Config()
    CreateDb()
    config.AddResource(Login, '/login')
    config.AddResource(Register, '/register')
    config.AddResource(GitHubOauthAuthorization, '/OuthGithub/authorize')
    config.AddResource(GitHubOauthAccess, '/OauthGithub/access')
    config.AddResource(AboutResource, '/about.json')
    config.AddResource(Subscripe, '/subscribe')
    config.AddResource(Unsubscripe, '/unsubscribe')
    config.AddResource(RefreshToken, '/refresh')
    config.AddResource(UserInfo, '/me')
    config.AddResource(Trello_Access, '/trello/')
    config.AddResource(Github_Access, '/github/')
    config.AddResource(Area_Sub, '/create_AREA')
    config.AddResource(WebHookTrello, f'/{trello_endpoint()}/')
    config.AddResource(WebHookCallr, f'/{callr_endpoint()}/')
    config.Run()
