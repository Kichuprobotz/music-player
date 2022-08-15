import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "15691417"))
API_HASH = getenv("API_HASH", "862bf146beea9e01f18ee347a8e075fb")
BOT_TOKEN = getenv("BOT_TOKEN", "5536387973:AAEF4qXInJ1Wu9Vx_T2uKZUC_VvINPSKaTY")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "1BVtsOIcBu1pgYtRARymnDYwycLUf1n5y4uMFcAwADZjDe9ettnXqxd5X2Gm1MoVY4_tSGOzI5LDjDGc0812id2UqNIJFFphIRjXHZqCUJ9f0KN2RHpSavzsGdQ8VWA4T1kcm0HmS4wzvejeQTWhxjCBCgYdTK_criEc58F_tCBfk9BTepxymPDVHZV7MhPKAXbwyZQ0V6Tg0187t36Njz-DYAI5dF2xXJ57bLPq4N71V_nb79_KpX9xNaFM_7VLvAL1f5cJuVLOD-yn3Kz85zfIIbkHywNkGQSzdZ8j2Q1q5_X6lnCUFJk6uXpjPrlKgKpCFRIv07NtwyBqmT77u5cT_RskR3eA=")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1282754256").split()))
