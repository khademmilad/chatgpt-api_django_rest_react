import React, { useEffect, useState } from 'react';

function ProfilePage() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    fetchPosts();
  }, []);

  const fetchPosts = async () => {
    try {
      const userId = 1;
      const response = await fetch(`http://127.0.0.1:8000/api/posts/user/1/`);
      const responseData = await response.text();
      console.log(responseData); // Log the response for inspection
      const data = JSON.parse(responseData);
      setPosts(data);
      console.log('salam', data)
    } catch (error) {
      // console.error('Error fetching posts:', error);
    }
  };

  return (
    <div>
      <h1>Profile Page</h1>
      <ul>
        {posts.map((post) => (
          <li key={post.id}>{post.title}</li>
        ))}
      </ul>
    </div>
  );
}

export default ProfilePage;
