import logo from "./logo.svg";
import "./App.css";
import axios from "axios";
import { useState } from "react";
import Buttontest from "./currentplayingsongbutton";

function App() {
  const [data, setData] = useState(null);

  function getData() {
    axios({
      method: "GET",
      url: "/",
    })
      .then((response) => {
        const res = response.data;
        setData({
          profile_name: res.name,
          about_me: res.about,
          lyric: res.lyric, //this is a list of lines
        });
      })
      .catch((error) => {
        if (error.response) {
          console.log(error.response);
          console.log(error.response.status);
          console.log(error.response.headers);
        }
      });
  }

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <p>get your profile bs</p>
        <button onClick={getData}>click</button>
        {data && (
          <div>
            <p>Profile name: {data.profile_name}</p>
            <p>About me: {data.about_me}</p>
            {data.lyric && (
              <ul>
                {data.lyric.map((phrase, index) => (
                  <li key={index}>{phrase}</li>
                ))}
              </ul>
            )}
          </div>
        )}
      </header>
    </div>
  );
}

export default App;
