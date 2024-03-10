document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.player-choice').forEach(function(button) {
        button.addEventListener('click', function() {
            chooseStartingPlayer(this.textContent);
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
    })
}

