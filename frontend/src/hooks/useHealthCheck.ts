import { useState, useEffect } from 'react';
import { getHealth } from '../api/client';

export const useHealthCheck = () => {
  const [status, setStatus] = useState<string>('checking...');

  useEffect(() => {
    getHealth()
      .then((data) => setStatus(data.status))
      .catch(() => setStatus('disconnected'));
  }, []);

  return status;
};
