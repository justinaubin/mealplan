import React, { Component } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom'
import Occupancy from './Components/DiningOcc/Occupancy'
import Home from './Components/HomeScreen/Home'
import Account from './Components/Pages/Account'
import Logout from './Components/Pages/Logout'

class App extends Component {
  render() {
    return (
      <BrowserRouter >
      <div className="App">
        <Switch>
          <Route exact path='/' component={Home} />
          <Route path='/occupancy' component={Occupancy} />
          <Route path='/account' component={Account} />
          <Route path='/logout' component={Logout} />
        </Switch>
      </div>
      </BrowserRouter>
    );
  }
}

// let image = {
//   backgroundImage: `url(${dhall})`,
//   backgroundPosition: 'center',
//   backgroundSize: 'cover',
//   height: '100vw',
//   width: '100vw'
// }

export default App;
