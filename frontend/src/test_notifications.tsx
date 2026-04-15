import { NotificationProvider, useNotify } from './components/NotificationProvider';

const TestButton = () => {
  const notify = useNotify();
  return (
    <div className="space-x-4">
      <button onClick={() => notify("Success!", "success")} className="bg-success p-2 text-white">Success</button>
      <button onClick={() => notify("Something failed.", "error")} className="bg-red-500 p-2 text-white">Error</button>
    </div>
  );
};

export const TestNotifications = () => {
  return (
    <NotificationProvider>
      <div className="p-10 bg-gray-50 min-h-screen flex items-center justify-center">
        <TestButton />
      </div>
    </NotificationProvider>
  );
};
