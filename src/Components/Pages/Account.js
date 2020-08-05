import React, { Component } from 'react'
import TopBar from '../layout/TopBar'

export class Account extends Component {
    render() {
        const pageLinks = {
            name1: "Home",
            page1: '/',
            name2: 'Dining Hall Occupancy',
            page2: '/occupancy'
        };
        return (
            <div>
                <TopBar links={pageLinks}/>
                <p>ACCOUNT</p>
            </div>
        )
    }
}

export default Account
