import ActivityLog from './components/ActivityLog';

export const TestActivityLog = () => {
  const dummyActivities = [
    {
      id: 1,
      fileName: "report_v1.pdf",
      action: 'move' as const,
      src: "/Downloads",
      dest: "/Documents/Work",
      timestamp: "2 mins ago"
    },
    {
      id: 2,
      fileName: "screenshot.png",
      action: 'move' as const,
      src: "/Desktop",
      dest: "/Images/Screenshots",
      timestamp: "5 mins ago"
    }
  ];

  return (
    <div className="p-10 bg-gray-100 min-h-screen">
      <div className="max-w-xl mx-auto">
        <ActivityLog activities={dummyActivities} onUndo={(id) => console.log("Undo", id)} />
      </div>
    </div>
  );
};
