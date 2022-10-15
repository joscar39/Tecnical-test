
import RaisedButton from 'material-ui/RaisedButton';
import Paper from 'material-ui/Paper';
import Img from 'react-image';
import React from 'react';
import logo from '../logo.png';

const paperStyle = {
  padding: 20,
  height: 6000,
  margin: 20,
  alignItems: 'center',
  textAlign: 'center',
  backgroundColor: '#ced7e5',
};

const Logo = () => <Img src="" />;

const Introduction = props => (
  <section id="home">
    <Paper style={paperStyle} zDepth={3}>
      <Logo />
      <h1 className="title">Bienvenido a la prueba técnica de QA</h1>
      <p className="intro">
        Usando el lenguaje de programación de su elección, <br></br>queremos que cree un framework de Selenium o Cypress en .src/test/e2e.
           <br></br>Use Selenium o Cypress para hacer clic en el botón de abajo para continuar con la prueba.
      </p>
      <RaisedButton data-test-id={"render-challenge"}  label="Hacer el desafío" primary onClick={props.showChallenge} />
      <p>Es posible que haya notado que al hacer clic en este botón se inicia un desplazamiento muy, muy largo.<br></br>¿Me pregunto cómo vas a manejar eso?</p>
      <span style={{fontSize: 60}} role="img" aria-label="down-emoj" >⬇️</span>
    </Paper>
  </section>
);

export default Introduction;
