from webexteamssdk import WebexTeamsAPI

def alert_teams(hostname, dt_string, ti_string):

    teams_token = "TEAMS-TOKEN"

    api = WebexTeamsAPI(access_token = teams_token)

    message = api.messages.create(toPersonEmail="EMAIL",
               text=None, markdown=("**⚠️ Alert:** " + hostname + " detected an unknown visitor at " + ti_string + " " + dt_string + ". "), files=["alert.png"], attachments=None)
