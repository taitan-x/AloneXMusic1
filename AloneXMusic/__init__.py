from aiohttp import ClientSession
from .console import LOGGER

from AloneXMusic.modules.core.app import App
from AloneXMusic.modules.core.bot import Bot
from AloneXMusic.modules.core.dirs import dirr
from AloneXMusic.modules.core.git import git
from AloneXMusic.misc import dbb, heroku, sudo

dirr()

git()

dbb()

heroku()

sudo()

# Clients
app = App()

bot = Bot()


from AloneXMusic.utilities.media import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

aiohttpsession = ClientSession()
