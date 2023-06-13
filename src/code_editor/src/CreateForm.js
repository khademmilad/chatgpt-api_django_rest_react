import React, { useState } from 'react';
import axios from 'axios';

const PostForm = () => {
  const [title, setTitle] = useState('');
  const [text, setText] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    const data = {
      title: title,
      text: text,
    };

    axios.post('http://your-django-backend-url/posts/', data)
      .then((response) => {
        console.log(response.data); // handle success response
      })
      .catch((error) => {
        console.error(error); // handle error
      });

    // Reset form inputs
    setTitle('');
    setText('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="title">Title:</label>
        <input
          type="text"
          id="title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
      </div>
      <div>
        <label htmlFor="text">Text:</label>
        <textarea
          id="text"
          value={text}
          onChange={(e) => setText(e.target.value)}
        />
      </div>
      <button type="submit">Submit</button>
    </form>
  );
};

export default PostForm;
