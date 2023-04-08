import {useState, useEffect} from 'react'
import AboutUs from './InsideComps/AboutUs';
import Homepage from './InsideComps/Homepage';
import Activities from './InsideComps/Activities';
import AccountPage from './InsideComps/AccountPage';
import Resources from './InsideComps/Resources';
import "./InsideComps/insidestyle.css"
import Tasks from './InsideComps/ActivityComps/Tasks';
const ActualPage = ({contor, setContor}) => {

    const components = [<Homepage  />, <AboutUs />, <Activities setContor={setContor}/>, <AccountPage/>, <Resources/>, <Tasks/>];

    return ( <div>

{components[contor]}

    </div>
     );
}
 
export default ActualPage