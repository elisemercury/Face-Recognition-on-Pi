from webexteamssdk import WebexTeamsAPI

def alert_teams():

    teams_token = "NTdkMTJlMjUtZjg1ZC00ZWZmLWEwNGYtZjgyNjRmYzk3YzUyMzI5M2Y1ZDQtYzMx_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"

    api = WebexTeamsAPI(access_token = teams_token)

    message = api.messages.create(toPersonEmail="elisejlandman@hotmail.com",
               text=None, markdown=("**⚠️ Alert:** " + x + " detected an unknown visitor at " + ti_string + " " + dt_string + ". " + "Click [here](https://1drv.ms/u/s!Avfnv99SkyA5gbJSm4YXTxfVjn9eYg?e=JlUhXY) to view the log file." ), files=["alert.png"], attachments=None
