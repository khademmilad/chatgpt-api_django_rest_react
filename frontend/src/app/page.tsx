import Image from 'next/image'
import Profile from './components/Profile';


export default function Home() {
  return (
    <div>
      <h1>Welcome to My Profile Page</h1>
      <Profile name="John Doe" age={25} />
    </div>
  )
}
