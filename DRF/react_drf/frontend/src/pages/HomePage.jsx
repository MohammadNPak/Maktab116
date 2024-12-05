import React from 'react';
import { Link } from 'react-router-dom';

const HomePage = () => {
  const posts = [
    { id: 1, title: "Post 1", summary: "Summary of post 1" },
    { id: 2, title: "Post 2", summary: "Summary of post 2" },
  ];

  return (
    <div>
      <h1>Blog</h1>
      <ul>
        {posts.map(post => (
          <li key={post.id}>
            <h2>{post.title}</h2>
            <p>{post.summary}</p>
            <Link to={`/post/${post.id}`}>Read More</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default HomePage;
