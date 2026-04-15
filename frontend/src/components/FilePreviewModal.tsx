import React from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { X, ExternalLink, Download, Trash2, Info } from 'lucide-react';
import { scaleUp, fadeIn } from '../utils/animations';

interface FilePreviewModalProps {
  isOpen: boolean;
  onClose: () => void;
  file: {
    name: string;
    type: string;
    path: string;
    size: string;
  } | null;
}

const FilePreviewModal: React.FC<FilePreviewModalProps> = ({ isOpen, onClose, file }) => {
  if (!file) return null;

  return (
    <AnimatePresence>
      {isOpen && (
        <div className="fixed inset-0 z-[110] flex items-center justify-center p-10">
          <motion.div
            {...fadeIn}
            onClick={onClose}
            className="absolute inset-0 bg-dark/40 backdrop-blur-md"
          />
          
          <motion.div
            {...scaleUp}
            className="relative bg-white rounded-[40px] shadow-2xl w-full max-w-5xl h-full flex flex-col overflow-hidden"
          >
            {/* Modal Header */}
            <div className="h-20 border-b border-gray-100 flex items-center justify-between px-10 shrink-0">
              <div className="flex items-center gap-4">
                <div className="w-10 h-10 bg-indigo-50 rounded-xl flex items-center justify-center text-primary">
                  <Info size={20} />
                </div>
                <div>
                  <h3 className="font-black text-dark leading-tight">{file.name}</h3>
                  <span className="text-[10px] text-gray-400 font-bold uppercase">{file.size} • {file.type}</span>
                </div>
              </div>

              <div className="flex items-center gap-3">
                <button className="p-2.5 bg-gray-50 text-gray-500 rounded-2xl hover:bg-gray-100 transition-all">
                  <Download size={20} />
                </button>
                <button className="p-2.5 bg-gray-50 text-gray-500 rounded-2xl hover:bg-gray-100 transition-all">
                  <ExternalLink size={20} />
                </button>
                <div className="w-px h-8 bg-gray-100 mx-2" />
                <button onClick={onClose} className="p-2.5 bg-gray-50 text-gray-500 rounded-2xl hover:bg-gray-100 transition-all">
                  <X size={20} />
                </button>
              </div>
            </div>

            {/* Preview Area */}
            <div className="flex-1 bg-gray-50 overflow-auto flex items-center justify-center p-10">
              {file.type.startsWith('image/') ? (
                <img src={file.path} alt={file.name} className="max-w-full max-h-full rounded-2xl shadow-2xl" />
              ) : (
                <div className="text-center">
                  <div className="w-24 h-24 bg-white rounded-[32px] flex items-center justify-center text-gray-200 mx-auto mb-6 shadow-sm">
                    <Info size={48} />
                  </div>
                  <h4 className="text-xl font-black text-dark mb-2">No Visual Preview</h4>
                  <p className="text-gray-400 font-medium">This file type cannot be previewed directly.</p>
                </div>
              )}
            </div>

            {/* Modal Footer / Actions */}
            <div className="h-20 bg-white border-t border-gray-100 flex items-center justify-between px-10 shrink-0">
              <button className="flex items-center gap-2 text-red-500 font-bold hover:bg-red-50 px-4 py-2 rounded-xl transition-all">
                <Trash2 size={18} />
                Delete File
              </button>
              <button className="bg-primary text-white px-8 py-3 rounded-2xl font-black shadow-lg shadow-indigo-100 hover:scale-105 active:scale-95 transition-all">
                Organize This File
              </button>
            </div>
          </motion.div>
        </div>
      )}
    </AnimatePresence>
  );
};

export default FilePreviewModal;
