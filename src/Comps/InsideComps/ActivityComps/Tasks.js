import { useState } from 'react';
import "./ministyle.css"; 

const provocari = [
  "Mulțumește cuiva pentru ajutorul lor",
  "Zâmbește cuiva pe stradă",
  "Ajută pe cineva cu o sarcină grea",
  "Întreabă pe cineva cum se simte astăzi",
  "Dăruiește hainele pe care nu le mai porți",
  "Adu un mic cadou surpriză pentru colegii de muncă",
  "Răspunde la un mesaj într-un mod amabil",
  "Împarte o poză sau un citat pozitiv pe rețelele de socializare",
  "Fă o donație mică unei organizații caritabile",
  "Ajută un vecin în vârstă cu cumpărăturile",
  "Ascultă cu atenție pe cineva când îți povestește ceva",
  "Oferă un îmbrățișare sau o mângâiere cuiva care are nevoie de încurajare",
  "Spune o glumă pentru a face pe cineva să zâmbească",
  "Oferă un pahar cu apă sau o gustare cuiva care pare obosit",
  "Mulțumește șoferului de autobuz pentru munca sa",
  "Cumpără o cafea sau un ceai pentru cineva care pare stresat",
  "Ajută un prieten sau un coleg să înțeleagă un concept dificil",
  "Adu o prăjitură sau o plăcintă la o petrecere sau eveniment social",
  "Dăruiește o carte bună cuiva care își dorește să citească mai mult",
  "Încurajează pe cineva să-și urmeze visurile și să nu renunțe"
];

const Tasks = () => {
  const [taskarrays, setTaskarrays] = useState([]);

  const SelectTasks = (nr) => {
    const newTasks = [];
    
    for(let i = 0; i < nr; i++){
        let j  = Math.floor(Math.random() * provocari.length) ;
      newTasks.push(provocari[j]);
    }
    setTaskarrays(newTasks);
  }

  const removeDiv = (index) => {
    const newArray = [...taskarrays];
    newArray.splice(index, 1);
    setTaskarrays(newArray);
  };

  return (
    <div>
      <div className="chenar-chenar">
        <div className="chenar">
          <div className="title">TITLU</div>
          <div className="topbar">
            <button class="topbar-button" onClick={() => SelectTasks(7)}>Creaza-mi o lista</button>
          </div>
          <div className="restul">
  {taskarrays !== undefined && taskarrays.length > 0 ? (
    taskarrays.map((task, index) => (
      <div className="tasks" key={index}>
        {task}
        <button className="removebutton" onClick={() => { removeDiv(index) }}>
          X
        </button>
      </div>
    ))
  ) : (
    <div className='tasks'>Ai Terminat!</div>
  )}
</div>
        </div>
      </div>
    </div>
  );
}
 
export default Tasks;
