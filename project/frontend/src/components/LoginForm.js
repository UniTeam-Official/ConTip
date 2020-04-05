import React, { Component } from "react";
import PasswordInputField from "./PasswordInputFields";
import TextInputField from "./TextInputField";

class LoginForm extends Component {
  render() {
    return (
        <TextInputField />
        <PasswordInputField />
    );
  }
}

export default LoginForm;
