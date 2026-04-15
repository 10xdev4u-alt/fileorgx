import FileCard from './components/FileCard';

export const TestFileCards = () => {
  return (
    <div className="p-20 bg-gray-50 min-h-screen grid grid-cols-4 gap-6">
      <FileCard name="vacation_photo.jpg" type="image/jpeg" size="2.4MB" />
      <FileCard name="app_logic.ts" type="text/typescript" size="12KB" />
      <FileCard name="taxes_2024.pdf" type="application/pdf" size="1.1MB" />
      <FileCard name="notes.txt" type="text/plain" size="4KB" />
    </div>
  );
};
