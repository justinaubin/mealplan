import React, { Component } from 'react'
import TopBar from '../layout/TopBar'
import dhall from '../../Pictures/Saybrook_Dhall.jpg'

export class Home extends Component {
    render() {
        const pageLinks = {
            name1: "Account",
            page1: '/account',
            name2: 'Dining Hall Occupancy',
            page2: '/occupancy'
        };
        return (
            <div style={image}>
                <TopBar links={pageLinks}/>
            </div>
        )
    }
}

let image = {
  backgroundImage: `url(${dhall})`,
  backgroundPosition: 'center',
  backgroundSize: 'cover',
  height: '100vw',
  width: '100vw'
}

export default Home
