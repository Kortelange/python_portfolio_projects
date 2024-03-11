let currentPlayer;
let gameOver;

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.player-choice').forEach(function(button) {
        button.addEventListener('click', function() {
            chooseStartingPlayer(this.textContent);
        });
    });
    document.querySelectorAll('.cell').forEach(function(div){
        div.addEventListener('click', function(){
            if (this.getAttribute('slot-occupied') === 'true'){
                moveBrick(this.id.substring(4));
            } else {
                placeBrick(this.id.substring(4));
            }
        });
    });
});


function chooseStartingPlayer(player) {
    url = document.body.getAttribute('start-player-url');
    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ player: player})
    })
    .then(response => response.json())
    .then(data => {
        document.querySelector('#choose-start-player').style.display = 'none';
        document.querySelector('#instructions').style.display = 'block';
        document.querySelector('#instructions').textContent = `${data.player.toUpperCase()}'s turn`;
        document.querySelector('#reset-game').style.display = 'block';
        currentPlayer = data.player;
        gameOver = false;
    })
}

function postRequest(url, index) {
    return fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ index: index, player: currentPlayer })
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(err => {throw err; });
        }
        return response.json();
    });
}

function handleError(error) {
    const errorMessage = document.getElementById('error-message');
    errorMessage.textContent = error.error;
    errorMessage.style.display = 'block';
}

function placeBrick(index) {
    url = document.body.getAttribute('place-url')
    if (gameOver == false) {
        postRequest(url, index)
        .then(data => {
            document.getElementById('error-message').style.display='none';
            const divElement = document.querySelector(`#cell${index}`);
            divElement.textContent = currentPlayer.toUpperCase();
            divElement.setAttribute('slot-occupied', 'true');
            gameOver = data.game_over;
            if (gameOver) {
                document.getElementById('win-message').textContent = `Congratulations! ${currentPlayer} won!`;
                document.getElementById('win-message').style.display = 'block';
                document.getElementById('instructions').style.display = 'none';
            }
            currentPlayer = data.player;
            document.getElementById('instructions').textContent = `${currentPlayer.toUpperCase()}'s turn.`;
        })
        .catch(error => handleError(error));
    }
}

function moveBrick(index) {
    url = document.body.getAttribute('move-url')
    if (!gameOver) {
        postRequest(url, index)
        .then(data => {
            document.getElementById('error-message').style.display='none';
            const divElement = document.querySelector(`#cell${index}`);
            divElement.textContent = "";
            divElement.setAttribute('slot-occupied', 'false');
            document.getElementById('instructions').textContent = `${currentPlayer.toUpperCase()}'s to place.`;
        })
        .catch(error => handleError(error));
    }
}