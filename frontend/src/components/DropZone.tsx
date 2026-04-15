import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { UploadCloud, File, X } from 'lucide-react';
import { scaleUp } from '../utils/animations';

interface DropZoneProps {
  onFilesDropped: (files: FileList) => void;
}

const DropZone: React.FC<DropZoneProps> = ({ onFilesDropped }) => {
  const [isDragging, setIsDragging] = useState(false);

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const handleDragLeave = () => {
    setIsDragging(false);
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);
    if (e.dataTransfer.files) {
      onFilesDropped(e.dataTransfer.files);
    }
  };

  return (
    <div
      onDragOver={handleDragOver}
      onDragLeave={handleDragLeave}
      onDrop={handleDrop}
      className={`relative w-full h-64 rounded-[40px] border-4 border-dashed transition-all duration-300 flex flex-col items-center justify-center gap-4 cursor-pointer overflow-hidden ${
        isDragging ? 'bg-primary/5 border-primary scale-[0.98]' : 'bg-gray-50 border-gray-100 hover:bg-white hover:border-gray-200'
      }`}
    >
      <div className={`w-20 h-20 rounded-3xl flex items-center justify-center transition-all duration-500 ${
        isDragging ? 'bg-primary text-white rotate-12 scale-110 shadow-2xl shadow-indigo-200' : 'bg-white text-gray-400 shadow-sm'
      }`}>
        <UploadCloud size={40} />
      </div>

      <div className="text-center">
        <h3 className={`text-xl font-black tracking-tight transition-colors ${isDragging ? 'text-primary' : 'text-dark'}`}>
          {isDragging ? 'Drop to Organize!' : 'Drag files here'}
        </h3>
        <p className="text-gray-400 text-sm mt-1 font-medium">Or click to browse your computer</p>
      </div>

      <input 
        type="file" 
        multiple 
        className="absolute inset-0 opacity-0 cursor-pointer" 
        onChange={(e) => e.target.files && onFilesDropped(e.target.files)}
      />

      <AnimatePresence>
        {isDragging && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="absolute inset-0 bg-primary/5 pointer-events-none"
          />
        )}
      </AnimatePresence>
    </div>
  );
};

export default DropZone;
