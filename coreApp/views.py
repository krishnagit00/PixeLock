
from django.shortcuts import render

def history_view(request):
    # In a real "no-logs" scenario, history might be stored in the client's
    # browser localstorage and rendered via JS.
    # If server-side session history is required:
    transfer_history = request.session.get('transfer_history', [])
    
    context = {
        'transfer_history': transfer_history
    }
    # Using the template shown in Image 1 & 5
    return render(request, 'history.html', context)
