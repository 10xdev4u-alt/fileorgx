import React from 'react';
import { FileText, Image as ImageIcon, FileCode, CheckCircle2 } from 'lucide-react';
import { motion } from 'framer-motion';

interface TimelineEvent {
  id: number;
  fileName: string;
  type: 'image' | 'pdf' | 'code' | 'other';
  oldPath: string;
  newPath: string;
  timestamp: string;
}

interface TimelineProps {
  events: TimelineEvent[];
}

const Timeline: React.FC<TimelineProps> = ({ events }) => {
  return (
    <div className="flex gap-6 overflow-x-auto pb-6 scrollbar-hide py-4">
      {events.map((event, idx) => (
        <motion.div
          key={event.id}
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: idx * 0.1 }}
          className="min-w-[280px] bg-white rounded-3xl p-6 border border-gray-100 shadow-sm relative group hover:shadow-xl hover:scale-105 transition-all cursor-pointer"
        >
          <div className="absolute -top-3 -right-3 w-8 h-8 bg-success rounded-full flex items-center justify-center text-white border-4 border-gray-50 z-10">
            <CheckCircle2 size={16} />
          </div>

          <div className="flex items-center gap-4 mb-4">
            <div className="w-12 h-12 bg-indigo-50 rounded-2xl flex items-center justify-center text-primary">
              {event.type === 'image' && <ImageIcon size={24} />}
              {event.type === 'pdf' && <FileText size={24} />}
              {event.type === 'code' && <FileCode size={24} />}
              {event.type === 'other' && <FileText size={24} />}
            </div>
            <div className="overflow-hidden">
              <h4 className="font-black text-dark truncate leading-tight">{event.fileName}</h4>
              <span className="text-[10px] text-gray-400 font-bold uppercase">{event.timestamp}</span>
            </div>
          </div>

          <div className="space-y-2">
            <div className="flex flex-col">
              <span className="text-[9px] font-black text-gray-300 uppercase tracking-tighter">Moved From</span>
              <span className="text-xs text-gray-400 truncate">{event.oldPath}</span>
            </div>
            <div className="flex flex-col bg-indigo-50/50 p-2 rounded-xl border border-indigo-100/30">
              <span className="text-[9px] font-black text-primary/40 uppercase tracking-tighter">Moved To</span>
              <span className="text-xs text-primary font-bold truncate">{event.newPath}</span>
            </div>
          </div>
        </motion.div>
      ))}
    </div>
  );
};

export default Timeline;
