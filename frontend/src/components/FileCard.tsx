import React from 'react';
import { FileText, Image as ImageIcon, FileCode, MoreVertical, ExternalLink } from 'lucide-react';
import { motion } from 'framer-motion';
import { hoverScale } from '../utils/animations';

interface FileCardProps {
  name: string;
  type: string;
  size: string;
  thumbnail?: string;
  onAction?: () => void;
}

const FileCard: React.FC<FileCardProps> = ({ name, type, size, thumbnail, onAction }) => {
  const isImage = type.startsWith('image/');
  const isCode = type.includes('code') || name.endsWith('.ts') || name.endsWith('.py');

  return (
    <motion.div
      {...hoverScale}
      className="bg-white rounded-2xl border border-gray-100 p-4 shadow-sm group hover:shadow-xl transition-all cursor-pointer relative"
    >
      <div className="flex items-center justify-between mb-4">
        <div className="w-10 h-10 bg-gray-50 rounded-xl flex items-center justify-center text-gray-400 group-hover:bg-primary/10 group-hover:text-primary transition-colors">
          {isImage ? <ImageIcon size={20} /> : isCode ? <FileCode size={20} /> : <FileText size={20} />}
        </div>
        <button className="p-1 hover:bg-gray-50 rounded-lg text-gray-300 hover:text-dark">
          <MoreVertical size={18} />
        </button>
      </div>

      <div className="mb-4 aspect-video bg-gray-50 rounded-xl overflow-hidden flex items-center justify-center">
        {thumbnail ? (
          <img src={thumbnail} alt={name} className="w-full h-full object-cover" />
        ) : (
          <div className="text-[10px] font-black text-gray-200 uppercase tracking-widest select-none">
            No Preview
          </div>
        )}
      </div>

      <div>
        <h4 className="font-bold text-dark text-sm truncate mb-1">{name}</h4>
        <div className="flex items-center justify-between">
          <span className="text-[10px] text-gray-400 font-bold uppercase">{size}</span>
          <span className="text-[10px] text-primary/40 font-black uppercase tracking-tighter group-hover:text-primary transition-colors">
            {type.split('/')[1] || 'FILE'}
          </span>
        </div>
      </div>
      
      <div className="absolute top-4 right-12 opacity-0 group-hover:opacity-100 transition-all">
        <ExternalLink size={16} className="text-primary" />
      </div>
    </motion.div>
  );
};

export default FileCard;
