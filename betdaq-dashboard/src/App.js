import React, { Component } from 'react';
import Button from 'react-bootstrap/Button'
import Data from './Data/strat_data.json'

import './App.css';

class App extends Component {
  render() {
    return (
    <div class="w3-row-padding w3-padding-64 w3-container">
      <div class="w3-content">
            <Clock />
            <Balence balence="£196.36" />
            <div>
              <h3>Strategy 1</h3>
              <Toggle/>
            </div>
            <center>
              <h2>Active Orders</h2>
              <List/>
            </center>
        </div>
      </div>

    );
  }
}

function Balence (props) {
  return <h4>Account Balance: {props.balence}</h4>
}


class Clock extends React.Component {
  constructor(props) {
    super(props);
    this.state = {date: new Date()};
  }

  componentDidMount() {
    this.timerID = setInterval(
      () => this.tick(),
      1000
    );
  }

  componentWillUnmount() {
    clearInterval(this.timerID);
  }

  tick() {
    this.setState({
      date: new Date()
    });
  }

  render() {
    return (
      <div>
        <h4>{this.state.date.toLocaleTimeString()}</h4>
      </div>
    );
  }
}

class Toggle extends React.Component {
  constructor(props) {
    super(props);
    this.state = {isToggleOn: true};

    // This binding is necessary to make `this` work in the callback
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    this.setState(prevState => ({
      isToggleOn: !prevState.isToggleOn
    }));
  }

  render() {
    return (
      <Button variant="primary" onClick={this.handleClick}>
        {this.state.isToggleOn ? 'ON' : 'OFF'}
      </Button>
    );
  }
}

class List extends React.Component{
  constructor(){
     super();
     this.state = {
       data: ["Horse Racing £20 12/1", "Greyhound Racing £10 7/2", 
              "Golf £30 10/3", "Horse Racing £15 7/2"]
     }
     this.delete = this.delete.bind(this);
  }
  
  delete(id){
     this.setState(prevState => ({
         data: prevState.data.filter(el => el !== id )
     }));
  }
  
  render(){
     return(
         <Child delete={this.delete} data={this.state.data}/>
     );
  }
}

class Child extends React.Component{

  delete(id){
      this.props.delete(id);
  }
  
  render(){
     return(
        <div className = "List">
          {
             this.props.data.map(el=>
                 <p onClick={this.delete.bind(this, el)}>{el}</p>
             )
          }
        </div>
     )
  }
}


export default App;
