from webexteamssdk import WebexTeamsAPI

def alert_teams(hostname, dt_string, ti_string):

    teams_token = "NTdkMTJlMjUtZjg1ZC00ZWZmLWEwNGYtZjgyNjRmYzk3YzUyMzI5M2Y1ZDQtYzMx_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"

    api = WebexTeamsAPI(access_token = teams_token)

    message = api.messages.create(toPersonEmail="elisejlandman@hotmail.com",
               text=None, markdown=("**⚠️ Alert:** " + hostname + " detected an unknown visitor at " + ti_string + " " + dt_string + ". "), files=["alert.png"], attachments=None)
