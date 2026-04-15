import Onboarding from './components/Onboarding';
import { useState } from 'react';

export const TestOnboarding = () => {
  const [show, setShow] = useState(true);
  
  if (!show) return <button onClick={() => setShow(true)} className="p-10">Restart Onboarding</button>;
  
  return <Onboarding onComplete={() => setShow(false)} />;
};
