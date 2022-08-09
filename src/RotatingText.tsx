import './App.css';
import { useState, useEffect } from 'react';

const OPTIONS = ["talk politics", "play soccer", "eat ice cream", "write code"]
const START_IDX = Math.round(Math.random() * (OPTIONS.length - 1))

function RotatingText() {
  
  const [currentIdx, setCurrentIdx] = useState(START_IDX);
  const [isVisible, setIsVisible] = useState(true);

  useEffect(() => {
    setTimeout(() => {
      setIsVisible(false);
    }, 2000);
    
    setTimeout(() => {
      setCurrentIdx((currentIdx + 1) % OPTIONS.length);
      setIsVisible(true);
    }, 4000);    
  }, [currentIdx]);


  const className = "rotating-text" + (isVisible ? "" : " invisible")

  return (
   <p className={className}>{OPTIONS[currentIdx] + "."}</p>
  );
}

export default RotatingText;
