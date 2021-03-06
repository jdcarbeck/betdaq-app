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
            <Balence />
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

class Balence extends React.Component {
  constructor(props){
    super(props);
    this.state = Data
  }

  componentDidMount() {
    this.balenceId = setInterval(
      () => this.tick(),
      1000
    )
  }

  componentWillUnmount(){
    clearInterval(this.balenceId)
  }

  tick() {
    this.setState(Data);
  }
  
  render() {
    return(
     <h4>£{this.state.Account_Balence}</h4>
    )
  }
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
    this.state = Data.Strat_Active;

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
     this.state = Data.Active_Orders
  }
  
  render(){
     return(
         <Child data={this.state}/>
     );
  }
}

class Child extends React.Component{
  
  render(){
     return(
        <div className = "List">
          {
             this.props.data.map(el=>
                 <p>{el}</p>
             )
          }
        </div>
     )
  }
}


export default App;
