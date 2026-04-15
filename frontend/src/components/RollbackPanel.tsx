import React, { useState } from 'react';
import { RotateCcw, Filter, Calendar, Trash2 } from 'lucide-react';
import ActivityLog from './ActivityLog';

interface Activity {
  id: number;
  fileName: string;
  action: 'move' | 'rename' | 'copy';
  src: string;
  dest: string;
  timestamp: string;
}

const RollbackPanel: React.FC = () => {
  const [activities, setActivities] = useState<Activity[]>([
    { id: 1, fileName: "test1.pdf", action: 'move', src: "/Downloads", dest: "/Docs", timestamp: "1 hour ago" },
    { id: 2, fileName: "test2.jpg", action: 'move', src: "/Downloads", dest: "/Images", timestamp: "2 hours ago" },
    { id: 3, fileName: "test3.zip", action: 'move', src: "/Downloads", dest: "/Archives", timestamp: "1 day ago" },
  ]);

  const handleUndo = (id: number) => {
    // Simulated undo
    setActivities(prev => prev.filter(a => a.id !== id));
  };

  const handleBulkUndo = () => {
    // Simulated bulk undo
    setActivities([]);
  };

  return (
    <div className="bg-white p-6 rounded-2xl shadow-lg border border-gray-100 max-w-2xl mx-auto">
      <div className="flex items-center justify-between mb-8">
        <div>
          <h2 className="text-2xl font-black text-dark tracking-tight">Rollback History</h2>
          <p className="text-gray-400 text-sm">Reverse any organization action from the last 30 days.</p>
        </div>
        <button 
          onClick={handleBulkUndo}
          disabled={activities.length === 0}
          className="flex items-center gap-2 px-4 py-2 bg-red-50 text-red-500 rounded-lg font-bold hover:bg-red-500 hover:text-white transition-all disabled:opacity-30 disabled:hover:bg-red-50 disabled:hover:text-red-500"
        >
          <Trash2 size={18} />
          Rollback All
        </button>
      </div>

      <div className="flex gap-4 mb-6">
        <div className="flex-1 relative">
          <Filter className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" size={16} />
          <input 
            placeholder="Search by filename or path..." 
            className="w-full pl-10 pr-4 py-2 bg-gray-50 border-none rounded-xl text-sm focus:ring-2 focus:ring-primary/20 transition-all"
          />
        </div>
        <button className="p-2 bg-gray-50 text-gray-500 rounded-xl hover:bg-gray-100 transition-all">
          <Calendar size={18} />
        </button>
      </div>

      <ActivityLog activities={activities} onUndo={handleUndo} />
    </div>
  );
};

export default RollbackPanel;
