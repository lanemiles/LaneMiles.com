import './App.css';
import { useState, useEffect } from 'react';

const OPTIONS = ["talk politics", "play soccer", "eat ice cream", "write code"]

function RotatingText() {
  const randIdx = Math.round(Math.random() * (OPTIONS.length - 1))
  const [currentIdx, setCurrentIdx] = useState(randIdx);
  const [isVisible, setIsVisible] = useState(true);

  useEffect(() => {
    setTimeout(() => {
      setCurrentIdx((currentIdx + 1) % OPTIONS.length);
    }, 4000);
  }, [currentIdx]);

  useEffect(() => {
    setTimeout(() => {
      setIsVisible(!isVisible);
    }, 2000);
  }, [isVisible]);

  const className = "rotating-text" + (isVisible ? "" : " invisible")

  return (
   <p className={className}>{OPTIONS[currentIdx] + "."}</p>
  );
}

export default RotatingText;
