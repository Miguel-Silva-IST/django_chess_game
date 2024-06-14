from django.shortcuts import render, redirect
from django.urls import reverse
from urllib.parse import urlencode
from django.http import JsonResponse
from chess.chess_game_logic import main
from .models import BoardState
import json

#def start_game(request):
#    #deletes any saved game state
#    BoardState.objects.all().delete()
#    initial_board = main.start().board
#    BoardState.objects.create(state=str(initial_board))
#    return redirect(reverse('game-view'))


def start_game(request):
    #deletes any saved game state
    BoardState.objects.all().delete()
    initial_board = {"board" : main.start().board}
    initial_board_json = json.dumps(initial_board) 
    board = BoardState(state=initial_board_json)
    board.save()
    return redirect(reverse('game-view'))



def game_view(request):
    context = {
    'board' : BoardState.objects.all()
    }
    return render(request, 'chess/game_view.html', context)

def move_piece(request):
    if request.method == 'POST':
        move = request.POST.get('move')
        game = request.session['game']
        success, board_fen = game.move(move)
        request.session['board_fen'] = board_fen
        if success:
            return JsonResponse({'status': 'success', 'board_fen': board_fen})
        else:
            return JsonResponse({'status': 'invalid move'})
    return JsonResponse({'status': 'fail'})
