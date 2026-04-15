import Timeline from './components/Timeline';

export const TestTimeline = () => {
  const dummyEvents = [
    { id: 1, fileName: "receipt.pdf", type: 'pdf' as const, oldPath: "/Downloads", newPath: "/Finance/Receipts", timestamp: "12:45 PM" },
    { id: 2, fileName: "vacation.png", type: 'image' as const, oldPath: "/Desktop", newPath: "/Images/Personal", timestamp: "1:15 PM" },
    { id: 3, fileName: "app.ts", type: 'code' as const, oldPath: "/Downloads", newPath: "/Dev/Projects", timestamp: "2:30 PM" },
    { id: 4, fileName: "summary.docx", type: 'other' as const, oldPath: "/Downloads", newPath: "/Work/Docs", timestamp: "3:00 PM" },
  ];

  return (
    <div className="p-10 bg-gray-50 min-h-screen">
      <h2 className="text-2xl font-black mb-8 text-dark tracking-tight">Today's Journey</h2>
      <Timeline events={dummyEvents} />
    </div>
  );
};
