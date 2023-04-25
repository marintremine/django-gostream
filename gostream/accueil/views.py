from django.shortcuts import render
import twitch

from equipe.models import Streamer

# Create your views here.
def accueil(request):
    streamers = Streamer.objects.all()
    
    liste_chaine_twitch = ['gostreamfr']
    for streamer in streamers.values():
        liste_chaine_twitch.append(streamer['twitch'][22:])
    live = [{'nom': streamer['name'], 'twitch':streamer['twitch'], 'online':False, 'pp':streamer['pp'],'streamer':streamer} for streamer in streamers.values()]

    client = twitch.TwitchHelix(client_id='04f1as1dvnnv3hohrbzeaumxt2xy88', client_secret='v60u7ayx6bvfawy9r3mzmq5hv67dn3', scopes=[twitch.constants.OAUTH_SCOPE_ANALYTICS_READ_EXTENSIONS])
    client.get_oauth()
    stream = client.get_streams(user_logins=liste_chaine_twitch)
    stream = list(stream).copy()
    rendu = {'title':"C'est désert pour le moment...",'game_name':'Check le planning !','viewer_count':'∞'}
    for streamer in live:
        for chaine in stream:
            if chaine['user_name'].lower() == streamer['twitch'][22:].lower():
                streamer['online'] = True
    for chaine in stream:
        if chaine['user_name'].lower() == 'gostreamfr':
            rendu = chaine
    rendu['streamers'] = live
    return render(request, 'accueil/index.html', context=rendu)