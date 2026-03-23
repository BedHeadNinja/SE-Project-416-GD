/*convert from string to an Object 
      and use locolStorage to store the score
      console.log(JSON.parse(localStorage.getItem('score'))); */

      let score = JSON.parse(localStorage.getItem('score')) || { 
          wins: 0,
          loses: 0,
          ties: 0
        };

        updateScore();
        
      /*score === null == !score (same thing)
      if(score === null){
        score = { 
          wins: 0,
          loses: 0,
          ties: 0
        }
      }*/ 

      function playgame(playerMove){
        const computerMove = pickComputerMove();
        let result ='';

        if(playerMove === 'scissors'){
          if(computerMove === 'rock'){
            result = 'You Lose';
          }
          else if(computerMove === 'paper'){
            result = 'You Win';
          }
          else if(computerMove === 'scissors'){
            result = 'Tie';
          }
        } 
        else if(playerMove === 'paper'){
            if(computerMove === 'rock'){
            result = 'You Win';
          }
            else if(computerMove === 'paper'){
            result = 'Tie';
          }
            else if(computerMove === 'scissors'){
            result = 'You Lose';
          }
        }
        else{
          if(computerMove === 'rock'){
            result = 'Tie';
          }
            else if(computerMove === 'paper'){
            result = 'You Lose';
          }
            else if(computerMove === 'scissors'){
            result = 'You Win';
          }
        }

        if(result === 'You Win'){
          score.wins += 1;
        }
        else if(result === 'You Lose'){
          score.loses += 1;
        }
        else if(result === 'Tie'){
          score.ties += 1;
        }
        
        /*save score into localStorage
        and use JSON.stringify to convert from object to string*/
        localStorage.setItem('score', JSON.stringify(score));
        
        updateScore();
        
        document.querySelector('.js-result')
        .innerHTML = result;

        document.querySelector('.js-moves')
        .innerHTML = ` You ${playerMove}- Computer ${computerMove}`;
  
      }
      function updateScore(){
         document.querySelector('.js-score')
         .innerHTML = `Wins: ${score.wins}, Loses: ${score.loses}, Ties:${score.ties}`; 
      }

      function pickComputerMove(){
        const randomNumber = Math.random();
        let computerMove = '';
        if(randomNumber >= 0 && randomNumber < 1/3){
          computerMove = 'rock';
        }
        else if(randomNumber >= 1/3 && randomNumber < 2/3){
          computerMove = 'paper';
        }
        else{
          computerMove = 'scissors';
        }

        return computerMove;
      }