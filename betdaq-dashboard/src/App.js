import React, { Component } from 'react';
import Button from 'react-bootstrap/Button'

import './App.css';

class App extends Component {
  render() {
    return (
      <div>
        <h1>Betdaq Stragegy</h1>
        <Clock />
        <Balence balence="£196.36" />
        <div >
          <h3>Stragey 1</h3>
          <Toggle/>
        </div>
        <h2>Active Orders</h2>
        <List/>
      </div>
    );
  }
}

function Balence (props) {
  return <h2>{props.balence}</h2>
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
        <h2>{this.state.date.toLocaleTimeString()}</h2>
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
