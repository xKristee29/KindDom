import './App.css';
import Section1 from './Section1';
import Section2 from './Section2';
import React, { useState } from 'react';

function App() {
  const [selectedOption, setSelectedOption] = useState('');

  const optionDescription = {
    1: <Section1 />,
    2: <Section2 />,
    3: "Option 3"
  }

  const handleClick = (option) => {
    setSelectedOption(option);
  };

  return (
    <div className="App">
      <div className="Options">
        <p onClick={() => handleClick(1)}>Option 1</p>
        <p onClick={() => handleClick(2)}>Option 2</p>
        <p onClick={() => handleClick(3)}>Option 3</p>
      </div>
      {selectedOption && (
        <div className="description">
          <h2>Option {selectedOption}</h2>
          <p>{optionDescription[selectedOption]}</p>
        </div>
      )}
    </div>
  );
}

export default App;
