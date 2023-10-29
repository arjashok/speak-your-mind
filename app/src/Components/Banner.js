import React from 'react';
import './Banner.css';
import logo from "../logo.png"

function Banner(){
    return(
        <div className="banner">
            <img src={logo} alt="Banner" className="banner-image"/>
        </div>
    );
}

export default Banner;