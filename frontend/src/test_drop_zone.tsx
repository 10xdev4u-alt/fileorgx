import DropZone from './components/DropZone';

export const TestDropZone = () => {
  return (
    <div className="p-20 bg-gray-100 min-h-screen">
      <div className="max-w-xl mx-auto">
        <DropZone onFilesDropped={(files) => console.log("Dropped files:", files)} />
      </div>
    </div>
  );
};
