import React, { Component } from "react";
import { render } from "react-dom";
import Header from "./Header";
import Main from "./Main";
import Footer from "./Footer";

class App extends Component {
//  constructor(props) {
//    super(props);
//    this.state = {
//      data: [],
//      loaded: false,
//      placeholder: "Loading"
//    };
//  }

//  componentDidMount() {
//    fetch("api/v1/app/film/list/")
//      .then(response => {
//        if (response.status > 400) {
//          return this.setState(() => {
//            return { placeholder: "Something went wrong!" };
//          });
//        }
//        return response.json();
//      })
//      .then(data => {
//        this.setState(() => {
//          return {
//            data,
//            loaded: true
//          };
//        });
//      });
//  }

  render() {
    return (
      <Header />
      <Main />
      <Footer />
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);