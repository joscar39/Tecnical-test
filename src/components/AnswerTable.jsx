import React, {Component} from 'react';
import Paper from 'material-ui/Paper';
import TextField from 'material-ui/TextField';
import RaisedButton from 'material-ui/RaisedButton';
import Divider from 'material-ui/Divider';
import DialogBox from './DialogBox';

const verifyEndpoint = 'https://eqe90bcod2.execute-api.eu-west-1.amazonaws.com/live/ECSD-QA-tech-test';

const paperStyle = {
  padding: 10,
  height: 500,
  flex: 1, 
  flexDirection: 'row',
  alignItems:'center',
  textAlign: 'center',
  backgroundColor: '#c0cfe5'
};

const answerStyle = {
  textAlign: 'center',
  alignItems:'center',
  justifyContent: 'center',
  display: 'inline-block',
}

const rowStyle ={
  textAlign: 'center',
  alignItems:'center',
  justifyContent: 'center',
  display: 'block',
  width: 250
}

export default class AnswerTable extends Component {
  constructor(props) {
    super()
    this.handleClose = this.handleClose.bind(this)
  }
  
  state = {
    "dialogBoxOpen": false,
    "complete": false
  }

  handleClose = () => {
    this.setState({dialogBoxOpen: false});
  };

 submitForm = () => {
  this.setState({dialogBoxOpen: true});

  fetch(verifyEndpoint, {
      mode: 'cors',
      body: JSON.stringify({                
        "answer-1": this.state["answer-1"],
        "answer-2": this.state["answer-2"],
        "answer-3": this.state["answer-3"],
        "challenger-name": this.state["challenger-name"]
    }), 
        headers: {
        'content-type': 'application/json'
      },
      method: 'POST', 
    })
    .then(response => response.text())
    .then(text => {
      if (text.includes('success')) {
        this.setState({complete: true});
      }
    })
    .catch(err => console.error)
  }

  handleText = (event, value, formId) => {
    this.setState({
      [formId]: event.target.value,
    });
  };

  render() {
    return (
      <div>
        <Paper style={paperStyle} zDepth={2}>
          <h2>Envía tus respuestas</h2>
          <Paper style={answerStyle}>
            <TextField data-test-id={"submit-1"} hintStyle={rowStyle} hintText="enviar reto 1" underlineShow={false} onChange={(event, value) => this.handleText(event, value, 'answer-1')}/>
            <Divider />
            <TextField data-test-id={"submit-2"} hintStyle={rowStyle} hintText="enviar reto 2" underlineShow={false} onChange={(event, value) => this.handleText(event, value, 'answer-2')}/>
            <Divider />
            <TextField data-test-id={"submit-3"} hintStyle={rowStyle} hintText="enviar reto 3" underlineShow={false} onChange={(event, value) => this.handleText(event, value, 'answer-3')}/>
            <Divider />            
            <TextField data-test-id={"submit-4"} hintStyle={rowStyle} hintText="Tu nombre" underlineShow={false} onChange={(event, value) => this.handleText(event, value, 'challenger-name')}/>
          </Paper>
          <p>En el envío, verificaremos si sus respuestas son correctas.</p>
          <p>¡Buena suerte!</p>
          <RaisedButton label="Enviar respuestas" primary={true} onClick={this.submitForm}/>
         <DialogBox data-test-id={"render-challenge"} className={"submit-button"}  open={this.state.dialogBoxOpen} complete={this.state.complete} handleClose={this.handleClose} />
        </Paper>
      </div>
    );
  }
}
