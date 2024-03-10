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
            placeBrick(this.id.substring(4));
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
        document.querySelector('#instructions').style.display = "true";
        document.querySelector('#instructions').textContent = `${data.player.toUpperCase()}'s turn`
        currentPlayer = data.player;
        gameOver = false;
    })
}

function placeBrick(index) {
    url = document.body.getAttribute('place-url')
    if (gameOver == false) {
        fetch(url, {
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
        })
        .then(data => {
            document.getElementById('error-message').style.display='none';
            document.querySelector(`#cell${index}`).textContent = currentPlayer.toUpperCase();
            gameOver = data.game_over;
            if (gameOver) {
                document.getElementById('win-message').textContent = `Congratulations! ${currentPlayer} won!`;
                document.getElementById('win-message').style.display = 'block';
                document.getElementById('instructions').style.display = 'none';
            }
            currentPlayer = data.player;
            document.getElementById('instructions').textContent = `${currentPlayer.toUpperCase()}'s turn.`;
        })
        .catch(error => {
            const errorMessage = document.getElementById('error-message');
            errorMessage.textContent = error.error;
            errorMessage.style.display = 'block';
        });
    }
}

