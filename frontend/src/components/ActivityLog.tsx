import React from 'react';
import { History, ArrowRight, RotateCcw } from 'lucide-react';

interface Activity {
  id: number;
  fileName: string;
  action: 'move' | 'rename' | 'copy';
  src: string;
  dest: string;
  timestamp: string;
}

interface ActivityLogProps {
  activities: Activity[];
  onUndo?: (id: number) => void;
}

const ActivityLog: React.FC<ActivityLogProps> = ({ activities, onUndo }) => {
  return (
    <div className="bg-white rounded-xl shadow-md border border-gray-100 overflow-hidden">
      <div className="p-4 bg-gray-50 border-b flex items-center justify-between">
        <h3 className="font-bold flex items-center gap-2 text-dark">
          <History size={18} className="text-primary" />
          Recent Activity
        </h3>
        <span className="text-xs text-gray-500 font-medium">{activities.length} total actions</span>
      </div>

      <div className="divide-y divide-gray-100 max-h-[400px] overflow-auto">
        {activities.length === 0 ? (
          <div className="p-8 text-center text-gray-400 italic">No recent activity.</div>
        ) : (
          activities.map((activity) => (
            <div key={activity.id} className="p-4 hover:bg-gray-50 transition-all group">
              <div className="flex items-center justify-between mb-2">
                <span className="text-sm font-bold text-dark">{activity.fileName}</span>
                <span className="text-xs text-gray-400">{activity.timestamp}</span>
              </div>
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-2 text-xs text-gray-500 truncate max-w-[80%]">
                  <span className="px-1.5 py-0.5 bg-gray-100 rounded uppercase font-bold text-[10px]">
                    {activity.action}
                  </span>
                  <span className="truncate">{activity.src}</span>
                  <ArrowRight size={12} className="shrink-0" />
                  <span className="truncate text-primary font-medium">{activity.dest}</span>
                </div>
                {onUndo && (
                  <button 
                    onClick={() => onUndo(activity.id)}
                    className="p-1.5 hover:bg-indigo-50 text-indigo-400 hover:text-primary rounded-full opacity-0 group-hover:opacity-100 transition-all"
                    title="Undo Action"
                  >
                    <RotateCcw size={14} />
                  </button>
                )}
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
};

export default ActivityLog;
