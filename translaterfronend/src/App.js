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
      url: "/profile",
    })
      .then((response) => {
        const res = response.data;
        setData({
          test: res.strin,
          song_name: res.songname,
          author: res.author,
          album_name: res.albumname,
          lyric: res.lyric, //this is a list of lines
          song_img: res.imgsrc,
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
        {/* <p>
          Edit <code>src/App.js</code> and save to reload.
        </p> */}
        {/* <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a> */}
        <p>click button for current song</p>
        <button onClick={getData}>click</button>
        {data && (
          <div>
            <img src={data.song_img} />
            <p>song: {data.song_name}</p>
            <p>by: {data.author}</p>
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
