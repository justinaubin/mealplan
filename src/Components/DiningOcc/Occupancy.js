import React, { Component } from 'react'
import TopBar from '../layout/TopBar'
import LineGraph from '../Graphs/LineGraph'
// import dhall from '../../Pictures/dhall.jpg'

export class Occupancy extends Component {
    constructor(props) {
        super(props);
        this.state = {lineData: []};
    }

    componentDidMount() {
        fetch('/diningdata').then(res => res.json()).then(data => {
            this.setState({lineData: data.data});
            console.log(data)
        });
    //     // fetch('/diningdata').then(res => res.json()).then(data => {
    //     //   this.setState({currentTime: data.sillAvg});
    //     //   console.log(data)
    //     // });
    }

    render() {
        const pageLinks = {
            name1: "Account",
            page1: '/account',
            name2: 'Home',
            page2: '/'
        };

        return (
            <div >
                <TopBar links={pageLinks}/>
                <LineGraph data={this.state.lineData}/>
            </div>
        )
    }
}

// let image = {
//     backgroundImage: `url(${dhall})`,
//     backgroundPosition: 'center',
//     backgroundSize: 'cover',
//     height: '100vw',
//     width: '100vw'
//   }

// let style2 = {
//     height: '150px',
//     width: '150px'
// }


export default Occupancy
