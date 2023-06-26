const Profile: React.FC = () => {
  const user = {
    name: 'John Doe',
    email: 'johndoe@example.com',
    bio: 'I am a web developer.',
  };

  return (
    <div>
      <h1>Profile</h1>
      <p>Name: {user.name}</p>
      <p>Email: {user.email}</p>
      <p>Bio: {user.bio}</p>
    </div>
  );
};

export default Profile;