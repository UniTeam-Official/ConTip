import React, { Component } from "react";

class Movie extends Component {
  render() {
    return (
          <article class="style1">
            <span class="image">
              <img src="images/pic01.jpg" alt="" />
            </span>
            <a href="film_page.html">
              <h2>*Movie Title*</h2>
              <div class="content">
                <p>*Genre*<br />*Year*</p>
              </div>
            </a>
          </article>
    );
  }
}

export default Movie;