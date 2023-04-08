import './insidestyle.css';

const Activities = ({setContor}) => {
    return ( <div>

    <div className="panel1">
    
     <h1>Kindness Roulette</h1>
     <p>mortii tai</p>
     <button onClick={()=>{setContor(5)}}> Tasks </button>

    </div>

<div className='transition'>
.
</div>

    <div className="panel2">
     <h1>
        Text
     </h1>
     <p>AAAAAAAAAA</p>
     <button> Buton </button>

    </div>

    <div className='transition'>
.
    </div>

    <div className="panel3">

     <h1>
        Text
     </h1>

     <p>AAAAAAAAAA</p>
     <button>Buton</button>

    </div>

    </div> );
}
 
export default Activities;