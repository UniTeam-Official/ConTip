import React, { Component } from "react";

class TextInputField extends Component {
  render() {
    return (
      <input type="text" name="username" id="username" value="" placeholder="Your Username" />
    );
  }
}

export default TextInputField;