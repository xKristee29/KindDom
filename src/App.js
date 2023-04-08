import logo from './logo.svg';
import './App.css';
import ActualPage from './Comps/ActualPage';
import NavBar from './Comps/NavBar';
import {useState} from 'react'
import "./Comps/style.css"

function App() {

  const [contor, setContor] = useState(0);

 

  return (
    <div className="App">
      
      <NavBar setContor = {setContor} contor = {contor} />
      <ActualPage contor = {contor} setContor={setContor}/>

    </div>
  );
}

export default App;
