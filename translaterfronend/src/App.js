import "./App.css";
import axios from "axios";
import { useEffect, useState } from "react";
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

  useEffect(() => {
    // Function to be called at each interval

    // Set up the interval
    const intervalId = setInterval(getData, 800); // 1000ms = 1 second

    // Cleanup function to clear the interval
    return () => clearInterval(intervalId);
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <p>click button for current song</p>
        <button onClick={getData}>click</button>
        {data && (
          <div>
            <img style={{ width: 200, height: 280 }} src={data.song_img} />
            <p>song: {data.song_name}</p>
            <p>by: {data.author}</p>
            {data.lyric && (
              <ul style={{ listStyleType: "none" }}>
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
