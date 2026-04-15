import FilePreviewModal from './components/FilePreviewModal';
import { useState } from 'react';

export const TestFilePreview = () => {
  const [isOpen, setIsOpen] = useState(false);
  const dummyFile = {
    name: "invoice_august.pdf",
    type: "application/pdf",
    path: "/fake/path/invoice.pdf",
    size: "1.2 MB"
  };

  return (
    <div className="p-20">
      <button onClick={() => setIsOpen(true)} className="bg-primary text-white p-4 rounded-xl font-bold">Open Preview</button>
      <FilePreviewModal isOpen={isOpen} onClose={() => setIsOpen(false)} file={dummyFile} />
    </div>
  );
};
