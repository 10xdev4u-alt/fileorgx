import React from 'react';
import { Tag as TagIcon, Folder, ShieldCheck } from 'lucide-react';

interface AIResult {
  category: string;
  tags: string[];
  suggested_folder: string;
  confidence: number;
}

interface AIPreviewProps {
  result: AIResult;
  fileName: string;
}

const AIPreview: React.FC<AIPreviewProps> = ({ result, fileName }) => {
  const confidenceColor = result.confidence > 0.8 ? 'text-success' : 'text-warning';

  return (
    <div className="bg-white rounded-xl shadow-lg border border-gray-100 p-6 max-w-md">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-bold text-dark truncate flex-1">{fileName}</h3>
        <div className={`flex items-center gap-1 font-semibold ${confidenceColor}`}>
          <ShieldCheck size={18} />
          {Math.round(result.confidence * 100)}%
        </div>
      </div>

      <div className="space-y-4">
        <div>
          <span className="text-xs font-semibold text-gray-400 uppercase tracking-wider">Suggested Category</span>
          <div className="mt-1 flex items-center gap-2 text-primary font-medium">
            <Folder size={18} />
            {result.category}
          </div>
        </div>

        <div>
          <span className="text-xs font-semibold text-gray-400 uppercase tracking-wider">Suggested Folder</span>
          <div className="mt-1 text-dark italic">
            /{result.suggested_folder}
          </div>
        </div>

        <div>
          <span className="text-xs font-semibold text-gray-400 uppercase tracking-wider">AI Tags</span>
          <div className="mt-2 flex flex-wrap gap-2">
            {result.tags.map((tag, idx) => (
              <span key={idx} className="px-3 py-1 bg-indigo-50 text-primary text-sm rounded-full flex items-center gap-1 border border-indigo-100">
                <TagIcon size={14} />
                {tag}
              </span>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default AIPreview;
