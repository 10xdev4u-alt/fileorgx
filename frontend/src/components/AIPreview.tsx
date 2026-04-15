import React, { useState } from 'react';
import { Tag as TagIcon, Folder, ShieldCheck, Edit2, Check, X } from 'lucide-react';

interface AIResult {
  category: string;
  tags: string[];
  suggested_folder: string;
  confidence: number;
}

interface AIPreviewProps {
  result: AIResult;
  fileName: string;
  onUpdate?: (updated: AIResult) => void;
}

const AIPreview: React.FC<AIPreviewProps> = ({ result: initialResult, fileName, onUpdate }) => {
  const [isEditing, setIsEditing] = useState(false);
  const [result, setResult] = useState<AIResult>(initialResult);
  const confidenceColor = result.confidence > 0.8 ? 'text-success' : 'text-warning';

  const handleSave = () => {
    setIsEditing(false);
    if (onUpdate) onUpdate(result);
  };

  return (
    <div className="bg-white rounded-xl shadow-lg border border-gray-100 p-6 max-w-md">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-bold text-dark truncate flex-1">{fileName}</h3>
        <div className="flex items-center gap-3">
          <div className={`flex items-center gap-1 font-semibold ${confidenceColor}`}>
            <ShieldCheck size={18} />
            {Math.round(result.confidence * 100)}%
          </div>
          <button 
            onClick={() => isEditing ? handleSave() : setIsEditing(true)}
            className="p-1 hover:bg-gray-100 rounded text-gray-400 hover:text-primary transition-all"
          >
            {isEditing ? <Check size={18} /> : <Edit2 size={18} />}
          </button>
        </div>
      </div>

      <div className="space-y-4">
        <div>
          <span className="text-xs font-semibold text-gray-400 uppercase tracking-wider">Category</span>
          {isEditing ? (
            <input 
              className="mt-1 w-full p-2 border rounded-lg text-sm"
              value={result.category}
              onChange={(e) => setResult({...result, category: e.target.value})}
            />
          ) : (
            <div className="mt-1 flex items-center gap-2 text-primary font-medium">
              <Folder size={18} />
              {result.category}
            </div>
          )}
        </div>

        <div>
          <span className="text-xs font-semibold text-gray-400 uppercase tracking-wider">Suggested Folder</span>
          <div className="mt-1 text-dark italic">
            /{result.suggested_folder}
          </div>
        </div>

        <div>
          <span className="text-xs font-semibold text-gray-400 uppercase tracking-wider">Tags</span>
          {isEditing ? (
            <input 
              className="mt-1 w-full p-2 border rounded-lg text-sm"
              placeholder="Comma separated tags..."
              value={result.tags.join(', ')}
              onChange={(e) => setResult({...result, tags: e.target.value.split(',').map(t => t.trim())})}
            />
          ) : (
            <div className="mt-2 flex flex-wrap gap-2">
              {result.tags.map((tag, idx) => (
                <span key={idx} className="px-3 py-1 bg-indigo-50 text-primary text-sm rounded-full flex items-center gap-1 border border-indigo-100">
                  <TagIcon size={14} />
                  {tag}
                </span>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default AIPreview;

export default AIPreview;
