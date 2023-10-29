import React, { useState } from 'react';
import axios from 'axios';

function PostForm(){
    const url= "http://localhost:5000/sym-processor"; //Get Url from Arjun and add it here
    const [data, setData] = useState({
        target: "",
        request_content: ""
    })

    const [response, setResponse] = useState(null);

    function submit(e){
        e.preventDefault();
        axios.post(url, {
            target: data.target,
            request_content: data.request_content
        }).then(res=>{
            console.log(res.data);
            setResponse(res.data);
        })
        .catch(err => {
            console.error("Error submitting data:", err);
            setResponse("Error occurred while submitting");
        });
    }

    function handle(e){
        const newdata={...data}
        newdata[e.target.id] = e.target.value
        setData(newdata)
        console.log(newdata)
    }

    const formStyle = {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        gap: '15px',
        margin: '50px auto',
        maxWidth: '750px',
        padding: '50px',
        boxShadow: '0 0 10px rgba(0, 0, 0, 0.1)',
        borderRadius:'8px',
        backgroundColor: 'white'
    }

    const inputStyle = {
        width: '50%',
        padding: '10px',
        boxSizing: 'border-box',
        borderRadius: '1px',
        border: '1px solid #ccc'
    };

    const hStyle = {
        margin: '2px'
    }

    return (
        <form onSubmit={(e)=> submit(e)} style={formStyle}>
            <h1 style = {hStyle}>Video Submission and Analysis Form</h1>
            <h2 style = {hStyle}>For Target Audience:</h2>
            <h3 style = {hStyle}>Audience: Type 0</h3>
            <h3 style = {hStyle}>Speaker: Type 1</h3>
            <h3 style = {hStyle}>Both: Type 2</h3>
            <input onChange={(e) => handle(e)} id="target" value={data.target} placeholder="Target Audience" type="number" style = {inputStyle}></input>
            <input onChange={(e) => handle(e)} id="request_content" value={data.request_content} placeholder="Video Url" type="text" style = {inputStyle}></input>
            <button>Submit</button>
        </form>
    );
}

export default PostForm;