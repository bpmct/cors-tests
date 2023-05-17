import React, { useEffect, useState } from "react";
import logo from "./logo.svg";
import "./App.css";

function App() {
  const [data, setData] = useState({});
  const [error, setError] = useState({});

  useEffect(() => {
    fetchAndHandleData("/get/no-cors", "noCors");
    fetchAndHandleData("/get-and-options/no-cors", "noCorsWithOptions");
    fetchAndHandleData(
      "/get-and-options/no-cors-with-credentials",
      "noCorsWithOptionsCredentials"
    );
    fetchAndHandleData("/get-and-options/with-cors", "withCors");
    fetchAndHandleData(
      "/get-and-options-and-credentials/with-cors",
      "withCorsAndCredentials"
    );
  }, []);

  const fetchAndHandleData = async (path, key) => {
    try {
      const response = await fetch(
        `https://5000-bpmct-corstests-paqeobhjskm.ws-us97.gitpod.io${path}`,
        {
          method: "GET",
          credentials:
            key === "withCorsAndCredentials" ||
            key === "noCorsWithOptionsCredentials"
              ? "include"
              : "omit",
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
      const data = await response.json();
      setData((prevData) => ({ ...prevData, [key]: data }));
    } catch (error) {
      setError((prevError) => ({ ...prevError, [key]: error.message }));
      console.error(error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        {Object.entries(data).map(([key, value]) => (
          <div key={key}>
            <h2>Data from {key}:</h2>
            <pre>{JSON.stringify(value, null, 2)}</pre>
          </div>
        ))}
        {Object.entries(error).map(([key, value]) => (
          <div key={key}>
            <h2>Error from {key}:</h2>
            <pre>{value}</pre>
          </div>
        ))}
      </header>
    </div>
  );
}

export default App;
