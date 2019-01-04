import React, { Component } from "react";
import axios from "axios";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      response: {}
    };
  }

  componentDidMount() {
    axios.get("/api/v1.0/sample").then(resp => {
      console.log(resp.data);
      this.setState({ response: resp.data });
    });
  }

  render() {
    return (
      <div>
        <h3>API Response</h3>
        <pre>{JSON.stringify(this.state.response, null, 2)}</pre>
      </div>
    );
  }
}

export default App;
