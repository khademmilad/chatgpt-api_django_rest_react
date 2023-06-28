import React from 'react';

interface ProfileProps {
  name: string;
  age: number;
}

const Profile: React.FC<ProfileProps> = ({ name, age }) => {
  return (
    <div>
      <h1>{name}</h1>
      <p>Age: {age}</p>
    </div>
  );
};

export default Profile;
