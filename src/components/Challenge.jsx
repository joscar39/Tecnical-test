import React from 'react';
import Paper from 'material-ui/Paper';
import RenderTable from './RenderTable.jsx';
import AnswerTable from './AnswerTable.jsx';

const paperStyle = {
  padding: 20,
  height: 1100,
  margin: 20,
  alignItems: 'center',
  textAlign: 'center',
  backgroundColor: '#ced7e5',
};

const Challenge = () => (
  <section id="challenge">
    <Paper className={"challenge"} style={paperStyle} zDepth={3}>

      <div>
        <h1>Desafío de matrices</h1>

        <h3>A continuación hay un número de filas con números enteros</h3>

        <p> Su trabajo es usar Selenium o Cypress para leer el dom y crear una estructura de datos de matriz para cada una de las filas.</p>
        <p>
        Una vez que tenga cada matriz, escriba una función que pueda devolver el índice de la matriz<br></br> donde la suma de los enteros en el índice de la izquierda es igual a la suma de los enteros en la derecha.</p>
        
        <p>Si no hay índice devuelve null</p>
          
        <p>
        Por ejemplo dada la matriz <code>[10, 15, 5, 7, 1, 24, 36, 2] </code><br></br>
        índice 5 (con el valor de 24) sería el centro, para 10 + 15 + 5 + 7 + 1 = 38 y 36 + 2 = 38
        </p>

        <RenderTable />
        <AnswerTable />
      </div>
    </Paper>
  </section>
);

export default Challenge;