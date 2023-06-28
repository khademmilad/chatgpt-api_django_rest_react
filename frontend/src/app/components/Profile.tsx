import React from 'react';



type Props = {
    name: string;
    age: number;}

const Profile = (props: Props) => {
    const {age,name} = props
  return (
    <div className='flex flex-row mx-auto w-full text-3xl text-center items-center'>My name is {name}</div>
  )
}

export default Profile