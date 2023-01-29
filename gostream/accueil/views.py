from django.shortcuts import render
import twitch
# Create your views here.
def accueil(request):
    client = twitch.TwitchHelix(client_id='04f1as1dvnnv3hohrbzeaumxt2xy88', client_secret='v60u7ayx6bvfawy9r3mzmq5hv67dn3', scopes=[twitch.constants.OAUTH_SCOPE_ANALYTICS_READ_EXTENSIONS])
    client.get_oauth()
    stream = client.get_streams(user_logins=['otplol_'])
    return render(request, 'accueil/index.html', context=stream[0])