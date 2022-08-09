import './App.css';
import emailIcon from './images/emailbig.png'
import workIcon from './images/workbig.png'
import schoolIcon from './images/universitybig.png'
import githubIcon from './images/githubbig.png'
import linkedInIcon from './images/linkedinbig.png'
import resumeIcon from './images/resumebig.png'
import RotatingText from './RotatingText'

function App() {
  return (
    <div className="outer-container">
      <div className='inner-container'>
        <div className="left-col">
          <div>
            <h1 className="hello">Hey there!</h1>
          </div>
          <div>
            <p className="my-name-is">My name is</p>
            <p className="lane-miles">Lane Miles</p>
            <p className="my-name-is">and I like to</p>
            <RotatingText />
          </div>
        </div>

        <div className="right-col">
          <div className="info-row">
            <img className="icon" src={schoolIcon} alt="School Icon"></img>
            <p className="about">Now: JD Candidate @ Stanford Law School</p>
          </div>
          <div className="info-row">
            <img className="icon" src={workIcon} alt="Work Icon"></img>
            <p className="about">Before: Senior Software Engineer @ Airbnb</p>
          </div>
          <div className="info-row">
            <img className="icon" src={emailIcon} alt="Email Icon"></img>
            <p className="about">Contact: lane.m.miles@gmail.com</p>
          </div>
          <div className="info-row">
            <img className="icon" src={resumeIcon} alt="Resume Icon"></img>
            <p className="about"><a href="/Lane Miles Resume.pdf" target="_blank" rel="noreferrer">Resume</a></p>
          </div>
          <div className="info-row">
            <img className="icon" src={linkedInIcon} alt="LinkedIn Icon"></img>
            <p className="about"><a href="http://www.linkedin.com/in/lanemiles" target="_blank" rel="noreferrer">LinkedIn</a></p>
          </div>
          <div className="info-row">
            <img className="icon" src={githubIcon} alt="GitHub Icon"></img>
            <p className="about"><a href="http://www.github.com/lanemiles" target="_blank" rel="noreferrer">GitHub</a></p>
          </div>
        </div>
        
      </div>
    </div>
  );
}

export default App;
