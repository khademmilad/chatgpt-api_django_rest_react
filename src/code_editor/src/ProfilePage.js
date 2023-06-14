import React, { useEffect, useState } from 'react';
import Navbar from './Navbar';

function ProfilePage() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    fetchPosts();
  }, []);

  const fetchPosts = async () => {
    try {
      const userId = 1;
      const response = await fetch(`http://127.0.0.1:8000/api/posts/user/1/`);
      const responseData = await response.json();
      setPosts(responseData);
    } catch (error) {
      console.error('Error fetching posts:', error);
    }
  };

  return (
    <div className="container">
      <Navbar />

      <div className="profile-content">
        <h1>Profile Page</h1>
        <ul>
          {posts.map((post) => (
            <li key={post.id}>{post.title}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default ProfilePage;
